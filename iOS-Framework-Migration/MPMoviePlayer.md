# MPMoviePlayerController Deprecated in iOS 10, Replaced by AVPlayerViewController in iOS 7


```
'moviePlayer' is deprecated: first deprecated in iOS 9.0 - Use AVPlayerViewController in AVKit.
```

AVPlayerViewController는 iOS 7.0부터 도입되었지만 iOS 9.0부터 MPMoviePlayerController의 대체제로 사용되기 시작한다. 

MPMoviePlayerController는 iOS에서 오래 사용하던 비디오 플레이어 컴포넌트인데, 기본적인 비디오 재생 기능만을 제공했다.  

AVPlayerViewController으로 대체된 주된 이유는 더 향상된 기능과 유연성 때문이다.  

AVPlayerViewController는 AVFoundation 프레임워크의 일부로,  
보다 고급 기능과 맞춤형 비디오 재생 경험을 제공한다.  

## 나아진 점
- **커스텀 사용자 인터페이스**
    - AVPlayerViewController를 사용하면 개발자가 비디오 플레이어의 사용자 인터페이스를 더 세밀하게 제어하고 사용자 정의할 수 있다. 즉, 앱의 디자인과 더 잘 어울리게 만들 수 있다는 의미다.
- **더 나은 스트리밍 지원** 
    - AVPlayerViewController는 다양한 스트리밍 형식과 프로토콜을 지원하여, 라이브 스트리밍이나 온디맨드 비디오 재생에 더 적합해졌다.
- **자막과 클로즈드 캡션 지원** 
    - 사용자가 필요로 하는 자막과 클로즈드 캡션을 쉽게 통합하고 제어할 수 있다.
- **에어플레이와 외부 디스플레이 지원** 
    - 사용자가 비디오를 Apple TV나 다른 에어플레이 호환 디바이스에 쉽게 스트리밍할 수 있게 해준다.
- **시간 이동 및 탐색 기능** 
    - 사용자가 비디오 내에서 쉽게 특정 시점으로 이동하거나 탐색할 수 있다.
- **백그라운드 오디오 재생** 
    - 앱이 백그라운드에서 실행되는 동안에도 오디오 재생이 가능하다.
- **통합된 프레임워크**
    - AVFoundation 프레임워크의 일부로, 비디오 재생뿐만 아니라 비디오 편집, 오디오 처리 등 다양한 멀티미디어 기능을 쉽게 통합할 수 있다.
        

## 간단한 세팅방법

### 파일명으로 가져오기
  
- URL Path 만들기

MPMoviePlayerController(contentURL:) 메서드를 통해서 준비를 한다.  

