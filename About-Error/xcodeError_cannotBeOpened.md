# Xcode - Cannot be opened because it is in a future Xcode project file format.

xcode 14.0에서 생성한 프로젝트가 xcode 13.1에서 열리지 않았다

내용은 명료하다

현재 xcode 버전과 프로젝트 xcode 버전이 **호환**이 안돼서 열지 못 한다는 내용..

## **2. 해결방법**

프로젝트파일 우클릭 → 패키지 내용보기

- project.pbxproj
- project.xcworkspace
- xcuserdata

그러면 위 세 가지 항목들이 보이는데 그 중 `project.pbxproj`를 열어준다

해당 파일에는 프로젝트 설정들이 들어가있다

### 수정할 부분

결론부터 말하자면 objectVersion만 1줄였더니 가능했다.

레퍼런스처럼 다 안해도 최상단 objectVersion만 줄여보면 될듯. 만약 깃에 머지한다면 요건 반영하지말도록하자!

- `objectVersion`
    - 이 값의 정확한 의미는 잘 모르겠다.
    - 이 값을 다운그레이드 하지 않으니 계속 프로젝트가 열리지 않아서 낮춰주었다
- `CreatedOnToolsVersion`
    - 프로젝트를 생성한 Xcode 버전을 의미한다
    - Xcode13.1에서 실행할거라 1310으로 수정했다
    - 얘도 원복했는데 정상작동한다.
- `LastUpgradeCheck`
    - 프로젝트에서 마지막으로 체크한 Xcode 버전을 의미하는 것 같다
    - 기존에 1410이었다. Xcode 14.1을 의미한다.
    - 1310은 Xcode 13.1을 의미하므로 1310으로 다운그레이드 해주었다
    - 얘는 원복해도 정상작동한다
- `compatibilityVersion`
    - 문맥상 Xcode 호환 버전인 것 같은데 13으로 잡혀있어서 다운그레이드 해주었다
    - 얘도 원복해봤는데 정상작동한다
- `IPHONEOS_DEPLOYMENT_TARGET`
    - 프로젝트 생성 시에 디폴트로 최상위 버전이 잡히는 것 같다
    - 만약 높게 잡혀있다면 낮춰주도록 하자

```jsx
objectVersion = 50;
LastUpgradeCheck = 1230;
CreatedOnToolsVersion = 12.3;
compatibilityVersion = "Xcode 13.0";
IPHONEOS_DEPLOYMENT_TARGET = 11.0;
IPHONEOS_DEPLOYMENT_TARGET = 11.0;
```

### 레퍼런스

[https://github.com/YuchanSong/sample-image-editor/commit/3bd3594d695f7ffa294547b9af8d9885d79ac549#diff-6b39ec162873d5fe9ca3c88f5e35d4f0849d45f3db6b1eb37920787bb95c9890](https://github.com/YuchanSong/sample-image-editor/commit/3bd3594d695f7ffa294547b9af8d9885d79ac549#diff-6b39ec162873d5fe9ca3c88f5e35d4f0849d45f3db6b1eb37920787bb95c9890)
