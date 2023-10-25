# [Apple Document] - UIControl.Event 살펴보기


UIControl은 UIView를 상속한다. 

즉, UIControl은 형태를 보여주는 것 외에 여러가지 이벤트 처리가 추가된 클래스이다.


<br>ㅍ

## declaration

Swift언어 기반에서는 UIControl 클래스 내부에 Event 구조체로 정의되어있고,

Objective - c 기반에서는 UIControlEvents 열거형으로 정의되어있다.

<br><br>

## Events

UIControl을 상속하는 객체는 UIButton, UITextField, UISlider, UIStepper, UISwitch, UISwitch, UIPageControl, UIDatePicker, UIRefreshControl 등이 있다.

이 객체들이 처리할 이벤트들은 아래와 같다.

```swift

// 버튼이 터치될 때 발생하는 이벤트
static var touchDown: UIControl.Event

// 버튼이 반복해서 빠르게 터치될 때 발생하는 이벤트
static var touchDownRepeat: UIControl.Event

// 버튼 내부에서 드래그할 때 발생하는 이벤트
static var touchDragInside: UIControl.Event

// 버튼 외부에서 드래그할 때 발생하는 이벤트
static var touchDragOutside: UIControl.Event

// 버튼에 드래그로 진입할 때 발생하는 이벤트
static var touchDragEnter: UIControl.Event

// 버튼에서 드래그로 벗어날 때 발생하는 이벤트
static var touchDragExit: UIControl.Event

// 버튼을 터치한 후 손을 떼었을 때 발생하는 이벤트
static var touchUpInside: UIControl.Event

// 버튼을 터치한 후 버튼 영역을 벗어났을 때 발생하는 이벤트
static var touchUpOutside: UIControl.Event

// 터치 이벤트가 취소될 때 발생하는 이벤트
static var touchCancel: UIControl.Event

// 주로 슬라이더나 스테퍼와 같은 값 변경 컨트롤에서 값이 변경될 때 발생하는 이벤트
static var valueChanged: UIControl.Event

// iOS 14 이상에서 사용되며, 컨트롤에 연결된 메뉴 액션을 트리거할 때 발생하는 이벤트
static var menuActionTriggered: UIControl.Event

// iOS 14 이상에서 사용되며, 주로 버튼을 탭했을 때 발생하는 기본 동작을 처리하는 이벤트
static var primaryActionTriggered: UIControl.Event

// 텍스트 입력 필드에서 편집이 시작될 때 발생하는 이벤트
static var editingDidBegin: UIControl.Event

// 텍스트 입력 필드의 텍스트가 변경될 때 발생하는 이벤트
static var editingChanged: UIControl.Event

// 텍스트 입력 필드의 편집이 종료될 때 발생하는 이벤트
static var editingDidEnd: UIControl.Event

// 텍스트 입력 필드에서 Return 키를 눌러 편집이 종료될 때 발생하는 이벤트
static var editingDidEndOnExit: UIControl.Event

// 모든 터치 관련 이벤트를 나타내는 옵션
static var allTouchEvents: UIControl.Event

// 모든 텍스트 입력 필드 관련 이벤트를 나타내는 옵션
static var allEditingEvents: UIControl.Event

// 애플리케이션에서 예약된 이벤트
static var applicationReserved: UIControl.Event

// 시스템에서 예약된 이벤트
static var systemReserved: UIControl.Event

// 모든 이벤트를 나타내는 옵션
static var allEvents: UIControl.Event

```

다양한 이벤트들이 있지만 주로 사용하는 이벤트는 몇가지 안된다.

## 주로 사용하는 이벤트

- .touchUpInside: 버튼을 눌렀다가 손을 뗄 때 발생하는 이벤트로, 주로 버튼을 클릭할 때 사용된다. 주로 버튼에 연결된 액션 메서드를 호출하여 사용자의 명령을 실행하는 데 사용된다.

- .valueChanged: 주로 UISlider나 UIStepper와 같은 값 변경 컨트롤에서 사용된다. 사용자가 슬라이더를 드래그하거나 스테퍼를 조작할 때 값이 변경될 때 이 이벤트가 발생하고, 값을 업데이트하는 데 사용된다.

