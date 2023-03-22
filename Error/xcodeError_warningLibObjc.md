# Xcode - warning: libobjc.A.dylib is being read from process memory...

최근에 아래와 같은 메시지가 콘솔 창에 뜨면서 빌드가 잘되지 않는 문제를 겪었다.
Xcode로 빌드된 다음 한참뒤에 앱이 시작된다. 

```
warning: libobjc.A.dylib is being read from process memory. This indicates that LLDB could not find the on-disk shared cache for this device. This will likely reduce debugging performance.
```

이 warning 메시지는 LLDB 디버깅 중에 발생할 수 있는 메시지 중 하나이다. 이 메시지는 LLDB가 iOS 디바이스의 on-disk shared cache를 찾지 못했음을 나타내며, 이로 인해 디버깅 성능이 저하될 수 있다는 것을 알려준다.

이러한 경고 메시지는 일반적으로 Xcode가 iOS 디바이스의 캐시 파일을 로드할 수 없을 때 발생한다. 이 문제는 다양한 이유로 발생할 수 있지만, 가장 일반적인 원인 중 하나는 iOS 디바이스의 용량이 부족하여 캐시 파일을 저장할 수 없는 경우다.

이러한 경우, iOS 디바이스를 재부팅하고 다시 연결해보거나, Xcode를 업데이트하거나, iOS 디바이스의 용량을 충분히 확보한 후 다시 시도해보는 것이 좋다. 또한, Xcode에서 디버깅 성능을 높이기 위해 기타 최적화 작업을 수행할 수도 있다.

## 해결방법

터미널을 열고 아래와 같이 입력한다. 
```
rm -r ~/Library/Developer/Xcode/iOS\ DeviceSupport
```

## 지웠는데도 안되는 경우
디바이스 목록에 들어가보면 내 기기정보에 이런 메세지가 있는 경우의 전제이다. 
```
iPhone is busy: Making Apple Watch ready for development
```
[TIL정리 : Xcode - iPhone is busy: Making Apple Watch ready for development](123)

Xcode14와 iOS16의 환장의 조화로 이런 경우가 발생하곤 한다고 한다.
이미 위에서 DeviceSupport를 지웠다면 Xcode를 껐다 다시키고 빌드하도록 기다리자.
디바이스도 뽑았다가 다시 껴주고 대기하면 에러 메세지가 없어질 것이다. 



