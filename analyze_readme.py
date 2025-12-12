#!/usr/bin/env python3
"""
README.md의 링크를 분석하여 통계를 출력하는 스크립트
"""
import re
import os
from pathlib import Path
from collections import defaultdict

# 현재 스크립트의 디렉토리를 기준으로 경로 설정
SCRIPT_DIR = Path(__file__).parent
README_PATH = SCRIPT_DIR / "README.md"

def get_file_content_size(file_path):
    """파일의 내용 크기를 확인 (바이트)"""
    try:
        if not file_path.exists():
            return -1  # 파일 없음

        content = file_path.read_text(encoding='utf-8')
        # 공백, 개행 등을 제외한 실제 내용만 계산
        stripped_content = content.strip()

        return len(stripped_content)
    except Exception as e:
        return -2  # 에러

def analyze_markdown_links(readme_content):
    """README의 마크다운 링크를 분석"""

    # 마크다운 링크 패턴: [텍스트](링크)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    stats = {
        'total_links': 0,
        'external_links': 0,
        'anchor_links': 0,
        'file_links': 0,
        'files_with_content': 0,
        'empty_files': 0,
        'missing_files': 0,
        'error_files': 0,
    }

    files_by_category = {
        'with_content': [],
        'empty': [],
        'missing': [],
        'error': []
    }

    for match in re.finditer(link_pattern, readme_content):
        link_text = match.group(1)
        link_url = match.group(2)

        stats['total_links'] += 1

        # 외부 링크
        if link_url.startswith('http'):
            stats['external_links'] += 1
            continue

        # 앵커 링크
        if link_url.startswith('#'):
            stats['anchor_links'] += 1
            continue

        # 파일 링크
        stats['file_links'] += 1

        # 상대 경로를 절대 경로로 변환
        file_path = SCRIPT_DIR / link_url

        # 파일 내용 확인
        content_size = get_file_content_size(file_path)

        if content_size == -1:
            stats['missing_files'] += 1
            files_by_category['missing'].append((link_text, link_url))
        elif content_size == -2:
            stats['error_files'] += 1
            files_by_category['error'].append((link_text, link_url))
        elif content_size < 100:  # 100자 미만은 빈 파일로 간주
            stats['empty_files'] += 1
            files_by_category['empty'].append((link_text, link_url, content_size))
        else:
            stats['files_with_content'] += 1
            files_by_category['with_content'].append((link_text, link_url, content_size))

    return stats, files_by_category

def main():
    """메인 함수"""
    print(f"📊 README.md 링크 분석 시작\n")
    print(f"README 경로: {README_PATH}\n")

    # README 파일 읽기
    if not README_PATH.exists():
        print(f"❌ ERROR: README.md를 찾을 수 없습니다: {README_PATH}")
        return

    readme_content = README_PATH.read_text(encoding='utf-8')

    # 링크 분석
    stats, files_by_category = analyze_markdown_links(readme_content)

    # 통계 출력
    print("=" * 60)
    print("📈 전체 통계")
    print("=" * 60)
    print(f"전체 링크 수: {stats['total_links']}")
    print(f"  - 외부 링크 (http): {stats['external_links']}")
    print(f"  - 앵커 링크 (#): {stats['anchor_links']}")
    print(f"  - 파일 링크: {stats['file_links']}")
    print()
    print(f"파일 링크 상세:")
    print(f"  ✅ 내용 있는 파일: {stats['files_with_content']} ({stats['files_with_content']/stats['file_links']*100:.1f}%)")
    print(f"  📝 빈 파일 (100자 미만): {stats['empty_files']} ({stats['empty_files']/stats['file_links']*100:.1f}%)")
    print(f"  ❌ 파일 없음: {stats['missing_files']} ({stats['missing_files']/stats['file_links']*100:.1f}%)")
    if stats['error_files'] > 0:
        print(f"  ⚠️  읽기 에러: {stats['error_files']}")
    print()

    # 빈 파일 목록 출력 (처음 10개만)
    if files_by_category['empty']:
        print("=" * 60)
        print(f"📝 빈 파일 목록 (처음 10개)")
        print("=" * 60)
        for i, (text, url, size) in enumerate(files_by_category['empty'][:10], 1):
            print(f"{i:2d}. [{text}]({url}) - {size}자")
        if len(files_by_category['empty']) > 10:
            print(f"    ... 외 {len(files_by_category['empty']) - 10}개")
        print()

    # 파일 없음 목록 출력 (처음 10개만)
    if files_by_category['missing']:
        print("=" * 60)
        print(f"❌ 파일 없음 목록 (처음 10개)")
        print("=" * 60)
        for i, (text, url) in enumerate(files_by_category['missing'][:10], 1):
            print(f"{i:2d}. [{text}]({url})")
        if len(files_by_category['missing']) > 10:
            print(f"    ... 외 {len(files_by_category['missing']) - 10}개")
        print()

    # 결론
    print("=" * 60)
    print("💡 결론")
    print("=" * 60)
    total_problematic = stats['empty_files'] + stats['missing_files']
    problematic_ratio = total_problematic / stats['file_links'] * 100 if stats['file_links'] > 0 else 0

    if problematic_ratio < 10:
        print(f"✅ 문제 비율: {problematic_ratio:.1f}% - 낮은 편입니다.")
        print("   → 링크 제거 작업을 진행하면 좋을 것 같습니다.")
    elif problematic_ratio < 30:
        print(f"⚠️  문제 비율: {problematic_ratio:.1f}% - 보통입니다.")
        print("   → 링크 제거 또는 섹션 분리를 고려하세요.")
    else:
        print(f"❌ 문제 비율: {problematic_ratio:.1f}% - 높은 편입니다.")
        print("   → 섹션을 분리하는 것을 권장합니다.")
        print("   → '✅ 작성 완료' / '📝 작성 예정' 섹션으로 나누기")

if __name__ == "__main__":
    main()
