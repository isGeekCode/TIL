# Commit Template - 소스트리

원하는 내용으로 템플릿을 하나 생성한다. 

확장자는 txt, md 모두 인식한다. 


## Commit Template

설정 - 커밋템플릿 메뉴 



### Default

소스트리 Preference에서 Commit Template을 설정한 내용으로 적용된다. 

아래화면은 소스트리 Preference 화면

<img width="676" alt="스크린샷 2022-12-01 오후 12 43 48" src="https://user-images.githubusercontent.com/76529148/204977300-d56796cb-55c2-423a-a40b-20dd13f7ca4f.png">


### Custom

이곳에서 각각 버튼을 눌러 하단에 작성할 수도 있고

우측 Import버튼을 눌러 만들어둔 템플릿을 가져올 수도 있다.

!! 가져와서 하단에 입력을 하는 방식이기 때문에 하단을 수정하면 반영되니 조심

<img width="567" alt="스크린샷 2022-12-01 오후 12 42 00" src="https://user-images.githubusercontent.com/76529148/204977306-2814ec51-bd7a-4432-962c-79e6a1bb15a2.png">



### 반영한 모습

자동으로 생성된다.

<img width="1421" alt="스크린샷 2022-12-01 오후 1 05 14" src="https://user-images.githubusercontent.com/76529148/204977311-ef85b318-ef09-4f95-ad84-ac0e5db3a91c.png">



### 삭제하기

삭제하는 경우  없음을 클릭하고 확인을 누른다. 

바로 변경은 안되니 소스트리를 종료하고 재실행하면 반영된다. 



### 예시에 사용한 template파일

```
[타입] 파일위치 - 제목
# [CHORE] MainVC - getAPI함수 추가
# 바로 아래 공백 유지 (제목과 본문의 분리를 위함)

# Body Message (선택사항)
# 본문(구체적인 내용)을 아랫줄에 작성
# 여러 줄의 메시지를 작성할 땐 "-"로 구분 (한 줄은 72자 이내)

################
# --- COMMIT END ---
# <type> list
#   [CHORE]    : 코드 수정, 내부 파일 수정, 주석 , 빌드업무수정, 패키지 매니저 수정
#   [FEAT]     : 새로운 기능 구현 
#   [ADD]      : Feat 이외의 부수적인 코드 추가, 라이브러리 추가, 새로운 파일 생성 시, 에셋 추가 
#   [FIX]      : 버그, 오류 해결 
#   [DEL]      : 쓸모없는 코드 삭제 
#   [DOCS]     :  README나 WIKI 등의 문서 개정
#   [MOVE]     : 프로젝트 내 파일이나 코드의 이동
#   [RENAME]   :  파일 이름 변경이 있을 때 사용합니다 
#   [REFACTOR] : 전면 수정이 있을 때 사용합니다 
#   [INIT]     : 프로젝트 생성
#   [TEST]     : 테스트관련 추가 및 수정
# ------------------

# Remember me ~
#   Do not end the subject line with a period
#     제목 끝에 마침표(.) 금지
#   Separate subject from body with a blank line
#     제목과 본문을 한 줄 띄워 분리하기 (빈 행으로 구분)
# ------------------
```
