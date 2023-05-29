# Xcode Error - Launching _AppName_ is taking longer than expected

앱을 실행하는 데 매우 오래 걸리며(2분 이상) 스플래시 화면에 2~3분 더 표시된다.

Xcode에서는 아래 경고창이 표시된다. 이때 Continue를 누르거나 그냥 놔두어도 한참뒤에 작동한다.

![스크린샷 2022-11-17 오후 4 22 08](https://user-images.githubusercontent.com/76529148/202384524-140b7fb5-59d5-4e67-a95c-28b2940f3759.png)

### 해결방법

참고: [https://stackoverflow.com/questions/69366799/xcode-13-ios15-is-taking-longer-than-expected-to-launch-it-shows-a-lldb-related](https://stackoverflow.com/questions/69366799/xcode-13-ios15-is-taking-longer-than-expected-to-launch-it-shows-a-lldb-related)

1. 장치 연결 해제
2. Xcode 종료
3. 터미널 창을 열고 위의 명령을 실행합니다.
4. Xcode 열기
5. 장치를 연결하고 앱을 실행하십시오.

```
rm -r ~/Library/Developer/Xcode/iOS\ DeviceSupport
```

앱을 처음 실행하면 컴퓨터가 삭제한 정보를 다시 가져오므로 시간이 다소 걸리지만 이후 앱 실행은 훨씬 더 빠르게 작동한다.

![스크린샷 2022-11-17 오후 4 27 55](https://user-images.githubusercontent.com/76529148/202384539-8a62d1ac-d18e-40f7-9100-20844c4609d2.png)
