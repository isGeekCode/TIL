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
    """각 ## 헤더 섹션의 파일 개수를 계산"""

    # ## 헤더로 섹션 분리
    section_pattern = r'^(##\s+.+?)$'
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    lines = readme_content.split('\n')
    section_counts = {}
    current_section = None
    current_section_name = None

    for line in lines:
        # ## 헤더 찾기
        header_match = re.match(section_pattern, line)
        if header_match:
            current_section = header_match.group(1)
            # 기존에 (숫자) 표시가 있으면 제거
            current_section_name = re.sub(r'\s*\(\d+\)\s*$', '', current_section).strip()
            if current_section_name not in section_counts:
                section_counts[current_section_name] = 0
            continue

        # 현재 섹션에서 파일 링크 찾기
        if current_section_name:
            for match in re.finditer(link_pattern, line):
                link_url = match.group(2)

                # 외부 링크나 앵커 링크는 제외
                if link_url.startswith('http') or link_url.startswith('#'):
                    continue

                # 파일 경로 확인
                file_path = SCRIPT_DIR / link_url
                if get_file_content_size(file_path) > 0:
                    section_counts[current_section_name] += 1

    return section_counts

def add_counts_to_toc(readme_content, section_counts):
    """TOC의 링크에 개수를 추가"""

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

            # 기존 (숫자) 표시 제거
            clean_text = re.sub(r'\s*\(\d+\)\s*$', '', link_text).strip()

            # 섹션 카운트에서 매칭되는 항목 찾기
            count = None
            for section_name, section_count in section_counts.items():
                # 이모지와 텍스트 부분만 비교 (## 제거)
                section_clean = re.sub(r'^##\s+', '', section_name).strip()
                if section_clean in clean_text or clean_text in section_clean:
                    count = section_count
                    break

            # 개수 추가 (링크 바깥에)
            if count is not None and count > 0:
                new_line = f"{indent}[{clean_text}]({anchor}) ({count}){rest}"
            else:
                new_line = f"{indent}[{clean_text}]({anchor}){rest}"

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