파일명으로 사용할때는 URL을 생성시  URL(string: `urlStr`) 메서드를 사용하는게 아니라
URL(fileURLWithPath:`pathStr` 메서드를 이용한다.  

- 파일이 없을 떄의 예외처리를 해준다. 
만약 하지않으면 앱이 종료될 수 있다.  


```swift
// Swift
guard let filePath = Bundle.main.path(forResource: "dog", ofType: "mp4") else {
    print("파일이 존재하지 않습니다.")
    return
}
let fileURL = URL(fileURLWithPath: filePath)
moviePlayer = MPMoviePlayerController(contentURL: fileURL)
// 이후 실행로직은 동일



// OBJC
NSString *filePath = [[NSBundle mainBundle] pathForResource:@"dog" ofType:@"mp4"];

// 파일이 존재하지 않으면 함수 종료
if (![[NSFileManager defaultManager] fileExistsAtPath:filePath]) {
    NSLog(@"파일이 존재하지 않습니다.");
    return; // 파일이 없으므로 여기서 함수를 종료
}

NSURL *fileURL = [NSURL fileURLWithPath:filePath];

self.moviePlayer = [[MPMoviePlayerController alloc] initWithContentURL:fileURL];
// 이후 실행로직은 동일

```


### URL로 가져오기


```swift
// Swift

import UIKit
import MediaPlayer

class MoviePlayerController: UIViewController {
    
    var moviePlayer: MPMoviePlayerController?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        NotificationCenter.default.addObserver(self, selector: #selector(moviePlayerLoadStateChanged), name: .MPMoviePlayerLoadStateDidChange, object: nil)
        NotificationCenter.default.addObserver(self, selector: #selector(moviePlayerPlaybackDidFinish), name: .MPMoviePlayerPlaybackDidFinish, object: nil)

        setupMoviePlayer()

    }

    func setupMoviePlayer() {
        let urlStr = "http://down.humoruniv.com/hwiparambbs/data/editor/pdswait/e_s661a39001_c6c0d855eee53a714dbac585191e3e8bea0376ca.mp4"
        
        guard let videoURL = URL(string: urlStr) else { return }
        moviePlayer = MPMoviePlayerController(contentURL: videoURL)
        moviePlayer?.controlStyle = .default
        moviePlayer?.shouldAutoplay = true
        moviePlayer?.prepareToPlay()

        if let playerView = moviePlayer?.view {
            playerView.frame = self.view.bounds
            self.view.addSubview(playerView)
        }
    
        DispatchQueue.main.async {
            self.moviePlayer?.play() // 재생 시작
        }
        
    }
    
    @objc func moviePlayerLoadStateChanged(notification: NSNotification) {
        // 노티피케이션의 object가 MPMoviePlayerController 타입인지 확인
        if let player = notification.object as? MPMoviePlayerController {
            /**
             MPMoviePlayerController의 현재 로드 상태를 나타낸다.
             - Unknown : 비디오의 로드 상태가 알려지지 않았거나 아직 결정되지 않은상태.  이 상태는 일반적으로 초기 로딩 과정에서 발생하며, 이때 비디오 재생을 시작하거나 계속하는 것이 적절하지 않다.
             - playable: 이 상태는 비디오가 재생 준비가 되어 있음을 의미한다. 즉, 비디오가 충분히 버퍼링되어 재생될 준비가 된 상태
             - playthroughOK: 이 상태는 네트워크를 통해 스트리밍되는 비디오의 경우, 스트림이 원활하게 진행될 것으로 예상됨을 의미
             - Stalled : 비디오의 로딩이 일시적으로 중단된 상태입니다. 이는 네트워크 지연 또는 기타 문제로 인해 비디오 버퍼링이 일시적으로 멈춘 경우에 발생. 이 상태에서는 비디오가 일시적으로 멈출 수 있으며, 로딩이 재개될 때까지 기다려야 할 수 있다.

             */
            
            if player.loadState.contains(.playable) ||
                player.loadState.contains(.playthroughOK) {
                DispatchQueue.main.async {
                    player.play() // 메인 스레드에서 재생 시작
                    print("영상시작")
                }
            }
        }
    }

    @objc func moviePlayerPlaybackDidFinish(notification: NSNotification) {
        // Handle playback finished
        print("영상종료")
    }

    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        moviePlayer?.stop()
    }
}




// OBJC
//
//  ViewController.m
//  movie
//
//  Created by bang_hyeonseok on 12/18/23.
//

#import "ViewController.h"
#import "MediaPlayer/MediaPlayer.h"

@interface ViewController ()

@property (strong, nonatomic) MPMoviePlayerController *moviePlayer;


@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(moviePlayerLoadStateChanged:) name:MPMoviePlayerLoadStateDidChangeNotification object:nil];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(moviePlayerPlaybackDidFinish:) name:MPMoviePlayerPlaybackDidFinishNotification object:nil];
    
    
    [self setupMoviePlayer];
}

- (void)setupMoviePlayer {
    NSString *urlStr = @"http://down.humoruniv.com//hwiparambbs/data/editor/pdswait/e_s661a39002_846dd22bd05ecb889c61558314d4892c8b75978f.mp4";
    
    NSURL *videoURL = [NSURL URLWithString:urlStr];
    self.moviePlayer = [[MPMoviePlayerController alloc] initWithContentURL:videoURL];
    [self.moviePlayer setControlStyle:MPMovieControlStyleDefault];
    [self.moviePlayer setShouldAutoplay:YES];
    [self.moviePlayer prepareToPlay];

    self.moviePlayer.view.frame = self.view.bounds;
    [self.view addSubview:self.moviePlayer.view];

    dispatch_async(dispatch_get_main_queue(), ^{
        [self.moviePlayer play]; // 메인 스레드에서 재생 시작
    });
}

- (void)moviePlayerLoadStateChanged:(NSNotification *)notification {
    MPMoviePlayerController *player = notification.object;
    
    if ([player loadState] & MPMovieLoadStatePlayable ||
        [player loadState] & MPMovieLoadStatePlaythroughOK) {
        dispatch_async(dispatch_get_main_queue(), ^{
            [player play]; // 메인 스레드에서 재생 시작
            NSLog(@"영상시작");
        });
    }
}

- (void)moviePlayerPlaybackDidFinish:(NSNotification *)notification {
    NSLog(@"영상종료");
}

- (void)viewWillDisappear:(BOOL)animated {
    [super viewWillDisappear:animated];
    [self.moviePlayer stop];
}

@end
```


### MPMoviePlayerController에서 사용가능한 NotificationName

아래와 같이 특정시점들을 캐치할 수 있다.  

- MPMoviePlayerWillExitFullscreen
    - 전체 화면 모드를 종료하기 직전
- MPMoviePlayerDidExitFullscreen
    - 전체 화면 모드가 종료된 후
- MPMoviePlayerWillEnterFullscreen
    - 전체 화면 모드로 진입하기 직전
- MPMoviePlayerDidEnterFullscreen
    - 전체 화면 모드로 진입한 후
- MPMovieDurationAvailable
    - 비디오의 전체 재생 시간 정보가 사용 가능해질 때
- MPMovieMediaTypesAvailable
    - 비디오의 미디어 타입 정보가 사용 가능해질 때
- MPMovieSourceTypeAvailable
    - 비디오의 소스 타입 정보가 사용 가능해질 때
- MPMovieNaturalSizeAvailable
    - 비디오의 자연스러운 크기(해상도) 정보가 사용 가능해질 때
- MPMoviePlayerPlaybackDidFinish
    - 비디오의 재생이 완료되었을 때
- MPMoviePlayerTimedMetadataUpdated
    - 타임 메타데이터가 업데이트 되었을 때
- MPMoviePlayerLoadStateDidChange
    - 비디오의 로드 상태가 변경되었을 때
- MPMoviePlayerScalingModeDidChange
    - 비디오의 스케일링 모드가 변경되었을 때
- MPMoviePlayerPlaybackStateDidChange
    - 비디오의 재생 상태가 변경되었을 때
- MPMoviePlayerNowPlayingMovieDidChange
    - 현재 재생 중인 비디오가 변경되었을 때
- MPMoviePlayerReadyForDisplayDidChange
    - 비디오가 디스플레이를 위해 준비된 상태가 변경되었을 때 
- MPMoviePlayerThumbnailImageRequestDidFinish
    - 썸네일 이미지 요청 작업이 완료되었을 때
- MPMoviePlayerIsAirPlayVideoActiveDidChange
    - AirPlay를 통한 비디오 재생의 활성화 상태가 변경되었을 때 

## MPMoviePlayer -> AVPlayer

영상을 실행하는 데 있어 체크해야할 시점은 아래와 같다.  

- 영상경로를 가져오는 로직
- 객체 생성로직
- 영상 실행준비 시점캐치
- 영상 종료시점 캐치
- 영상 종료 이후 로직

기본적으로 MPMoviePlayer는 NotificationCenter를 통해 동작을 캐치하고 구현을 한다.  




## History 
- 231218: 초안작성
