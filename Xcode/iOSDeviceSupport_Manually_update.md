# iOS DeviceSupport - 테스트 디바이스 iOS 수동 업데이트

개인 Mac에서는 마음껏 버전업해도 상관이 없지만

업무환경에 따라 부득이하게 Xcode를 버전업하지 못하는 경우가 있다.

이 때, 현재 Xcode 버전에서 테스트장비의 iOS를 지원하지 않는 경우가 있다.

## 일반적인 상황

앱스토어에서 Xcode 정식버전 업데이트를 하면 된다.

## 타겟 iOS가 베타버전인 상황

이럴경우에는 Xcode도 베타버전이 있을 수 있다.

아래 링크에서 베타 버전을 다운로드받을 수 있다. → 개발자 계정 필요 (무료도 상관없음)

[https://developer.apple.com/download/](https://developer.apple.com/download/)

혹은 수동업데이트를 할 수도 있다.

## Xcode가 구버전인 상황

업무환경에 따라 이전 버전의 Xcode를  사용해야만하는 경우는 수동 업데이트를 해줘야한다.

## 수동업데이트

### Step 1.

Finder를 열고 좌측상단 패널 - “이동”탭에서 “폴더로 이동”을 누른다

이곳에서 아래 경로를 입력한다.

`/Users/kanghyeonjung/Library/Developer/Xcode`

Xcode폴더 안에서 iOS DeviceSupport폴더에 들어간다.

앱이 빌드가 안되면 가끔 이 폴더를 삭제하는 경우가 있다. 만약 이렇게 수동으로 시뮬레이터 버전을 설치하는 경우엔 기억하자.

### Step 2.

아래 링크에서 원하는 iOS버전 압축파일을 다운받고 버전이름이 있는 폴더 그대로 iOS DeviceSupport안에 넣는다

[https://github.com/filsv/iOSDeviceSupport](https://github.com/filsv/iOSDeviceSupport)

### Step 3.

Xcode재시작

### Step 4.

디바이스목록에서 선택

→ Xcode doesn’t support 에러가 사라진 걸 확인할 수 있다.
