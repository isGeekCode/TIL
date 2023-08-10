# .github/workflows/update_readme.py

import os
import re
import requests
from datetime import datetime

def generate_readme(data):
    readme_content = f"""# TIL
> Today I Learned

A collection of concrete writeups of small things I learn daily while working and researching. My goal is to work in public. I was inspired to start this repository after reading Simon Wilson's [hacker new post][1], and he was apparently inspired by Josh Branchaud's [TIL collection][2].

_{data['total_tils']} TILs and counting..._

---

{generate_recent_tils(data['recent_tils'])}

{generate_categories(data['categories'])}
"""
    return readme_content

def generate_recent_tils(recent_tils):
    if not recent_tils:
        return ""

    recent_tils_content = "### 2 most recent TILs\n"
    for til in recent_tils:
        recent_tils_content += f"- [{til['title']}]({til['category']}/{til['filename']}) - {til['date']}\n"
    return recent_tils_content

def generate_categories(categories):
    categories_content = "### Categories\n"
    for category in categories:
        categories_content += f"- [{category}]#{category}\n"
    return categories_content

def main():
    try:
        # Fetch data or generate data as needed
        data = {
            "total_tils": 3,
            "recent_tils": [
                {"title": "How to add a CSS border", "category": "css", "filename": "how-to-add-a-border.md", "date": "Sat Apr 25 19:39:03 2020 +0800"},
                {"title": "How to make a div", "category": "html", "filename": "how-to-make-a-div.md", "date": "Sat Apr 25 17:53:55 2020 +0800"}
            ],
            "categories": ["css", "html", "k8s"]
        }

        generated_readme = generate_readme(data)

        # Write generated content to README.md
        with open("README.md", "w") as readme_file:
            readme_file.write(generated_readme)

        print("README 파일이 성공적으로 업데이트되었습니다.")
    except Exception as e:
        print("스크립트 실행 중 오류가 발생했습니다:", e)

if __name__ == "__main__":
    main()
