# 'setVolume:' is deprecated: first deprecated in iOS 7.0 - Use MPVolumeView for volume control.


```
'setVolume:' is deprecated: first deprecated in iOS 7.0 - Use MPVolumeView for volume control.
```


'setVolume:' 메소드는 iOS 7.0 버전부터 더 이상 권장되지 않는다. 

`MPVolumeView`를 사용하는 방식으로 변경하여 사용을 권장한다.  



```swift
        // 기존의 volumeView 상단에 MPVolumeView 생성
        MPVolumeView *volumeView = [[MPVolumeView alloc] initWithFrame: CGRectZero];
        volumeView.showsRouteButton = NO;
        UISlider *volumeViewSlider = nil;
        for (UIView *view in volumeView.subviews) {
            if ([view isKindOfClass:[UISlider class]]) {
                volumeViewSlider = (UISlider *)view;
                break;
            }
        }
        
        // addSubView하지 않고 생성만 하고 사용 -> 기존의 커스텀 슬라이더를 사용하기 위함
        
        _volumeView = [[VolumeView alloc] init];
        _volumeView.frame = CGRectMake((w - CIRCLE_DIAMETER) / 2 * 1.5 + CIRCLE_DIAMETER - fixedImageWidth / 2,
                                       CIRCLE_DIAMETER / 2 - fixedImageHeight / 2,
                                       fixedImageWidth + CIRCLE_THICK/*drag 여유*/,
                                       fixedImageHeight);
        _volumeView.image = sourceImage;
        [_volumeView setContentMode:UIViewContentModeScaleAspectFit];
        _volumeView.onChanged = ^(float value){
            [[MPMusicPlayerController applicationMusicPlayer] setVolume:value/100.0f];
            // 새로생성한 volumeViewSlider에 기존 값 연동
              volumeViewSlider.value = value/100.0f;
        };
        
```
