소켓이란

**TIL220420_socket**

0. 서론
   오늘 몇시간을 소켓통신에 대하여 조사를 했는데 생각보다 많은 자료를 찾지는 못했다.

한번 다시 정리해야할 자료이므로 참고 부탁드립니다.

한번 쭉 읽어보셔도 좋을 거에요

1. 선행지식
   📌

📌

2. 개념
   소켓이란
   정규 유닉스 파일 기술자를 이용하여 다른 프로그램과 정보를 교환하는 방법

용어 설명
유닉스는 운영체제 중 하나입니다. 유닉스에서는 모든 것이 파일로 존재하게 됩니다.

그리고 소켓도 유닉스에서 파일 로 취급받습니다.

모든 유닉스 프로그램은 파일 기술자(File Descriptor) 라는 것을 통해서 입출력(read, write)을 실행합니다.

파일 기술자는 열린 파일을 의미하는 인덱스 번호입니다.

비슷한 맥락으로 **소켓 기술자(Socket Descriptor)**는 소켓을 만들고 얻은 파일 기술자를 뜻하는 것이죠

정리
서버와 소켓 통신을 하기 위해서는 소켓을 생성하는 작업이 필요합니다.

socket()이라는 함수를 통해 내부적으로 소켓에 사용할 파일을 하나 열고

해당 파일의 인덱스 번호를 소켓함수가 return하게 됩니다.

이때 이 인텍스 번호가 **소켓 기술자(Socket Descriptor)**가 되는 것이고 해당 소켓 기술자를 활용하여 send(), recv() 하여 통신을 하는 것입니다.

만약 소켓을 무한대로 생성해서 더 이상 파일을 열지 못한다면, 소켓 생성 에러가 발생.

따라서 소켓 통신을 소켓 기술자를 이용하여 send, recv를 하는 통신이라고 이해해 볼 수 있습니다.

소켓 기술자는 열려진 파일의 index이기 때문에, 정수형으로 되어 있어요.

내가 만약 A라는 소켓을 만들고 그 소켓 기술자가 3이라면, B라는 소켓을 만들면 그 소켓 기술자는 4. 이런 식으로 생각하시면 됩니다.

(파일 기술자의 0,1,2는 이미 할당되어 있어서 3부터 쓸 수 있습니다)

iOS에서 소켓 통신
C언어와 같은 low-level인 경우 경우 소켓기술자를 직접 이용해서 소켓을 구현하게 됩니다. 주소와 포트번호를 설정하는 과정에허 리틀앤디안, 빅앤디안을 바꿔주는 작업이 필요로 하고

또 connect() 호출 후 성공할 때 send(), recv()과 같은 메서드를 호출해야 합니다.

서버 사이드에서 보자면, bind(), listen(), accep()와 같은 작업이 추가될 뿐 아니라 데이터가 block되지 않게 좀 더 복잡한 작업을 추가해야 합니다.

int sock_fd;
sock_fd = socket(AF_INET, SOCK_STREAM, 0);
소켓 기술자인 sock_fd는 정수형 자료형이기 때문에,

리틀앤디안, 빅앤디안을 신경써서 바꿔주는 작업(htons 등)도 해야해요.

간단히 주소와 포트 번호를 설정하더라도 다음과 같이 말이졍.

struct sockaddr_in addr;

addr.sin_family = AF_INET;
addr.sin_port = htons(port);
addr.sin_addr.s_addr = htonl(INADDR_ANY);
뭐 이 뒤로도 connect()를 호출하고 성공 시 send()/recv(), 끝낼 시 close() 등을 호출 하는게

일반적인 socket client 통신이에요.

(서버라면 bind(), listen(), accept() 작업들이 추가)

더 나아가 읽을 데이터가 있을 때까지 blocking(블로킹) 되지 않게 더 심화된 작업들도 추가해줘야 돼요

Stream
이러한 복잡한 작업이 좀더 하이레벨의 언어인 iOS에서는 추상화가 되어있습니다. 모든 건 다 프레임워크화 되어있어, 상위레벨에서 제공하는 메서드를 가져다 사용하면 됩니다. 소켓통신은 소켓 기술자라는 것을 이용해 send, recv를 하는 통신이구나! 정도만 이해

IP, Port만 알아도 통신이 가능!

소켓의 종류

1. TCP(Transmission Control Protocol)
   → Stream Socket
   데이터를 메세지 형태로 보내기 위해 IP와 함께 사용되는 프로토콜이 바로 TCP입니다.

IP가 데이터 배달을 처리하고,
TCP는 데이트 패킷을 추적 & 관리하게 됩니다.
데이터를 보낼 때 한 번에 온전한 데이터를 보내는 것 보다 효율성을 위해 데이터를 조각 으로 나누어서 보내게 됩니다. 이 과정에서 나뉜 데이터 조각을 패킷 이라 부르는 것입니다.
TCP는 각 데이터 패킷에 번호를 부여하여 패킷이 중간에 손실된 부분이 없는지 검증을하고, 목적지에서 나누어진 패킷을 온전한 데이터가 될 수 있도록 재조립을 하게됩니다.
이렇게 패킷에 번호를 부여하고 재조립하는 과정을 추적관리 라고 볼 수 있습니다.

<aside> 💡 IP, Port IP 주소로 Socket이 연결되면 해당 컴퓨터들끼리 연결이 되는 것입니다.

