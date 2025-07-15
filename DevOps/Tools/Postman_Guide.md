# Postman 사용법

Postman은 REST API를 시각적으로 테스트하고 관리할 수 있는 툴이다.  
HTTP 메서드 설정, 요청 주소 입력, 헤더/바디 구성 등을 통해 API 요청 흐름을 직접 확인할 수 있다.

<br>

## 1. 요청 구성 흐름

1. 새 요청 생성  
2. 요청 정보 입력  
   - Method: GET / POST 등  
   - URL: 예) `https://jsonplaceholder.typicode.com/posts/1`  
   - Headers: `Content-Type`, `Authorization` 등 필요 시 설정  
   - Body: POST 등의 경우 JSON 형태 입력 (raw → JSON 설정)  
3. Send 클릭 후 응답 JSON 확인

<br><br>

## 2-1. GET 예시 (JSONPlaceholder)
JSONPlaceholder는 실습용 MockData를 제공하는 API다. 
```
GET https://jsonplaceholder.typicode.com/posts/1
```
응답:
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

<br>

## 2-0. 쿼리 파라미터가 많은 경우

GET 요청 시, URL에 여러 개의 쿼리 파라미터가 포함될 수 있다.  
예를 들어 아래와 같이 도메인에 이미 쿼리 스트링이 붙은 URL을 입력하면,  
Postman에서는 자동으로 이를 파싱하여 Params 탭에 각 항목이 분리되어 표시된다.

예시:
```
https://example.com/search?query=apple&limit=10&page=2
```

→ 이 URL을 그대로 입력하면 아래처럼 표 형식으로 자동 분리된다:

| KEY     | VALUE  |
|---------|--------|
| query   | apple  |
| limit   | 10     |
| page    | 2      |

직접 추가하거나 수정할 수도 있으며, 이를 통해 URL을 매번 다시 작성할 필요 없이 편리하게 파라미터 관리가 가능하다.

<br>

## 2-2. POST 예시 (DeepL API)
```
curl -X POST 'https://api-free.deepl.com/v2/translate' \
--header 'Authorization: DeepL-Auth-Key [yourAuthKey]' \
--header 'Content-Type: application/json' \
--data '{
  "text": ["안녕하세요. 오늘 날씨가 좋네요"],
  "target_lang": "EN"
}'
```
응답:
```json
{
  "translations": [
    {
        "detected_source_language": "KO",
        "text": "Hello, it's a beautiful day"
    }
  ]
}
```

<br><br>

## 1-1. POST 방식의 종류

POST 요청 시 Body 입력 방식은 다양하며, 목적에 따라 선택해야 한다.  
Postman에서는 `Body` 탭에서 다음과 같은 포맷을 제공한다:

| 타입 | 설명 | 사용 예 |
|------|------|---------|
| raw (JSON) | JSON 포맷으로 데이터 전송 | 대부분의 RESTful API (ex: DeepL API) |
| x-www-form-urlencoded | HTML Form 방식처럼 key-value 쌍 전송 | 로그인/회원가입 API, 레거시 시스템 |
| form-data | 파일 업로드 및 멀티파트 데이터 전송 | 이미지 첨부 API 등 |
| GraphQL | GraphQL 쿼리 전송 | 특정 API 서버에서만 사용 |

<br><br>

예를 들어, 일반적인 JSON 전송이라면 `raw`를 선택하고 `Content-Type: application/json`을 설정한다.  
반면, `x-www-form-urlencoded` 방식이 요구된다면 `Headers`는 자동으로 `application/x-www-form-urlencoded`로 지정되며,  
`key-value` 입력칸에서 각각 값을 입력해 요청을 구성해야 한다.

이 차이를 이해하면 API 명세서를 보고 어떤 방식으로 Body를 구성할지 빠르게 판단할 수 있다.

<br><br>

## HISTORY
- 250715 : 초안작성
