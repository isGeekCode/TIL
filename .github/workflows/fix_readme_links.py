# fix_readme_links.py

# Python 스크립트 코드를 작성하여 README 파일을 수정하는 작업을 수행합니다.
# 아래는 예시 코드입니다. README 파일을 수정하는 작업을 여기에 추가하세요.

# 예시: README 파일의 링크들을 소문자로 변경
import re

def fix_readme_links(readme_content):
    fixed_content = re.sub(r'\[(.*?)\]\(#(.*?)\)', lambda x: f"[{x.group(1)}](#{x.group(2).lower()})", readme_content)
    return fixed_content

try:
    # README 파일의 내용을 읽어옴
    with open("README.md", "r") as file:
        readme_content = file.read()

    # 링크 수정
    fixed_content = fix_readme_links(readme_content)

    # 수정된 내용을 README 파일에 다시 씀
    with open("README.md", "w") as file:
        file.write(fixed_content)

    print("README 파일이 성공적으로 수정되었습니다.")
except Exception as e:
    print("스크립트 실행 중 오류가 발생했습니다:", e)