Port란, 해당 컴퓨터 안에서 어떤 프로세스에 연결할 것인가 입니다.(컴퓨터 안에 여러 프로세스들이 실행 중일 수 있으니) 아파트 주소가 IP라면, Port는 호수입니다

</aside>

TCP 소켓의 특징은 다음과 같습니다.

⦁ 연결형 서비스로 안정성, 신뢰성을 보장한다.

⦁ 발신자와 수신자를 연결하여 논리적 경로(가상 회선 방식)을 배정한다.

⦁ 3-Way Handshake 방식을 통해 연결을 맺고, 4-Way Handshake를 통해 해제한다.

⦁ 서버가 응답을 주지 않으면 계속적으로 요청하게 된다. (어느 시점에 포기할 수도 있음)

⦁ 서로 데이터를 주고받을 수 있는 양방향 통신이며, 일대일 통신(unicast)이다.

⦁ 패킷의 순서는 정확히 유지되고, 에러도 교정된다.

⦁ 데이터 흐름 제어 및 혼잡 제어가 가능하다.

⦁ UDP 보다 속도가 느리다.

3-Way Handshake는,

목적지와 수신지를 정확히 하여 정확한 전송을 보장하기 위해 하는 것입니다.

그렇다면, 어떻게 안전성과 신뢰성을 보장할 수 있을까요?

바로 Ack, 재전송으로 안정성을 제공받아요.

![ack](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F8bgQE%2FbtqEwJUcK8P%2FQZJcIW5mGXIC7u7KQgP5wK%2Fimg.png)
TCP는 패킷을 받을 때마다 Ack라는 별도의 패킷을 만들어서 보내요.

여기서 Ack 라는 것은 Acknowledge의 약자로, "잘 받았음" 이라는 뜻으로 사용해요.

송신자가 패킷을 보내면, 수신자는

"n번 패킷 잘 받았습니다. 이제 n+1번 패킷 주세요"

라고 Ack를 보내면서 데이터가 잘 오가고 있음을 체크하는 것입니다.

재전송 이라는 것은, Ack가 오지 않았을 때 송신자가 패킷을 다시 보내버리는 작업이에요.

Ack가 오지 않는 경우는 다음 두 가지 경우예요.

수신자가 패킷을 받지 못해 정말 Ack를 보내지 못한 것
수신자는 패킷을 잘 받아서 Ack를 보냈으나, Ack가 중간에 유실되어 버린 것
둘 중에 어떤 경우 때문에 Ack가 안온진 모르지만, 송신자는 일정 시간 동안 Ack가 오지 않으면 패킷을 재전송 합니다.

비효율적일진 몰라도, 데이터를 못받거나 하는 일은 절대 없으니 확실히 안정적이겠죠? :)

가상 회선 방식 을 제공한다는 것은,

![가상 회선 방식](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbf8fxK%2FbtqEvw8Woxv%2F5G2jaGLNKNXcmfBCOOY1I1%2Fimg.png)

이런식으로 패킷 1,2,3이 사이좋게 정해진 길(파란색 선)으로만 가죠?

이 길이 가상 회선(논리적 경로)가 되는 것입니다.

TCP에선 이 가상 회선을 배정해주기 때문에, 패킷들은 이 회선을 따라 움직입니다.

따라서 패킷의 순서가 뒤바뀔일 없이 순차적으로 도착합니다 :)

또한, 데이터 흐름 제어 나 혼잡 제어 같은 기능도 가능해요.

흐름제어 는, 데이터를 송수신 하는 곳과 수신하는 곳의 데이터 처리 속도를 조절하여,

수신자의 버퍼 오버플로우를 방지합니다. (송신자가 미친듯이 데이터를 쏴버리면 수신자가 문제가 생길 수 있으니 그것을 조절해줌)

혼잡 제어 는, 네트워크 내의 패킷 수가 넘치지 않게 방지하는 것입니다.

패킷의 수가 너무 많아지면 패킷을 조금만 전송하여 네트워크 혼잡을 막는 것입니다.

뭔가 기능이 많아보이죠?

기능이 많으면 물론 좋지만, 그만큼 CPU의 부담도 커진다는 얘기예요.

때문에, 속도가 느려지는 것입니다.

저런 작업들을 해주는 것이 속도 면에서 영향을 끼치니까요 :D

그럼 UDP는 저런 작업을 안해주니까 속도가 빠른 거겠죠?!?

따라서 TCP는 연속적으로 데이터를 주고받을 때 보단,

신뢰성 있는 연결을 중시할 때 사용합니다.

연속적으로 데이터를 주고받는 것의 예
영상같은 실시간 Streaming
영상 스트리밍 같은 경우 1초에만 해도 엄청나게 많은 프레임 패킷을 연속적으로 받아요.

그럴 때 만약 프레임 패킷 하나가 손실 되었다고 해서

다시 손실된 데이터를 요청하고 한다면... 실시간이라는 것에 조금 치명적일 수 있겠죠.(요청할 동안 버벅일테니..)

사실 프레임 패킷하나가 손실되었다 해서 재요청하는 것보단, 그냥 무시하고 계속 재생되는 게 더 맞을테니까요.

2. UDP(User Datagram Protocol)
   Datagram Socket
   UDP에서 데이터를 Datagram 단위로 처리합니다.

Datagram이란 독립적인 단계를 지니는 패킷을 뜻합니다.
UDP도 데이터그램을 받기 위해선 TCP와 같이 IP를 사용합니다.

