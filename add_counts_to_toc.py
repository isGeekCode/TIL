#!/usr/bin/env python3
"""
README.md의 TOC에 각 섹션의 글 개수를 추가하는 스크립트
헤더는 그대로 유지하고, TOC의 링크에만 개수를 추가합니다.
"""
import re
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
README_PATH = SCRIPT_DIR / "README.md"

def get_file_content_size(file_path):
    """파일의 내용이 있는지 확인 (100자 이상이면 내용 있음으로 판단)"""
    try:
        if not file_path.exists():
            return 0
        content = file_path.read_text(encoding='utf-8').strip()
        return len(content) if len(content) >= 100 else 0
    except:
        return 0

def extract_section_counts(readme_content):
    """각 ##, ### 헤더 섹션의 파일 개수를 계산 (상위 섹션은 하위 섹션 합계 포함)"""

    section_pattern = r'^(##+)\s+(.+?)$'
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    lines = readme_content.split('\n')
    section_counts = {}
    section_stack = []  # (level, name) 스택

    for line in lines:
        # 헤더 찾기
        header_match = re.match(section_pattern, line)
        if header_match:
            level = len(header_match.group(1))  # ## = 2, ### = 3
            header_name = header_match.group(2).strip()
            # 기존 (숫자) 제거
            header_name = re.sub(r'\s*\(\d+\)\s*$', '', header_name)
            full_header = '#' * level + ' ' + header_name

            # 현재 레벨보다 깊은 섹션 제거
            while section_stack and section_stack[-1][0] >= level:
                section_stack.pop()

            # 현재 섹션 추가
            section_stack.append((level, full_header))

            # 섹션 초기화
            if full_header not in section_counts:
                section_counts[full_header] = 0
            continue

        # 파일 링크 찾기 (현재 활성화된 모든 섹션에 추가)
        if section_stack:
            for match in re.finditer(link_pattern, line):
                link_url = match.group(2)

                # 외부 링크나 앵커 링크는 제외
                if link_url.startswith('http') or link_url.startswith('#'):
                    continue

                # 파일 경로 확인
                file_path = SCRIPT_DIR / link_url
                if get_file_content_size(file_path) > 0:
                    # 모든 상위 섹션에 카운트 추가
                    for level, section_name in section_stack:
                        section_counts[section_name] += 1

    return section_counts

def header_to_anchor(header_text):
    """헤더 텍스트를 GitHub/Obsidian 앵커 형식으로 변환"""
    # ##, ### 제거
    text = re.sub(r'^##+\s+', '', header_text)
    # 소문자 변환
    text = text.lower()
    # 이모지 제거 (공백은 유지!)
    text = re.sub(r'[\U0001F000-\U0001F9FF\U00002600-\U000027BF\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F900-\U0001F9FF]', '', text)
    # 특수문자 제거 (한글, 영문, 숫자, 공백, 하이픈만 유지)
    text = re.sub(r'[^\w가-힣\s-]', '', text)
    # 공백을 하이픈으로
    text = text.replace(' ', '-')
    return '#' + text

def add_counts_to_toc(readme_content, section_counts):
    """TOC의 링크에 개수를 추가"""

    # 섹션 이름을 앵커로 변환한 딕셔너리 생성
    anchor_to_count = {}
    for section_name, count in section_counts.items():
        section_anchor = header_to_anchor(section_name)
        anchor_to_count[section_anchor] = count

    lines = readme_content.split('\n')
    result_lines = []

    # TOC 링크 패턴: - [텍스트](앵커)
    toc_link_pattern = r'^(\s*-\s*)\[([^\]]+)\]\((#[^)]+)\)(.*)$'

    for line in lines:
        match = re.match(toc_link_pattern, line)
        if match:
            indent = match.group(1)
            link_text = match.group(2)
            anchor = match.group(3)
            rest = match.group(4)

            # 기존 (숫자) 표시를 모두 제거 (link_text와 rest 둘 다)
            clean_text = re.sub(r'\s*\(\d+\)', '', link_text).strip()
            clean_rest = re.sub(r'^\s*\(\d+\)', '', rest)
            # 공백-로 시작하면 그대로 붙이기 (기존 공백 유지), 나머지는 공백 추가
            if clean_rest and not clean_rest.startswith(' -'):
                clean_rest = ' ' + clean_rest

            # 앵커로 개수 찾기
            count = anchor_to_count.get(anchor)

            # 개수 추가 (링크 바깥에)
            if count is not None and count > 0:
                new_line = f"{indent}[{clean_text}]({anchor}) ({count}){clean_rest}"
            else:
                new_line = f"{indent}[{clean_text}]({anchor}){clean_rest}"

            result_lines.append(new_line)
        else:
            result_lines.append(line)

    return '\n'.join(result_lines)

def main():
    """메인 함수"""
    print(f"📊 README TOC에 글 개수 추가 시작\n")

    if not README_PATH.exists():
        print(f"❌ ERROR: README.md를 찾을 수 없습니다: {README_PATH}")
        return

    # README 읽기
    print("1. README.md 읽는 중...")
    readme_content = README_PATH.read_text(encoding='utf-8')

    # 섹션별 개수 계산
    print("2. 각 섹션의 글 개수 계산 중...")
    section_counts = extract_section_counts(readme_content)

    print(f"\n찾은 섹션: {len(section_counts)}개")
    print("\n주요 섹션 개수 (상위 10개):")
    sorted_sections = sorted(section_counts.items(), key=lambda x: x[1], reverse=True)
    for section, count in sorted_sections[:10]:
        if count > 0:
            print(f"  - {section}: {count}개")

    # TOC에 개수 추가
    print("\n3. TOC에 개수 추가 중...")
    updated_content = add_counts_to_toc(readme_content, section_counts)

    # 백업 생성
    backup_path = SCRIPT_DIR / "README.md.backup"
    print(f"\n4. 백업 생성: {backup_path}")
    backup_path.write_text(readme_content, encoding='utf-8')

    # 저장
    print("5. 업데이트된 README.md 저장 중...")
    README_PATH.write_text(updated_content, encoding='utf-8')

    print("\n✅ 완료!")
    print(f"   백업 파일: {backup_path}")

if __name__ == "__main__":
    main()