- .editingDidBegin: 텍스트 입력 필드(예: UITextField)에서 사용자가 입력을 시작할 때 호출된다. 주로 입력 필드와 관련된 작업을 수행하는 데 사용된다.

- .editingChanged: 입력 필드의 텍스트가 변경될 때 호출된다. 주로 입력 필드의 텍스트 변경에 반응하여 동적으로 UI를 업데이트하는 데 사용된다.

- .editingDidEnd: 입력 필드에서 편집이 종료될 때 호출된다. 주로 입력 필드의 편집이 종료된 후 처리해야 하는 작업을 수행하는 데 사용된다.

- .touchDragInside 및 .touchDragOutside: 버튼 또는 다른 UIControl 요소를 터치한 상태에서 드래그하는 이벤트로, 드래그 관련 동작을 구현할 때 사용된다.


## Comments
생각보다 touch와 관련되어서 비슷하다고 느껴지는 동작이 생각보다 많았다. 

textField에 관련된 이벤트는 대부분 사용하지만, 나머지 이벤트들은 일단 한번씩 경험해 보는 것이 중요하다고 생각한다. 




## 테스트 코드
```swift
    /// 버튼을 터치하고 손을 떼는 순간 호출
    @IBAction func touchUpInside(_ sender: Any) {
        print("touchUpInside")
    }
    
    /// 버튼을 터치하고 손을 떼지 않고 버튼영역을 벗어나는 순간 호출
    @IBAction func touchUpOutside(_ sender: Any) {
        print("touchUpOutside")
    }

    /// 버튼을 터치할 때 발생, 사용자가 버튼을 누를때 호출되고, 아직 손을 떼지 않은 경우에도 계속해서 발생
    @IBAction func touchDown(_ sender: Any) {
        print("touchDown")
    }
    
    /// 같은 버튼을 빠르게 두 번 이상 연속으로 터치할 때 발생
    @IBAction func touchDownRepeat(_ sender: Any) {
        print("touchDownRepeat")
    }
    

    /// 사용자가 버튼을 누른 상태에서 손가락을 움직일 때 버튼 내부에 있는 동안에만 발생
    @IBAction func touchDragInside(_ sender: Any) {
        print("touchDragInside")
    }
    

    /// 사용자가 버튼을 누른 상태에서 손가락을 버튼 외부로 움직일 때 발생
    @IBAction func touchDragOutside(_ sender: Any) {
        print("touchDragOutside")
    }
    
    /// 사용자가 다른 위치에서 버튼으로 드래그할 때 버튼 영역 안으로 진입할 때 호출
    @IBAction func touchDragEnter(_ sender: Any) {
        print("touchDragEnter")
    }

    /// 사용자가 버튼을 누른 상태에서 버튼 영역 밖으로 드래그할 때 호출
    @IBAction func touchDragExit(_ sender: Any) {
        print("touchDragExit")
    }
```

<br><br>

### 연동할 스토리보드 코드

<img width="300" alt="스크린샷 2023-10-25 오후 4 29 24" src="https://github.com/isGeekCode/TIL/assets/76529148/f73c14ec-bb76-41b8-b98c-54c2fc794ae7">

<br>

스토리보드 파일을 SourceCode로 보기 형식으로 바꾸고 아래 코드로 수정하면 된다.

그후, 다시 Interface Builder로 원복 시키면 스토리보드로 볼 수 있다.
<img width="600" alt="스크린샷 2023-10-25 오후 4 30 29" src="https://github.com/isGeekCode/TIL/assets/76529148/6e415755-d501-4b88-9c93-7e2eded781ec">

<details>
<summary>스토리보드 소스코드 보기</summary>
<div markdown="1">