다만, 소켓 통신을 구현할 때 소켓을 만들어 서로 연결을 맺는 구조가 아닌

소켓을 만들어 UDP 서버의 IP, Port로 데이터를 보내버리는 개념입니다.

그렇기 때문에 UDP 서버 하나에 여러 Client들이 붙어서 데이터를 받을 수 있습니다.

서버또한 클라이언트의 IP, Port로 데이터를 데이터그램 단위로 보내게 됩니다.

전화와 편지 비유
보통 TCP는 전화에, UDP는 편지에 많이 비교합니다.

TCP는 상대방의 번호(IP, Port)로 전화를 걸고 연결이 되면, 서로 의사소통을 주고 받을 수 있죠.

"너 내가 방금 한 말 들었어?"

"아니 못들었어! 다시 해줘!"

이런 식으로 :D

그러나 UDP는 편지이기 때문에, 상대방의 집주소(IP, Port)만 알면 그냥 편지에 데이터 쓰고 우체통에 넣어버리는 것입니다.

수신자는 자신의 편지통에 편지가 왔는지 직접 확인할 때까진 편지가 온지 모를테고,

또 송신자 역시 편지를 보내긴 했지만 수신자가 실제 그 편지를 받았는지, 읽었는지, 중간에 날라갔는지엔 관심 없습니다.

또한 UDP는 TCP와 달리 비연결형 소켓이기 때문에, 연결을 위해 할당되는 논리적 경로가 없습니다.

![UDP](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcYbhIF%2FbtqEvZwi4xV%2FQx4DEqZ7oIXOJxJhQ7E0x0%2Fimg.png)

CP와 달리 파란 선(가상 회선)이 없죠?

그렇기 때문에 UDP는 데이터들이 서로 다른 경로로 전송됩니다.

1,2,3번 패킷이 서로 독립접인 관계고, 실제로 보낸 순서대로 도착하지 않을 수도 있습니다.

이런 패킷들을 데이터그램이라 하고, 이러한 방식을 UDP라 합니다.

UDP 소켓의 특징은 다음과 같습니다.

비연결형 서비스로 데이터그램 방식을 제공한다.
정보를 주고받을 때, Handshake와 같은 신호 절차를 거치지 않는다.
UDP Hedaer의 CheckSum을 통해 최소한의 에러만 검출한다.
일대일 통신(unicast), 일대다 통신(broadcast), 다대다 통신(multicast)
데이터가 제대로 도착할 수도, 중간에 유실될 수도, 순서가 바뀌어 도착할 수도 있다.
TCP보다 속도가 빠르다.
신뢰성이 낮다.
UDP의 경우 연결을 맺고 끊는 과정이 존재하지 않고, Ack를 보내지도 않으며,

패킷에 순서를 부여하여 추적 관리하거나, 혼잡, 흐름 제어도 하지 않기 때문에

속도가 빠르고 네트워크 부하도 적습니다.

그러나, 중간에 패킷 손실과 같은 것을 체크할 수 없기 때문에,

데이터 전송 면에서 신뢰성이 떨어집니다.

따라서, TCP와 반대로

신뢰성보다 연속성이 중요한 서비스에서 사용 됩니다. (영상 실시간 Streaming 등)

그래서 iOS에서는 socket 연결을 설정하기 위해서 Stream 을 사용하게 됩니다.

Stream 은 말그대로 Stream을 나타내는 추상클래스이고 자식클래스로 InputStream 과 OutputStream 을 갖고 있습니다.

InputStream 을 활용하여 입력되는 데이터를 읽어올 수 있고

OutputStream 을 통해 데이터를 써서 결과물을 서버

로 보낼 수 가 있습니다.

3. 사용방법
   Socket 생성 및 연결
   소켓을 연결하는 작업을 3가지 정도로 시도해 봤습니다.

1. Stream을 활용한 소켓 연결
   getStreamsTo(\_:port:inputStream:outputStream:)
   해당 메서드를 활용하여 NSInputStream객체와 NSOutputStream객체를 생성한 뒤 소켓 연결을 위해 사용할 수 있습니다. 물론 이 과정에서 호스트와 포트에 대한 정보가 필요합니다.

다음과 같이 소켓 연결이 이루어질 수 있습니다..

final class Network: NSObject {
private var inputStream: InputStream?
private var outputStream: OutputStream?

func connect(hostName: String, portNumber: Int) {
Stream.getStreamsToHost(withName: hostName, port: portNumber, inputStream: &inputStream, outputStream: &outputStream)

    if inputStream != nil && outputStream != nil {

      // Set Delegate
      inputStream!.delegate = self
      outputStream!.delegate = self

      // Schedule Connection
      inputStream!.schedule(in: .main, forMode: .default)
      outputStream!.schedule(in: .main, forMode: .default)

      // open
      inputStream!.open()
      outputStream!.open()
    }

}
}

- Stream의 타입 메서드를 활용하여 Host로 연결하는 작업
  이 과정에서 호스트이름, 포트 그리고 inputStream과 outputStream의 주소값에 포인터를 넣어주는 작업이 필요합니다.

Stream.getStreamsToHost(withName: hostName, port: portNumber, inputStream: &inputStream, outputStream: &outputStream)

