# iOS와 HTTP/2에 대하여

HTTP/2는 인터넷에서 데이터를 전송하는 프로토콜이다.

## HTTP/2의 특징

- HTTP/2는 인터넷에서 데이터를 전송하는 프로토콜 중 하나이다.
- HTTP/2는 이전 버전인 HTTP/1.1보다 빠르고 효율적으로 데이터를 전송할 수 있다.
- HTTP/2는 하나의 연결로 여러 개의 요청과 응답을 처리할 수 있다.
- HTTP/2는 서버와 클라이언트 간의 압축을 지원하여 네트워크 대역폭을 절약할 수 있다.
- HTTP/2는 TLS(Transport Layer Security)를 강제로 적용하여 보안성을 높인다다.
- iOS는 HTTP/2를 지원한다. HTTP/2를 사용하면 iOS 디바이스에서 웹 사이트를 더 빠르게 로드할 수 있다. 또한, HTTP/2의 기능을 활용하여 애플리케이션에서 데이터를 빠르고 효율적으로 전송할 수 있다.

### 멀티플렉싱(multiplaxing)
HTTP/2의 주요 특징 중 하나는 멀티플렉싱(multiplexing)이다. 이전 버전인 HTTP/1.1에서는 클라이언트가 서버에 요청을 보내면, 서버는 해당 요청에 대한 응답을 전송한 후에 다음 요청을 처리할 수 있었다. 이로 인해 요청과 응답이 직렬적으로 처리되어 느린 속도와 지연 현상이 발생할 수 있었다.

하지만 HTTP/2에서는 하나의 연결로 여러 개의 요청과 응답을 처리할 수 있으며, 요청과 응답이 동시에 처리되어 멀티플렉싱을 구현할 수 있다. 이를 통해 네트워크 대역폭을 더욱 효율적으로 사용할 수 있다.

### 헤더압축 및 스트림 우선순위 지정
헤더 압축은 요청과 응답의 헤더를 압축하여 데이터 크기를 줄일 수 있다. 스트림 우선순위 지정은 클라이언트가 요청을 보낼 때, 요청의 우선순위를 지정하여 중요한 요청에 대한 응답을 더욱 빠르게 처리할 수 있도록 한다.

### TLS(Transport Layer Security)
HTTP/2는 TLS를 강제로 적용하여 보안성을 높일 수 있다. 이를 통해 암호화된 데이터를 전송하여 중간자 공격 등의 보안 위협으로부터 안전한 데이터 전송을 보장할 수 있다.

## iOS에서의 사용

iOS에서 HTTP/2는 이미 상용화되어 있다. Apple은 iOS 9부터 Safari 브라우저에서 HTTP/2를 지원했으며, 이후 iOS 버전에서도 HTTP/2를 계속해서 지원하고 있다.

또한, iOS에서는 NSURLSession과 Alamofire와 같은 네트워크 프레임워크를 사용하여 HTTP/2를 지원하고 있다. NSURLSession은 iOS 9부터 HTTP/2를 기본 프로토콜로 사용하도록 설정되어 있다. Alamofire는 iOS 9 이상에서 HTTP/2를 지원하며, 기본적으로 HTTP/2를 사용하도록 설정되어 있다.

따라서 iOS 애플리케이션을 개발할 때, HTTP/2를 사용하여 더욱 빠르고 안전한 데이터 전송을 구현할 수 있다.

다만 코드로 구현을 할때, HTTP/1.1과 HTTP/2를 구분할 필요는 없다.