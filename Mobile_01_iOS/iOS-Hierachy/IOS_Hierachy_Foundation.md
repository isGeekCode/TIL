# iOS_Hierachy - Foundation


Foundation은 애플리케이션의 기본적인 기능을 제공하는 프레임워크로서, 앱 개발에 필요한 기본적인 데이터 구조, 파일 처리, 문자열 처리, 날짜 및 시간 처리, 네트워킹, 메모리 관리 등의 기능을 포함하고 있다.

 그래서 모든 애플리케이션에 필요한 공통적인 작업을 다룬다.
 
Foundation 프레임워크에는 NSObject 클래스를 상속받고 있다.

### 주요 클래스

- NSString, NSArray, NSDictionary: 문자열, 배열, 딕셔너리와 같은 기본적인 데이터 구조를 다루는 클래스들.
- NSDate, NSCalendar: 날짜와 시간을 다루는 클래스들.
- NSFileManager: 파일과 디렉토리 관리를 위한 클래스.
- NSURLSession: 네트워킹을 위한 클래스로 데이터를 서버로 보내거나 받아오는 데 사용.
- NSNotificationCenter: 앱 내에서 이벤트와 정보를 전달하고 관리하는 클래스.

이 밖에도 다양한 클래스가 있다. 

전체적인 리스트는 Tree참고


### 위치
Foundation 프레임워크는 아래 경로에 위치해 있다.

```
/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/System/Library/Frameworks/Foundation.framework
```

### Tree
```swift
├── Headers
│   ├── Foundation.apinotes
│   ├── Foundation.h
│   ├── FoundationErrors.h
│   ├── FoundationLegacySwiftCompatibility.h
│   ├── NSArray.h
│   ├── NSAttributedString.h
│   ├── NSAutoreleasePool.h
│   ├── NSBundle.h
│   ├── NSByteCountFormatter.h
│   ├── NSByteOrder.h
│   ├── NSCache.h
│   ├── NSCalendar.h
│   ├── NSCharacterSet.h
│   ├── NSCoder.h
│   ├── NSComparisonPredicate.h
│   ├── NSCompoundPredicate.h
│   ├── NSData.h
│   ├── NSDate.h
│   ├── NSDateComponentsFormatter.h
│   ├── NSDateFormatter.h
│   ├── NSDateInterval.h
│   ├── NSDateIntervalFormatter.h
│   ├── NSDecimal.h
│   ├── NSDecimalNumber.h
│   ├── NSDictionary.h
│   ├── NSEnergyFormatter.h
│   ├── NSEnumerator.h
│   ├── NSError.h
│   ├── NSException.h
│   ├── NSExpression.h
│   ├── NSExtensionContext.h
│   ├── NSExtensionItem.h
│   ├── NSExtensionRequestHandling.h
│   ├── NSFileCoordinator.h
│   ├── NSFileHandle.h
│   ├── NSFileManager.h
│   ├── NSFilePresenter.h
│   ├── NSFileVersion.h
│   ├── NSFileWrapper.h
│   ├── NSFormatter.h
│   ├── NSHTTPCookie.h
│   ├── NSHTTPCookieStorage.h
│   ├── NSHashTable.h
│   ├── NSISO8601DateFormatter.h
│   ├── NSIndexPath.h
│   ├── NSIndexSet.h
│   ├── NSInflectionRule.h
│   ├── NSInvocation.h
│   ├── NSItemProvider.h
│   ├── NSItemProviderReadingWriting.h
│   ├── NSJSONSerialization.h
│   ├── NSKeyValueCoding.h
│   ├── NSKeyValueObserving.h
│   ├── NSKeyedArchiver.h
│   ├── NSLengthFormatter.h
│   ├── NSLinguisticTagger.h
│   ├── NSListFormatter.h
│   ├── NSLocale.h
│   ├── NSLock.h
│   ├── NSMapTable.h
│   ├── NSMassFormatter.h
│   ├── NSMeasurement.h
│   ├── NSMeasurementFormatter.h
│   ├── NSMetadata.h
│   ├── NSMetadataAttributes.h
│   ├── NSMethodSignature.h
│   ├── NSMorphology.h
│   ├── NSNetServices.h
│   ├── NSNotification.h
│   ├── NSNotificationQueue.h
│   ├── NSNull.h
│   ├── NSNumberFormatter.h
│   ├── NSObjCRuntime.h
│   ├── NSObject.h
│   ├── NSOperation.h
│   ├── NSOrderedCollectionChange.h
│   ├── NSOrderedCollectionDifference.h
│   ├── NSOrderedSet.h
│   ├── NSOrthography.h
│   ├── NSPathUtilities.h
│   ├── NSPersonNameComponents.h
│   ├── NSPersonNameComponentsFormatter.h
│   ├── NSPointerArray.h
│   ├── NSPointerFunctions.h
│   ├── NSPort.h
│   ├── NSPredicate.h
│   ├── NSProcessInfo.h
│   ├── NSProgress.h
│   ├── NSPropertyList.h
│   ├── NSProxy.h
│   ├── NSRange.h
│   ├── NSRegularExpression.h
│   ├── NSRelativeDateTimeFormatter.h
│   ├── NSRunLoop.h
│   ├── NSScanner.h
│   ├── NSSet.h
│   ├── NSSortDescriptor.h
│   ├── NSStream.h
│   ├── NSString.h
│   ├── NSTextCheckingResult.h
│   ├── NSThread.h
│   ├── NSTimeZone.h
│   ├── NSTimer.h
│   ├── NSURL.h
│   ├── NSURLAuthenticationChallenge.h
│   ├── NSURLCache.h
│   ├── NSURLConnection.h
│   ├── NSURLCredential.h
│   ├── NSURLCredentialStorage.h
│   ├── NSURLError.h
│   ├── NSURLProtectionSpace.h
│   ├── NSURLProtocol.h
│   ├── NSURLRequest.h
│   ├── NSURLResponse.h
│   ├── NSURLSession.h
│   ├── NSUUID.h
│   ├── NSUbiquitousKeyValueStore.h
│   ├── NSUndoManager.h
│   ├── NSUnit.h
│   ├── NSUserActivity.h
│   ├── NSUserDefaults.h
│   ├── NSValue.h
│   ├── NSValueTransformer.h
│   ├── NSXMLParser.h
│   ├── NSXPCConnection.h
│   └── NSZone.h

```