```swift
<?xml version="1.0" encoding="UTF-8"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="22154" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" useTraitCollections="YES" useSafeAreas="YES" colorMatched="YES" initialViewController="BYZ-38-t0r">
    <device id="retina6_12" orientation="portrait" appearance="light"/>
    <dependencies>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="22130"/>
        <capability name="Named colors" minToolsVersion="9.0"/>
        <capability name="Safe area layout guides" minToolsVersion="9.0"/>
        <capability name="System colors in document resources" minToolsVersion="11.0"/>
        <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
    </dependencies>
    <scenes>
        <!--View Controller-->
        <scene sceneID="tne-QT-ifu">
            <objects>
                <viewController id="BYZ-38-t0r" customClass="ViewController" customModule="UIKitSample" customModuleProvider="target" sceneMemberID="viewController">
                    <view key="view" contentMode="scaleToFill" id="8bC-Xf-vdC">
                        <rect key="frame" x="0.0" y="0.0" width="393" height="852"/>
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <subviews>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="cEg-hE-n1X">
                                <rect key="frame" x="96.666666666666686" y="159" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="width" constant="200" id="fJD-kP-Ymj"/>
                                    <constraint firstAttribute="height" constant="40" id="wO9-mj-qQ4"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Up Inside"/>
                                <connections>
                                    <action selector="touchUpInside:" destination="BYZ-38-t0r" eventType="touchUpInside" id="gXW-vl-HRE"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="chZ-0q-Kwm">
                                <rect key="frame" x="96.666666666666686" y="229" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="height" constant="40" id="egw-LZ-OZP"/>
                                    <constraint firstAttribute="width" constant="200" id="z37-jF-J0F"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Up Outside"/>
                                <connections>
                                    <action selector="touchUpOutside:" destination="BYZ-38-t0r" eventType="touchUpOutside" id="eX5-Im-szf"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="rtK-vb-uvs">
                                <rect key="frame" x="96.666666666666686" y="299" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="height" constant="40" id="S3h-fW-4Er"/>
                                    <constraint firstAttribute="width" constant="200" id="zfu-YP-EKM"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Down"/>
                                <connections>
                                    <action selector="touchDown:" destination="BYZ-38-t0r" eventType="touchDown" id="ZIT-7b-obh"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="EsI-Ec-jcQ">
                                <rect key="frame" x="96.666666666666686" y="369" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="height" constant="40" id="EdO-Qq-zW0"/>
                                    <constraint firstAttribute="width" constant="200" id="Xpx-NH-G97"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Down Repeat"/>
                                <connections>
                                    <action selector="touchDownRepeat:" destination="BYZ-38-t0r" eventType="touchDownRepeat" id="AH0-Fn-7m3"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="UJC-cl-oSM">
                                <rect key="frame" x="96.666666666666686" y="439" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="width" constant="200" id="7tX-WW-klu"/>
                                    <constraint firstAttribute="height" constant="40" id="dRh-JP-vlv"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Drag Inside"/>
                                <connections>
                                    <action selector="touchDragInside:" destination="BYZ-38-t0r" eventType="touchDragInside" id="HoI-yj-MKV"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="SDE-zk-T2A">
                                <rect key="frame" x="96.666666666666686" y="509" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="height" constant="40" id="Lul-vD-l3P"/>
                                    <constraint firstAttribute="width" constant="200" id="df4-Kd-gAO"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Drag Outside"/>
                                <connections>
                                    <action selector="touchDragOutside:" destination="BYZ-38-t0r" eventType="touchDragOutside" id="ifx-fM-WXd"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="bcE-d0-yvm">
                                <rect key="frame" x="96.666666666666686" y="579" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="height" constant="40" id="0cF-LE-b1f"/>
                                    <constraint firstAttribute="width" constant="200" id="QET-Qd-xZa"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Drag Enter"/>
                                <connections>
                                    <action selector="touchDragEnter:" destination="BYZ-38-t0r" eventType="touchDragEnter" id="lV9-hZ-Ll4"/>
                                </connections>
                            </button>
                            <button opaque="NO" contentMode="scaleToFill" contentHorizontalAlignment="center" contentVerticalAlignment="center" buttonType="system" lineBreakMode="middleTruncation" translatesAutoresizingMaskIntoConstraints="NO" id="jTq-mK-k4v">
                                <rect key="frame" x="96.666666666666686" y="649" width="200" height="40"/>
                                <color key="backgroundColor" name="AccentColor"/>
                                <constraints>
                                    <constraint firstAttribute="height" constant="40" id="ASc-D1-pFZ"/>
                                    <constraint firstAttribute="width" constant="200" id="t7s-rK-dQJ"/>
                                </constraints>
                                <color key="tintColor" white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
                                <state key="normal" title="Button"/>
                                <buttonConfiguration key="configuration" style="plain" title="Touch Drag Exit"/>
                                <connections>
                                    <action selector="touchDragExit:" destination="BYZ-38-t0r" eventType="touchDragExit" id="ce3-Vw-sPx"/>
                                </connections>
                            </button>
                        </subviews>
                        <viewLayoutGuide key="safeArea" id="6Tk-OE-BBY"/>
                        <color key="backgroundColor" systemColor="systemBackgroundColor"/>
                        <constraints>
                            <constraint firstItem="jTq-mK-k4v" firstAttribute="centerX" secondItem="6Tk-OE-BBY" secondAttribute="centerX" id="0zT-Ct-9CY"/>
                            <constraint firstItem="SDE-zk-T2A" firstAttribute="top" secondItem="UJC-cl-oSM" secondAttribute="bottom" constant="30" id="6l5-uj-dkr"/>
                            <constraint firstItem="jTq-mK-k4v" firstAttribute="top" secondItem="bcE-d0-yvm" secondAttribute="bottom" constant="30" id="Ffd-UF-dV7"/>
                            <constraint firstItem="UJC-cl-oSM" firstAttribute="top" secondItem="EsI-Ec-jcQ" secondAttribute="bottom" constant="30" id="ITa-VH-Khe"/>
                            <constraint firstItem="chZ-0q-Kwm" firstAttribute="centerX" secondItem="6Tk-OE-BBY" secondAttribute="centerX" id="NK1-BW-yOk"/>
                            <constraint firstItem="EsI-Ec-jcQ" firstAttribute="centerX" secondItem="rtK-vb-uvs" secondAttribute="centerX" id="VEr-Lb-SRs"/>
                            <constraint firstItem="rtK-vb-uvs" firstAttribute="top" secondItem="chZ-0q-Kwm" secondAttribute="bottom" constant="30" id="Wlo-Ce-7Yg"/>
                            <constraint firstItem="rtK-vb-uvs" firstAttribute="centerX" secondItem="chZ-0q-Kwm" secondAttribute="centerX" id="XqO-8r-TcP"/>
                            <constraint firstItem="cEg-hE-n1X" firstAttribute="centerX" secondItem="6Tk-OE-BBY" secondAttribute="centerX" id="Zj3-pz-Hbn"/>
                            <constraint firstItem="EsI-Ec-jcQ" firstAttribute="top" secondItem="rtK-vb-uvs" secondAttribute="bottom" constant="30" id="c5j-Lc-wFX"/>
                            <constraint firstItem="bcE-d0-yvm" firstAttribute="centerX" secondItem="6Tk-OE-BBY" secondAttribute="centerX" id="cwi-vs-ASY"/>
                            <constraint firstItem="chZ-0q-Kwm" firstAttribute="top" secondItem="cEg-hE-n1X" secondAttribute="bottom" constant="30" id="daB-vv-Zk7"/>
                            <constraint firstItem="UJC-cl-oSM" firstAttribute="centerX" secondItem="EsI-Ec-jcQ" secondAttribute="centerX" id="hgk-8y-89S"/>
                            <constraint firstItem="SDE-zk-T2A" firstAttribute="centerX" secondItem="6Tk-OE-BBY" secondAttribute="centerX" id="ifO-6Y-pfM"/>
                            <constraint firstItem="cEg-hE-n1X" firstAttribute="top" secondItem="6Tk-OE-BBY" secondAttribute="top" constant="100" id="oCH-Ut-59P"/>
                            <constraint firstItem="bcE-d0-yvm" firstAttribute="top" secondItem="SDE-zk-T2A" secondAttribute="bottom" constant="30" id="qr2-ew-7Wp"/>
                        </constraints>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="dkx-z0-nzr" sceneMemberID="firstResponder"/>
            </objects>
            <point key="canvasLocation" x="-671" y="-23"/>
        </scene>
    </scenes>
    <resources>
        <namedColor name="AccentColor">
            <color red="0.0" green="0.46000000000000002" blue="0.89000000000000001" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
        </namedColor>
        <systemColor name="systemBackgroundColor">
            <color white="1" alpha="1" colorSpace="custom" customColorSpace="genericGamma22GrayColorSpace"/>
        </systemColor>
    </resources>
</document>

```

</div>
</details>

<br><br>

## History

- 231025 : 초안 작성
