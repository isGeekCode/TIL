git ignore 사용하기

보통 우리가 사용하는 프로젝트는 깃을 통해 버전관리를 할수가 있다.

git push를 하게 되면 Local에서 사용하는 프로젝트는 Remote에 저장이 되는데

이때 private하거나 궂이 remote에 안올라가도 되는 파일들이 있을 때가 있다.

공유하면 곤란한 key 값이나 각종 라이브러리에 대한 정보가 담긴 cocoapods, spm 등등이다.

이 파일들. 특히 라이브러리 관련 파일들은 새롭게 빌드하게 되면 또 새로운 파일로 인식을 하게 되는데 그럴때마다 깃에서 인식을 해버리면
매번 커밋을 하기전에 신경이 쓰이는 일이 벌어진다.

개인적으로 작업한다면 모르겠지만 여러명이서 협업을 하게 될경우 , xcode에 담겨있는 유저정보가 서로 덮어쓰기 되면서 충돌을 일으킬 가능성도 있다.

이를 위해서 하는 작업이 ignore처리이다.

가장 좋은 것은 깃 레포지토리를 생성하고

프로젝트를 깃에 올리기 전에 ignore파일 부터 생성을 하는 것이다.

만약 이미 파일들이 이미 올라가있어도 나중에 remote에 있는 특정 파일만 일괄적으로 ignore 처리하는 것이 가능하다.

물론… 그것도 귀찮으니 가장 좋은 방법은 프로젝트를 올리기 전에 작업을 해주는 것이 좋다.

# 📌 깃 푸시 순서

1. **ignore 세팅**
2. **init 프로젝트**

### 1. ignore 에 들어갈 내용 만들기

사이트: [https://gitignore.io](https://gitignore.io/)

위 사이트에서 원하는 키워드를 입력한다.

swift, xcode, cocoapods 키워드를 추천한다.

키워드를 입력하고 검색하면 입력한 키워드에 해당하는 내용이 생성된다.

이 내용을 복사한다.

생성된 내용

- ignore처리 내용

  ```bash
  # Created by https://www.gitignore.io/api/xcode,swift,cocoapods
  # Edit at https://www.gitignore.io/?templates=xcode,swift,cocoapods

  ### CocoaPods ###
  ## CocoaPods GitIgnore Template

  # CocoaPods - Only use to conserve bandwidth / Save time on Pushing
  #           - Also handy if you have a large number of dependant pods
  #           - AS PER https://guides.cocoapods.org/using/using-cocoapods.html NEVER IGNORE THE LOCK FILE
  Pods/

  ### Swift ###
  # Xcode
  #
  # gitignore contributors: remember to update Global/Xcode.gitignore, Objective-C.gitignore & Swift.gitignore

  ## Build generated
  build/
  DerivedData/

  ## Various settings
  *.pbxuser
  !default.pbxuser
  *.mode1v3
  !default.mode1v3
  *.mode2v3
  !default.mode2v3
  *.perspectivev3
  !default.perspectivev3
  xcuserdata/

  ## Other
  *.moved-aside
  *.xccheckout
  *.xcscmblueprint

  ## Obj-C/Swift specific
  *.hmap
  *.ipa
  *.dSYM.zip
  *.dSYM

  ## Playgrounds
  timeline.xctimeline
  playground.xcworkspace

  # Swift Package Manager
  # Add this line if you want to avoid checking in source code from Swift Package Manager dependencies.
  # Packages/
  # Package.pins
  # Package.resolved
  .build/
  # Add this line if you want to avoid checking in Xcode SPM integration.
  # .swiftpm/xcode

  # CocoaPods
  # We recommend against adding the Pods directory to your .gitignore. However
  # you should judge for yourself, the pros and cons are mentioned at:
  # https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control
  # Pods/
  # Add this line if you want to avoid checking in source code from the Xcode workspace
  # *.xcworkspace

  # Carthage
  # Add this line if you want to avoid checking in source code from Carthage dependencies.
  # Carthage/Checkouts

  Carthage/Build

  # Accio dependency management
  Dependencies/
  .accio/

  # fastlane
  # It is recommended to not store the screenshots in the git repo. Instead, use fastlane to re-generate the
  # screenshots whenever they are needed.
  # For more information about the recommended setup visit:
  # https://docs.fastlane.tools/best-practices/source-control/#source-control

  fastlane/report.xml
  fastlane/Preview.html
  fastlane/screenshots/**/*.png
  fastlane/test_output

  # Code Injection
  # After new code Injection tools there's a generated folder /iOSInjectionProject
  # https://github.com/johnno1962/injectionforxcode

  iOSInjectionProject/

  ### Xcode ###
  # Xcode
  # gitignore contributors: remember to update Global/Xcode.gitignore, Objective-C.gitignore & Swift.gitignore

  ## User settings

  ## compatibility with Xcode 8 and earlier (ignoring not required starting Xcode 9)

  ## compatibility with Xcode 3 and earlier (ignoring not required starting Xcode 4)

  ## Xcode Patch
  *.xcodeproj/*
  !*.xcodeproj/project.pbxproj
  !*.xcodeproj/xcshareddata/
  !*.xcworkspace/contents.xcworkspacedata
  /*.gcno

  ### Xcode Patch ###
  **/xcshareddata/WorkspaceSettings.xcsettings

  # End of https://www.gitignore.io/api/xcode,swift,cocoapods
  ```

### 2. ignore파일 생성하기

- terminal 창에 git repository 디렉토리로 간다.
- vim .gitignore 명령어를 입력한다.
- i를 눌러 insert모드로 변경한다.
- 복사해온 ignore 내용을 붙여넣기한다.
- esc를 누르고 :wq를 입력하고 엔터를 누른다.
- git commit -m “git ignore init”
- git push

이제 제외처리된 파일들은 변경되어도 추적되지않는다.
