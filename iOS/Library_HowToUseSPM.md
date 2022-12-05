# 깃으로 SPM 설치하기

공부날짜: 2022년 5월 24일 오후 4:19

1. 원하는 깃의 브랜치에서 Git 링크를 가져온다.
2. 설치할 Xcode 프로젝트 - Target - General - Frameworks,Libraries, and Embedded Content + 버튼
3. 하단 Add Other - Add Package Dependency

<img width="519" alt="스크린샷_2022-05-24_오후_3 48 23" src="https://user-images.githubusercontent.com/76529148/169972685-974d0107-ec62-4d25-b0da-97fdc328ec89.png">
    
4. 복사해온 깃주소 붙여넣기
    
![스크린샷_2022-05-24_오후_4 14 30](https://user-images.githubusercontent.com/76529148/169972677-5c5ca5a0-7077-48ff-abd2-a34fbf1c57e6.png)
    
5. SPM은 버전, 브랜치, 커밋 ID를 입력해서 특정 버전, 커밋, 브랜치의 라이브러리를 추가를 할 수 있습니다.
    
    브랜치로 관리를 진행하고 있는 경우 브랜치 명을 입력해서 해당 브런치로 라이브러리 추가 가능
    
![스크린샷_2022-05-24_오후_4 17 03](https://user-images.githubusercontent.com/76529148/169972669-00e8652b-6711-4fce-b609-55e5d0ee5daf.png)

추가가 완료가 되면 왼쪽 프로젝트 네비게이터에서 SPM으로 추가한 라이브러리를 확인 할 수 있습니다.

6. 프레임워크 사용방법은 사용하려는 소스파일에서 상단에 import를 통해 사용이 가능
