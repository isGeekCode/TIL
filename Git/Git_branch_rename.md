# 브랜치 이름 변경하기

가끔 기존 브랜치를 롤백하거나, 신규 개발이 무산되는 등의 이유로   

브랜치의 이름을 변경해야하는 경우가 있다.  

<br><br>

입력할 형태는 아래와 같다.  
```
// 브랜치명 변경
git branch -m [기존 브랜치명] [새로운 브랜치명]

// 기존 origin에 반영
git push origin :[기존 브랜치명]
```

오늘은 develop 브랜치의 이름을 `Legacy_InStore` 라는 이름으로 바꾸는 상황이다.    

이를 반영한 전체코드는 아래와 같다.  

```
git branch -m develop Legacy_InStore
git push origin :develop
``` 

그럼 아래와 같이 기존 브랜치명이 삭제됐다는 메세지가 생성된다.  

``` 
To http://@@@@@@.git
 - [deleted]         develop
``` 

<br><br>

## 변경 내용없이 커밋메세지 넣기
브랜치명을 변경하고 해당 내용을 다른 변경내용 없이 커밋메세지만 넣고 싶다면  
아래와 같이 입력한다.  
```
git commit --allow-empty -m "Empty Commit Message"
```

