# About CocoaPods Error 방지하기


 iOS Simulator에서 앱을 빌드할 때 사용되는 아키텍처를 지정할 수 있다.
 
 ```swift
 //  팟파일 세팅완료
 
 
 post_install do |pi|
  pi.pods_project.targets.each do |t|
    t.build_configurations.each do |bc|
    bc.build_settings['ARCHS[sdk=iphonesimulator*]'] =  `uname -m`
    end
  end
end

 ```

CocoaPods에서 pod install 명령을 실행한 후에, Xcode 프로젝트를 빌드할 때 iOS Simulator 아키텍처를 지정하기 위한 코드다.

iOS 앱을 빌드하려면, 해당 앱을 실행할 기기의 아키텍처를 지정해야 한다. iOS 기기에는 ARM 아키텍처와 x86 아키텍처가 있다. 실제 iOS 기기에서 실행하는 경우에는 ARM 아키텍처를 지정해야 하지만, iOS Simulator에서 실행하는 경우에는 x86 아키텍처를 지정해야 한다.

위의 코드는 post_install 훅을 사용하여 CocoaPods가 설치한 모든 라이브러리 타겟의 빌드 설정을 변경한다. build_settings 딕셔너리의 ARCHS[sdk=iphonesimulator*] 키를 설정하면, iOS Simulator에서 빌드할 때 사용되는 아키텍처를 지정할 수 있다. 이 코드에서는 uname -m 명령어를 사용하여 현재 컴퓨터의 아키텍처를 가져오고, 이 값을 ARCHS[sdk=iphonesimulator*] 키에 할당하여 iOS Simulator에서 실행할 때 사용할 아키텍처를 지정한다.