- 각 stream객체가 nil이 아니라는 검증과정을 if문을 통해 진행
- inputStream, outputStream의 대리자 설정을 하는 작업을 진행
  이 경우 Network가 stream의 대리자가 되겠네요. 이렇게 위임 작업을 하는 이유는 StreamDelgate 를 활용하여 주어진 Stream이 받는 이벤트에 대한 처리를 할 수 있게 됩니다. 이런식으로요

extension Network: StreamDelegate {
func stream(\_ aStream: Stream, handle eventCode: Stream.Event) {
switch eventCode {
case .hasBytesAvailable:
print("new message received")
case .endEncountered:
// close socket here
print("end Message received")
case .errorOccurred:
print("error occurred")
case .hasSpaceAvailable:
print("has space available")
default:
print("some other event...")
}
}
이렇게 delegate에게 Stream의 이벤트처리를 하기 위해서는 delegate작업이 필요하고 delegate가 메세지를 받기 위해서는 Stream이 runloop에 스케줄되어 있어야 합니다. 이 경우 기본상태로 mainRunLoop로 inputStream과 outputStream을 스케줄하게되죠.

inputStream!.schedule(in: .main, forMode: .default)
outputStream!.schedule(in: .main, forMode: .default)
스케줄 준비가 되면 stream을 open() 하여 소켓을 생성하고 읽고 쓰는 작업이 가능하게 설정을 하게 됩니다.

open하게 되면 클라이언트가 직접적으로 사용이 가능해집니다. 단 이경우에는 runloop로 스케줄을 한 상태이니 Delegate인 Network가 쓰고 읽는 작업을 관리할 수 있게 됩니다.

++애플이 제공하는 아카이브 문서에 의하면

"The NSStream class does not support connecting to a remote host on iOS" 라고 하더라구요.

즉 Stream 클래스를 사용하게 되면 원격 호스트에 접근할 수 없으니 원격 서버로 접근하는 것도 지원하지 않는다

고 하는데...주변 개발자분들 얘기 들어보니 Stream을 활용하여 원격호스트 접근에 성공하신 분도 계셔서 이 부분은 조금 더 확인이 필요한 것 같습니다.

물론 아카이브된 문서는 애플이 내용을 보장하지 않는다는 의미이기 때문에 해당 내용이 outdated된걸 수도 있구요. 무튼 아카이브 문서에 따르면 **CFStream**이 원격호스트 연결을 지원하기 때문에 **CFStream**을 사용하라고 적혀있더라구요!!

2. CFStream을 활용한 소켓 연결
   func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!,
   _ host: CFString!,
   _ port: UInt32,
   _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!,
   \_ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
   메서드를 활용하여 inputStream과 outputStream 객체를 생성하여 소켓을 연결할 수 있습니다.

CFStream또한 Stream의 구현방식과 유사합니다

class Network: NSObject {
var inputStream: InputStream?
var outputStream: OutputStream?
weak var delegate: ChatRoomDelegate? //(delegate 이름)
let maxReadLength = 4096

func connect(hostName: String, portNumber: Int) {
var readStream: Unmanaged<CFReadStream>?
var writeStream: Unmanaged<CFWriteStream>?

    CFStreamCreatePairWithSocketToHost(kCFAllocatorDefault, hostName as CFString, portNumber, &readStream, &writeStream)
    guard let readStreamRetainedValue = readStream?.takeRetainedValue(),
          let writeStreamRetainedValue = writeStream?.takeRetainedValue() else {
      return
    }

    inputStream = readStreamRetainedValue
    outputStream = writeStreamRetainedValue

    inputStream?.delegate = self

    inputStream?.schedule(in: .current, forMode: .common)
    outputStream?.schedule(in: .current, forMode: .common)

    inputStream?.open()
    outputStream?.open()

}
}
CFStreamCreatePairWithSocketToHost(kCFAllocatorDefault, hostName as CFString, portNumber, &readStream, &writeStream)
inputStream과 outputStream에 메모리를 할당하기 위한 할당기(allocator)가 필요하고 이 경우 그냥 디폴트 allocator인 kcFAllocatorDefault를 전달인자로 넣어주었습니다.

hostName 또한 CoreFoundation 클래스에서 사용하기 위해 CFString으로 타입캐스팅을 해 주었구요.

풀이
var readStream: Unmanaged<CFReadStream>?
var writeStream: Unmanaged<CFWriteStream>?
Core Foundation 클래스를 활용하여 inputStream과 outputStream을 구현하기위해서 readStream과 writeStream을 선언한 뒤

각 Stream의 주소값에 포인터를 넣어주는 작업을 위해 &readStream 그리고 &writeStream 을 CFStreamCreatePairWithSocketToHost 의 전달인자로 넣어주었습니다.

CFStreamCreatePairWithSocketToHost(kCFAllocatorDefault, hostName as CFString, portNumber, &readStream, &writeStream)
guard let readStreamRetainedValue = readStream?.takeRetainedValue(),
let writeStreamRetainedValue = writeStream?.takeRetainedValue() else {
return
}
이제 객체로 사용되기 적합해진 readStream과 writeStream의 takeRetainedValue() 메서드를 통해 readStream과 writeStream의 주소로부터 값을 가져온 뒤

inputStream = readStreamRetainedValue
outputStream = writeStreamRetainedValue
사용할 inputStream과 outputStream에 할당해 주는 작업을 해주었습니다. CFStream은 CocoaFoundation의 Stream과 toll-free briedged 관계..즉 교환해서 사용가능한 관계이기 때문에 할당 또한 가능합니다.

3. URLSessionStreamTask를 활용한 소켓 연결
   마지막으로 URLSessionStreamTask 또한 소켓연결로서 활용될 수 있지 않을까 생각 해보았습니다. 위 두 방법 같은 경우 소켓 생성과정에서 활용되는 메서드들이 deprecated 되어있기 때문에 추후에 사용이 제한될 수 있기 때문에 시도해 볼만한 가치가 있다 생각한거죠!!

func streamTask(withHostName hostname: String,
port: Int) -> URLSessionStreamTask
final class Network: NSObject {

// weak var delegate: MessageTransferable?
var urlSession: URLSessionProtocol
var streamTask: URLSessionStreamTaskProtocol?
private var inputStream: InputStream?
private var outputStream: OutputStream?

