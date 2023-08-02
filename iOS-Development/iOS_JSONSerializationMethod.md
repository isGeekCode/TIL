# iOS에서 직렬화하기 : iOS JSONSerialization
- 참고링크
    - [TIL: 직렬화(Serialization)](https://github.com/isGeekCode/TIL/blob/main/ComputerScience/Serialization.md)
    - [TIL: JSONSerialization으로  직렬화하기](https://github.com/isGeekCode/TIL/blob/main/iOS-Foundation/Foundation_JSONSerialization.md)
    - [TIL: Codable로 직렬화하기]()


주로 아래와 같은 두가지 주요기능을 수행한다.

- Serialization : Dictionary or Array -> JSON Data
- Deserialization : JSON Data -> Dictionary or Array

간단하게 말해서, 직렬화와 역직렬화를 수행해주는 클래스이다.
일단 직렬화 방법은 

직렬화방법은 아래 세가지가 있다.
- 문자열로 JSONData만들기
- JSONSerialization을 이용해 JSONData만들기
- Codable을 이용해 JSONData만들기

좀더 세부적으로 보여주면

- String protocol을 이용해 JSONData만들기
- JSONSerialization을 이용해 JSONData만들기
    - Dictionary 타입으로 JSONData만들기
    - Array 타입으로 JSONData만들기
    - Dictionary / Array 를 혼합하여 JSONData만들기
- Codable protocol을 이용해 JSONData만들기
    - 객체를 Codable을 이용해서 JSONData만들기
    - 복잡한 데이터 구조를 가진 객체를 Codable을 이용해서 JSONData만들기


<br><br>

## 직렬화하기 

### 문자열로 JSONData 만들기
전체적인 단계는 아래와 같다.

- 문자열 생성
- JSON문자열을 JSON데이터로 변환
- JSON데이터를 파싱하여 Foundation 객체로 변환

### JSONSerialization을 이용해 JSONData만들기
이 방법은 아래 링크를 참고하자.
- []()


### Codable protocol을 이용해 JSONData만들기


<br><br>

<br><br><br>
## History
- 230802 : 초안작성
