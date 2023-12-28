



```
'setVolume:' is deprecated: first deprecated in iOS 7.0 - Use MPVolumeView for volume control.
```

```swift
        
        MPVolumeView *volumeView = [[MPVolumeView alloc] initWithFrame: CGRectZero];
        volumeView.showsRouteButton = NO;
        UISlider *volumeViewSlider = nil;
        for (UIView *view in volumeView.subviews) {
            if ([view isKindOfClass:[UISlider class]]) {
                volumeViewSlider = (UISlider *)view;
                break;
            }
        }
        
        _volumeView = [[VolumeView alloc] init];
        _volumeView.frame = CGRectMake((w - CIRCLE_DIAMETER) / 2 * 1.5 + CIRCLE_DIAMETER - fixedImageWidth / 2,
                                       CIRCLE_DIAMETER / 2 - fixedImageHeight / 2,
                                       fixedImageWidth + CIRCLE_THICK/*drag 여유*/,
                                       fixedImageHeight);
        _volumeView.image = sourceImage;
        [_volumeView setContentMode:UIViewContentModeScaleAspectFit];
        _volumeView.onChanged = ^(float value){
            [[MPMusicPlayerController applicationMusicPlayer] setVolume:value/100.0f];
              volumeViewSlider.value = value/100.0f;
        };
        
```