    init(urlSession: URLSessionProtocol = URLSession.shared) {
        self.urlSession = urlSession
    }

     func connect(hostName: String, portNumber: Int) {

        let configuration = URLSessionConfiguration.default
        configuration.requestCachePolicy = .reloadIgnoringLocalCacheData
        urlSession = URLSession(configuration: configuration, delegate: self, delegateQueue: nil)

        self.streamTask = urlSession.streamTask(withHostName: hostName, port: portNumber)
        streamTask?.captureStreams()
        streamTask?.resume()

    }

}
URLSession 의 streamTask 를 통해 URLSessionStreamTask 객체를 생성할 수 있습니다.

URLSessionStreamTask객체는 비동기적으로 읽고 쓰는 작업을 실행할 수 있고 모든 작업은 queue에 저장되어있다가 serial하게 실행되게 됩니다.

StreamTask를 생성한 뒤 inputStream과 outputStream을 생성하기 위해서는 captureStreams() 메서드가 필요합니다.

streamTask?.captureStreams()
해당 메서드가 호출이 되면 URLSessionStreamDelegate의

func urlSession(\_ session: URLSession, streamTask: URLSessionStreamTask, didBecome inputStream: InputStream, outputStream: OutputStream)
메서드가 호출이 되면서 inputStream과 outputStream의 세팅작업이 가능해 집니다.

func urlSession(\_ session: URLSession, streamTask: URLSessionStreamTask, didBecome inputStream: InputStream, outputStream: OutputStream) {
self.inputStream = inputStream
self.outputStream = outputStream

        self.inputStream?.delegate = self

        self.inputStream?.schedule(in: .current, forMode: .common)
        self.outputStream?.schedule(in: .current, forMode: .common)

        self.inputStream?.open()
        self.outputStream?.open()

    }

그렇게 되면 해당 메서드 내부에서 inputStream과 outputStream의 생성이 가능해지고 위임작업, 스케줄링과 open() 작업이 가능해 져서 소켓이 정상적으로 사용될 수 있게 생성이 되는 것이라 생각했지만...

Trouble: streamTask야 왜 읽지를 못하니...
URLSessionStreamTask의 문제점
왠걸...streamTask의 .capture() 메서드를 통해 inputStream과 outputStream 새팅을 해주니까 서버로 write하는데 까지는 문제가 없었지만...서버로 부터 데이터를 읽어오는데 핵심 역할을 하는 StreamDelegate 가 정상적으로 data를 받아서 처리를하지 못하는 문제를 직면했습니다.

self.inputStream?.delegate = self 를 통해 Network가 stream의 대리자가 되도록 설정을 하면 받아온 데이터가 StreamDelegate의 stream(\_:handle) 메서드를 통해 받아올 수 있는 데이터를 감지할 수 있습니다.

이 delegate의 메서드 덕분에 지속적인 polling이 아니라 필요할 때만 데이터를 받아올 수 있게 됩니다.

아래와 같은 방식으로 만약 가져올 수 있는 데이터가 있는 상황이다(**.hasBytesAvailable**)를 Stream의 Event에서 알려주면 그 때 데이터를 읽도록(readAvailableBytes(stream: InputStream)) 메서드를 호출하면 되는 것이지요

extension Network: StreamDelegate {
func stream(_ aStream: Stream, handle eventCode: Stream.Event) {
switch eventCode {
case .hasBytesAvailable:
guard let inputStream = aStream as? InputStream else { return }
readAvailableBytes(stream: inputStream)
NSLog("new message received")
case .endEncountered:
disconnect()
NSLog("socketIsClosed")
case .errorOccurred:
NSLog("error occurred")
case .hasSpaceAvailable:
NSLog("has space available")
default:
NSLog("some other event...")
}
}
}
그런데....URLSessionStreamTask로 inputStream과 outputStream 세팅을 하니 데이터를 작성할 수는 있지만 무슨일인지 delegate의 stream(_:handle) 메서드가 호출되지 않는 문제를 맞닥드렸습니다. 꽤 오래 고민하며 문제를 해결하려 하였으나 streamTask를 활용해서는 문제를 해결하지 못하였고..

TroubleShooting: CFStream을 사용하자!
두 번째 방법인 CFStream을 활용하여 소켓 연결을 구현하였습니다. 현재는 CFStreamCreatePairWithSocketToHost(_:_:_:_:\_:) 메서드를 사용할 수 있지만 언제 deprecated된 메서드 이기에 언제 사용이 불가능해질지 모르지만 애플이 대체할 수 있는 메서드를 들고 오겠지요😁

3가지 소켓 연결 방식에 대한 결론
Stream → getStreamsTo(_:port:inputStream:outputStream:) 통한 소켓 연결
문제점: 아카이브 문서에 따르면 Stream Class는 원격 호스트에 접근하는 것을 지원하지 않는다고 합니다. 물론 아카이브 문서가 오래된 문서이고 애플이 더 이상 보증하지 않는다는 점 그리고 주변 분들 중 Stream을 사용하여 원격 호스트 접근에 성공하신 분들이 계시기 때문에 사용하면 안된다 라고 할 수는 없지만 그래도...베스트 방법은 아닌 것 같다는 생각이 들었습니다. getStreamsTo 타입 메서드가 deprecated된 이상 미래지향적이 아닌 방법인 건 자명한듯 싶구요.
CFStream → CFStreamCreatePairWithSocketToHost(_:_:_:_:_:) 통한 소켓 연결
아카이브 문서 에서는 CFStream을 통해서 원격 호스트에 접근할 수 있다고 하니 조금 더 믿음직스러운 접근방법이 아닌가 싶습니다. 다만 연결을 위해 필요한 CFStreamCreatePairWithSocketToHost 메서드가 deprecated 된게 흠이긴 하지만요.
URLSessionStreamTask → streamTask(withHostName:port:) 통한 소켓 연결
read 와 write 를 좀 더 high-level에서 사용하기도 하고 위 메서드들 처럼 deprecated된 메서드를 사용하지 않아도 되니 처음에는 더 나은 접근이지 않나 생각을 했지만....제일 중요한 Stream 이벤트를 감지하고 처리해주는 작업이 되지 않으니 반쪽짜리 기능이어서 사용하기 적절하지 않다고 생각이 되었습니다.
데이터를 어떻게 읽지?
소켓 통신을 위에서 세팅을 해 보았는데요. 이제 데이터를 읽어야겠죠?

데이터는 다음과 같은 메서드를 통해 읽어볼 수 있습니다.

func readAvailableBytes(stream: InputStream) {
let availableBytes = UnsafeMutablePointer<UInt8>.allocate(capacity: ConnectionConfiguration.maximumReadLength)

        while stream.hasBytesAvailable {
            guard let numberOfBytesRead = inputStream?.read(availableBytes, maxLength: ConnectionConfiguration.maximumReadLength) else { return }

            if numberOfBytesRead < 0,
               let error = stream.streamError {
                NSLog(error.localizedDescription)
                break
            }
            try? delegate?.convertDataToTexts(buffer: availableBytes, length: numberOfBytesRead)
        }
    }

let availableBytes = UnsafeMutablePointer<UInt8>.allocate(capacity: ConnectionConfiguration.maximumReadLength)
먼저 웹소켓에서 사용되는 데이터는 UTF8로 인코딩 되어있으니 UnsafeMutablePointer 를 활용하여 UInt8 타입의 초기화 되지 않는 메모리를 할당합니다.

guard let numberOfBytesRead = inputStream?.read(availableBytes, maxLength: ConnectionConfiguration.maximumReadLength) else { return }
그리고 InputStream이 데이터를 받아 올 수 있는 상황을 조건일 때 inputStream의 read메서드를 통해 bytes들을 buffer에 저장합니다. 해당 메서드를 통해 반환되는 값을 통해 bytes를 제대로 읽었는지 확인할 수 있고 필요에 따라 화면에 보여지도록 사용할 수도 있습니다.

String(bytesNoCopy: availableBytes, length: length, encoding: .utf8, freeWhenDone: true)
예를들면 이와 같은 String의 이니셜라이저를 통해 읽어온 데이터를 String 객체로 초기화 하여 화면에 문자로서 보여지도록 활용할 수 있습니다.

이렇게 구현한 readAvailableBytes(stream:) 메서드를 StreamDelegate의 이벤트처리에 맞게 실행을 시켜주면 데이터를 읽어올 준비가 끝납니다.

extension Network: StreamDelegate {
func stream(\_ aStream: Stream, handle eventCode: Stream.Event) {
switch eventCode {
case .hasBytesAvailable:
guard let inputStream = aStream as? InputStream else { return }
// 데이터를 읽어오자!!!
readAvailableBytes(stream: inputStream)
NSLog("new message received")
case .endEncountered:
disconnect()
NSLog("socketIsClosed")
case .errorOccurred:
NSLog("error occurred")
case .hasSpaceAvailable:
NSLog("has space available")
default:
NSLog("some other event...")
}
}
}
데이터를 어떻게 전달하지?
사용자가 입력한 문자열을 Data타입으로 변환한 뒤 다음과 같은 방법으로 수신자에게 데이터의 컨텐츠를 OutputStream을 활용하여 전달할 수 있습니다.

func writeWithUnsafeBytes(using data: Data) {
data.withUnsafeBytes { unsafeBufferPointer in
guard let buffer = unsafeBufferPointer.baseAddress?.assumingMemoryBound(to: UInt8.self) else {
NSLog("error while writing chat")
return
}
outputStream?.write(buffer, maxLength: data.count)
}
}
data.withUnsafeBytes { unsafeBufferPointer in
guard let buffer = unsafeBufferPointer.baseAddress?.assumingMemoryBound(to: UInt8.self) else {
NSLog("error while writing chat")
return
}
OutputStream으로 write하기 위해서는 dataBuffer로 접근을 해야 합니다. withUnsafeBytes 라는 메서드를 통해 주어진 data의 buffer로 접근을 할 수 있습니다.

outputStream?.write(buffer, maxLength: data.count)
bufferpointer를 통해 buffer에 접근을 할 수 있고. 접근한 버퍼와 데이터의 갯수를 write의 전달인자에 할당을 하게되면 outputStream을 활용하여 데이터를 수신자에게 전달할 수 있게 됩니다😊

4. URLSessionWebSocketTask
   WWDC2019의 업데이트로 iOS13에서 WebSocket을 위해 설계한 URLSessionWebSocketTask를 도입했습니다.

URL Session에 WebSocket을 위한 새로운 메소드가 생겼습니다.

@available(iOS 13.0, \*)
open func webSocketTask(with url: URL) -> URLSessionWebSocketTask

@available(iOS 13.0, \*)
open func webSocketTask(with url: URL, protocols: [String]) -> URLSessionWebSocketTask

@available(iOS 13.0, \*)
open func webSocketTask(with request: URLRequest) -> URLSessionWebSocketTask
URLSessionWebSocketTask는 URLSessionTask를 확장하므로

일반 URLSessionTask에 사용하는 것과 동일한 기본 API 세트를 갖게 됩니다. 하지만 얼핏 보기에는 그럴듯해 보이지만 실제로는 WebSocket을 통한 양방향 실시간 통신 (2-way real-time communication via WebSocket) 은 일반적인 HTTP request 작업 흐름과 다릅니다. 특별히 웹소켓이 맞춰 디자인된 API를 사용하는게 가장 좋겠지만 이 방법을 사용해보면

1. WebSocket 연결을 생성
   테스트 목적으로 내 컴퓨터에서 실행되는 WebSocket 에코 서버를 사용할 것입니다. 이 서버는 수신한 모든 메시지를 다시 보냅니다.

let urlSession = URLSession(configuration: .default)
let webSocketTask = urlSession.webSocketTask(with: "ws://0.0.0.0:8080/echo")
연결을 열려면 webSocketTask를 다시 시작해야 합니다.

webSocketTask.resume()
정리

우리 자신의 URLSession객체를 만들고 현재 클래스 를 프로토콜 URLSession을 준수 하는 대리자로 설정합니다. URLSessionWebSocketDelegate이 대리자를 설정하는 것은 선택 사항이지만 소켓이 열리거나 닫힐 때 콜백을 가져오는 데 사용할 수 있으므로 분석을 기록하거나 디버그 정보를 분석할 수 있습니다.

func openWebSocket() {
let urlString = "wss://rtf.beta.getbux.com/subscriptions/me"
if let url = URL(string: urlString) {
var request = URLRequest(url: url)
let session = URLSession(configuration: .default, delegate: self, delegateQueue: nil)
let webSocket = session.webSocketTask(with: request)
webSocket?.resume()
}
}
**SocketNetworkService현재 클래스 에 대해 이 대리자를 구현해 보겠습니다 .**

웹 소켓을 연 직후 메시지 수신을 시작하지만 수신하려면 인스턴스 receive에서 API를 사용하여 설정해야 합니다.URLSessionWebSocketTask

extension SocketNetworkService: URLSessionWebSocketDelegate {
func urlSession(\_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol protocol: String?) {
print("Web socket opened")
isOpened = true
}

    func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?) {
        print("Web socket closed")
        isOpened = false
    }

} 2. 메시지 보내기
이제 무언가를 보낼 시간입니다. URLSessionWebSocketTask.send 메소드는 URLSessionWebSocketTask.Message 유형의 메시지를 허용합니다 . 2가지 경우가 있는 열거형입니다.

public enum Message {
case data(Data)
case string(String)
}
여기서는 텍스트 또는 바이너리 데이터만 보낼 수 있습니다.

로우-레벨의 WebSocket 프레임이나 control 메세지 를 보낼 수 없습니다.

let message = URLSessionWebSocketTask.Message.string("Hello Socket)
webSocketTask.send(message) { error in
if let error = error {  
 print("WebSocket sending error: \\(error)")
}
}

// Method2 String
webSocket.send(URLSessionWebSocketTask.Message.string("Hello")) { [weak self] error in
if let error = error {
print("Failed with Error \\(error.localizedDescription)")
} else {
// no-op
}
}
//Data
webSocket.send(URLSessionWebSocketTask.Message.data("Hello".data(using: .utf8)!)) { [weak self] error in
if let error = error {
print("Failed with Error \\(error.localizedDescription)")
} else {
self?.closeSocket()
}
}

에코 서버는 "Hello Socket"을 수신하고 다시 보냈습니다.

3. 메시지수신
   서버에서 오는 데이터를 받기 위해서는 URLSessionWebSocketTask.receive 메소드를 사용해야 합니다.

public func receive(completionHandler: @escaping (Result<URLSessionWebSocketTask.Message, Error>) -> Void)
이 메소드는 실패나 성공을 확인할 수 있는 completion handler를 결과로 받습니다..

/\*\*

var request = URLRequest(url: URL("wss://rtf.beta.getbux.com/subscriptions/me")!)

let webSocket = URLSession.shared.webSocketTask(with: request)

webSocket.resume()

\*/

webSocketTask.receive { result in
switch result {
case .failure(let error):
print("Failed to receive message: \\(error)")
case .success(let message):
switch message {
case .string(let text):
print("Received text message: \\(text)")
case .data(let data):
print("Received binary message: \\(data)")
default:
print("Unknown type received from WebSocket")
}  
 }
}
Apple에서 제공하는 이 receive Method는 단일메시지를 수신하는 경우 자동으로 추가 메시지 수신에 있어 등록을 취소하게 되어 있습니다.

때문에 만약 다른 메시지를 수신하려면 다시 수신 을 호출해야 합니다.

func readMessage() {
webSocket.receive(completionHandler: { [weak self] result in
switch result {
case .failure(let error):
print("Failed to receive message: \\(error)")
case .success(let message):
switch message {
case .string(let text):
print("Received text message: \\(text)")
case .data(let data):
print("Received binary message: \\(data)")
default:
fatalError()
}

        }
        self.receiveMessage()
    })

}

func openWebSocket() {
let urlString = "wss://rtf.beta.getbux.com/subscriptions/me"
if let url = URL(string: urlString) {
var request = URLRequest(url: url)
let session = URLSession(configuration: .default, delegate: self, delegateQueue: nil)
let webSocket = session.webSocketTask(with: request)
webSocket?.resume()
isOpened = true
}
}

‼️receicve 메세지를 한번만 수신할 것이 아니면 메서드를 다시 사용할 수 있게 만들것

4. 연결유지 - Ping Pongs
   앱이 WebSocket을 통해 오랫동안 사용하지않으면 유휴상태로 연결을 닫습니다. 무기한 열어두어야한다면 주기적으로 ping을 보내서 활성상태를 유지할 수 있습니다. . 서버에 의해 연결이 끊어지지 않도록 주기적으로(약 10초마다) 전송해야 합니다. 이를 위해 webSocketTask.sendPing을 사용해야 합니다.

let timer = Timer.scheduledTimer(withTimeInterval: 60.0, repeats: true) { [weak self] timer in
self?.webSocket?.sendPing(pongReceiveHandler: { error in
if let error = error {
print("Failed with Error \\(error.localizedDescription)")
} else {
// no-op
}
})
}
timer.fire()
이 방법은 매우기본적인 방법인데 기본 핑 메시지를 보내고 결과를 알립니다. 이 API는 ping message payload 사용자 지정을 허용하지 않습니다. 사용자 정의 payload가 있는 Ping 메시지를 사용하여 서버에 추가 정보(예: 통계)를 전달할 수 있습니다.

5. 연결 종료
   WebSocket 연결이 더 이상 필요하지 않은 경우에도 적절하게 닫아야 합니다. URLSessionWebSocketTask에는 별도의 WebSocket 전용 취소 메서드가 있습니다.

func closeSocket() {
webSocket.cancel(with: .goingAway, reason: nil)
webSocket = nil
isOpened = false
}
닫기 코드와 선택적 이유 페이로드를 허용합니다. 닫기 코드는 이 연결이 끊어지는 이유를 서버에 알리는 데 사용됩니다. 예를 들어 웹 소켓 또는 응용 프로그램 프로토콜과 관련된 다른 오류를 나타낼 수 있습니다.

연결상태 변화 확인
분명히, 우리는 WebSocket 연결이 언제 연결되거나 연결 해제되었는지와 그 이유를 알아야 합니다.

그렇게 하려면 URLSessionWebSocketDelegate 를 사용해야 합니다.

@available(iOS 13.0, \*)
public protocol URLSessionWebSocketDelegate : URLSessionTaskDelegate {

    optional func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didOpenWithProtocol protocol: String?)

    optional func urlSession(_ session: URLSession, webSocketTask: URLSessionWebSocketTask, didCloseWith closeCode: URLSessionWebSocketTask.CloseCode, reason: Data?)

}

API는 매우 간단합니다. 연결이 열렸거나 닫혔을 때 닫기 코드와 서버의 이유를 알려줍니다.

이를 위해 대리자를 URLSession 생성자에 전달해야 합니다.

urlSession = URLSession(configuration: sessionConfiguration, delegate: delegate, delegateQueue: OperationQueue())

다시 말하지만, Apple은 기존 URLSession 아키텍처를 따르려고 합니다.

여러 웹 소켓 연결에 대해 동일한 대리자를 공유해야 하는 이유가 이상합니다. 물론 각 연결에 대해 개별 URLSession을 생성할 수는 있습니다.

사용하는 데에 있어.
iOS 13에서만 사용할 수 있으며 솔직히 말해서 URLSessionWebSocketTask는 사용 가능한 최고의 WebSocket 라이브러리가 아닙니다. 기본 WebSocket 기능이 필요하고 이전 iOS 버전을 지원할 필요가 없는 경우 사용할 수 있습니다. 다른 경우에는 Apple의 SwiftNIO 또는 많은 오픈 소스 프레임워크( 예: Starscream ) 중 하나 와 같이 더 성숙하고 적절하게 설계된 것을 사용하는 것이 좋습니다 .

관련 샘플 프로젝트
URLSessionWebSocketTask 주위에 래퍼 클래스가 있는 샘플 프로젝트를 만들었습니다. 상용구 코드의 일부를 제거하고 일반적인 WebSocket 라이브러리와 유사한 API를 제공합니다. 이 프로젝트에는 테스트에 사용할 수 있는 SwiftNIO 기반 에코 서버가 있습니다. https://github.com/appspector/URLSessionWebSocketTask 리포지토리에서 찾을 수 있습니다.

프레임워크
starscream
[iOS - swift] Starscream을 이용한 WebSockets (웹 소켓) 사용 방법

https://ios-development.tistory.com/834
