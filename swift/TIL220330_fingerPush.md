# 핑거푸시 설치가이드

# 핑거푸시란

# 핑거푸시 SDK 설치가이드

[이용가이드 링크](https://helloworld.fingerpush.com/swift-%ed%94%84%eb%a1%9c%ec%a0%9d%ed%8a%b8%ec%97%90%ec%84%9c-%ed%95%91%ea%b1%b0%ed%91%b8%ec%8b%9c-%ec%9d%b4%ec%9a%a9%eb%b2%95/)

## **방법 1 – 수동으로 “ProjectName-Bridging-Header.h” 추가하기**

**1.1 Xcode의 project navigator에서 오른쪽 클릭하여 new file/souce 에서 Header File 선택 후, “ProjectName-Bridging-Header.h” 로 추가한다.**

**1.2 build settings 에서 Objective-C Bridging Header 에 “ProjectName-Bridging-Header.h” 의 경로를 추가한다.**

**1.3 “ProjectName-Bridging-Header.h” 에 #import <finger /finger.h> 추가한다.**

**1.4 라이브러리 사용하기**

```swift
/***
AppDelegate에 핑거푸시서버와 연동을 하기 위해서 다음과 같이 설정합니다.
***/

//핑거푸시
func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
    // Override point for customization after application launch.

    finger.sharedData().setAppKey("발급받은 앱키")
    finger.sharedData().setAppScrete("급받은 앱시크리트키")
..
..
 return true
}
```

## **방법 2 – 자동으로 “ProjectName-Bridging-Header.h” 추가하기**

**2.1 Xocde의 project navigator에서 오른쪽 클릭하여 new file / source 에서 Cocoa Touch Class 를 선택한다.**

**2.2 Class 명을 입력하고, Language를 Objective-c / swift 로 선택한 다음 Next를 선택한다.**

**2.3 Create Bridging Header 선택한다.**

– 생성된 파일일 중 헤더파일만 필요하므로, \*.m파일은 삭제해도 무방

**2.4 라이브러리 사용하기**

```swift
/***
AppDelegate에 핑거푸시서버와 연동을 하기 위해서 다음과 같이 설정합니다.
***/

//핑거푸시
func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
    // Override point for customization after application launch.

    finger.sharedData().setAppKey("발급받은 앱키")
    finger.sharedData().setAppScrete("급받은 앱시크리트키")
..
..

}
```

notification 앱 흐름 절차

### 1. 알림허용 요청

로컬/푸시 알림을 사용하기 위해서는 유저에게 승인을 받아야 합니다.

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

/*핑거 푸시*/
        forBuildStyle(debug: {
            //디버그일 경우
            fingerManager?.setAppKey("핑거푸시 APP KEY를 등록해주세요.")
            fingerManager?.setAppScrete("핑거푸시 APP SECRET KEY를 등록해주세요.")

        }) {
            fingerManager?.setAppKey("핑거푸시 APP KEY를 등록해주세요.")
            fingerManager?.setAppScrete("핑거푸시 APP SECRET KEY를 등록해주세요.")
        }

        /*apns 등록*/
        registeredForRemoteNotifications(application: application)

        return true
}

//MARK: - 푸시 등록
    func registeredForRemoteNotifications(application: UIApplication) {

        #if !targetEnvironment(simulator)

        if #available(iOS 10.0, *) {

            let center = UNUserNotificationCenter.current()
            center.delegate = self
            // 카테고리를 이용한 NotificationAction
            //payload category 는 fp (이미지가 있을 경우 fp가 자동으로 함께 전송됩니다.)
            /*
            let acceptAction = UNNotificationAction(identifier: "com.kissoft.yes", title: "확인", options: .foreground)
            let declineAction = UNNotificationAction(identifier: "com.kissoft.no", title: "닫기", options: .destructive)
            let category = UNNotificationCategory(identifier: "fp", actions: [acceptAction,declineAction], intentIdentifiers: [], options: .customDismissAction)
            center.setNotificationCategories([category])
             */

						// 사용여부 체크
            center.requestAuthorization(options: [.alert,.badge,.sound], completionHandler: { (granted, error) in
						    // log("granted : \(granted) / error : \(String(describing: error))")

								// 승인받았는지 여부를 여기서 확인
//1.
								guard granted else {
	                print("유저가 푸쉬알림을 허락하지 않음")
                return
	              }

                DispatchQueue.main.async(execute: {
                // 사용여부에 따른 푸시 등록 하는 함수 실행됨
                    application.registerForRemoteNotifications()
                    print("유저가 푸쉬알림을 허락한 상태")
                })
//2.
//            if error != nil {
//                //error 발생시
//                Dprint("push register error \(String(describing: error?.localizedDescription))")
//            }else if granted {
//                self.pushAllow = true
//                Dprint("push register agreement !!!!!")
//                DispatchQueue.main.async {
//                    self.application?.registerForRemoteNotifications()
//                    UserDefaults.standard.setValue(true, forKey: Configs.UserDefaultKey.pushAllwoedCheck)
//                }
//            }else {
//                //거부시
//                self.pushAllow = false
//                UserDefaults.standard.setValue(false, forKey: Configs.UserDefaultKey.pushAllwoedCheck)
//                Dprint("push regiser denied  @!!!!!!")
//            }

            })
        }
        #endif
    }

```

APNs서버에 등록 이후, 핑거푸시에 기기등록

```swift
func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {

        //토큰값을 가져옴
        let tokenParts = deviceToken.map { data in String(format: "%02.2hhx", data) }
        let token = tokenParts.joined()


        // 사용하려는 푸시 서비스 API에 기기토큰정보 등록
        finger.sharedData().registerUser(withBlock: deviceToken) { posts, error in
            print("finger token : " + ((self.fingerManager?.getToken()) ?? "없음"))
            print("finger DeviceIdx : " + ((self.fingerManager?.getDeviceIdx()) ?? "없음"))

            if error != nil {
                print("핑거푸시서버 기기 등록확인 \(String(describing: posts))" )
            } else {
                print("핑거푸시서버 기기등록 error \(String(describing: error))")
            }

            if (posts != nil) {
                //기기등록
                print("기기등록: \(String(describing: posts))")

            } else {
                //기기등록
                print("기기등록 error: \(String(describing: error))")
            }



        }
        // 콘솔에 토큰값 표시
        print("Device Token: \(token)\n")

    }

log("DeviceToken: \(deviceToken.description)")


        fingerManager?.registerUser(withBlock: deviceToken, { (posts, error) -> Void in

            log("finger token : " + ((self.fingerManager?.getToken()) ?? "없음"))
            log("finger DeviceIdx : " + ((self.fingerManager?.getDeviceIdx()) ?? "없음"))

            log("posts: \(String(describing: posts)) error: \(String(describing: error))")

        })
    }

```

### 2. UNUserNotificationCenterDelegate 프로토콜 채택

받은 알림을 처리하기위해 UNUserNotificationCenterDelegate 프로토콜을 채택하여 알림 처리를 위한 메서드를 구현해 줍니다.

```swift
extension AppDelegate: UNUserNotificationCenterDelegate {

// 애플리케이션이 foreground에 있는 경우 호출
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {

        completionHandler([.list, .badge, .sound, .banner])
    }

func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {

        let userInfo = response.notification.request.content.userInfo
        log("\(userInfo)")

        /*핑거푸시 읽음처리*/
        checkPush(userInfo)

        let strAction = response.actionIdentifier
        log(strAction)
        if strAction.contains("yes") || strAction.contains("UNNotificationDefaultActionIdentifier") {
            showPopUp(userInfo: userInfo)
        }

        completionHandler()
    }

}
```

```swift
// 핑거푸시 말고 일반트리거 사용하는 경우
func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
        let identifier = response.notification.request.identifier
        let userInfo = response.notification.request.content.userInfo

        switch identifier {
        case "id":
            dump(userInfo)
        default:
            break
        }

        completionHandler()
    }
```

### 3. 알림 보내기

알림을 보내기 위해서는 UNUserNotificationCenter에 알림요청 객체인 UNNotificationRequest를 추가해주면 됩니다.

### 4. Badge 초기화

애플리케이션이 백그라운드에서 포그라운드로 진입할 경우 뱃지 카운트를 초기화할 수 있습니다.

# Rich Notification

## **Notification Service Extension 생성**

**1. 기존 앱에 새 타겟(Notification Service Extension)을 추가합니다.**

**2. 새 타겟의 옵션을 각자에 맞게 설정합니다.**

– 애플 개발자 사이트에서 Notification Service Extension 만의 App ID와 Provisioning Profiles 을 생성해줘야 합니다.

참고 : Embed In Application 설정은 Xcode의 TAGETS/General/Embedded Binaries 에서 수정이 가능합니다.

**3. plist 설정**– Notification Service Extension 의 info.plist 에서 App Transport Security Settings 을 아래와 같이 설정합니다.(핑거푸시를 통해서 이미지를 다운로드하려면 필요한 설정입니다.)

## **Notification Service Extension 구현**

### **AppDelegate에 iOS10 RemoteNotification 등록**

```swift
// Swift

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

				/*apns 등록*/
        registeredForRemoteNotifications(application: application)

        return true
}

//MARK: - 푸시 등록
    func registeredForRemoteNotifications(application: UIApplication) {

        #if !targetEnvironment(simulator)

        if #available(iOS 10.0, *) {

            let center = UNUserNotificationCenter.current()
            center.delegate = self
            // 카테고리를 이용한 NotificationAction
            //payload category 는 fp (이미지가 있을 경우 fp가 자동으로 함께 전송됩니다.)
            /*
            let acceptAction = UNNotificationAction(identifier: "com.kissoft.yes", title: "확인", options: .foreground)
            let declineAction = UNNotificationAction(identifier: "com.kissoft.no", title: "닫기", options: .destructive)
            let category = UNNotificationCategory(identifier: "fp", actions: [acceptAction,declineAction], intentIdentifiers: [], options: .customDismissAction)
            center.setNotificationCategories([category])
             */
            center.requestAuthorization(options: [.alert,.badge,.sound], completionHandler: { (granted, error) in

                log("granted : \(granted) / error : \(String(describing: error))")

                DispatchQueue.main.async(execute: {
                    application.registerForRemoteNotifications()
                })

            })

        }

        #endif
    }

// Objective C
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
/***
RemoteNotifications 등록
***/
        UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
        center.delegate = self;

        [center requestAuthorizationWithOptions:(UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error){

            NSLog(@"granted :%i / error : %@",granted,error);

            if (granted) {
                [application registerForRemoteNotifications];
            }

        }];

}
```

### **AppDelegate에서 iOS10 Rich Notification 수신**

```swift
// Swift


//MARK: - 푸시 얼럿
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {

        completionHandler([.alert,.sound])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {

        let userInfo = response.notification.request.content.userInfo
        log("\(userInfo)")

        /*핑거푸시 읽음처리*/
        checkPush(userInfo)

        let strAction = response.actionIdentifier
        log(strAction)
        if strAction.contains("yes") || strAction.contains("UNNotificationDefaultActionIdentifier") {
            showPopUp(userInfo: userInfo)
        }

        completionHandler()
    }

func showPopUp(userInfo:[AnyHashable: Any]){

        var topRootViewController = UIApplication.shared.keyWindow!.rootViewController

        while topRootViewController!.presentedViewController != nil
        {
            topRootViewController = topRootViewController!.presentedViewController
        }

        if topRootViewController!.isKind(of: UINavigationController.self){

            let root = (topRootViewController as! UINavigationController).viewControllers.first

            if root!.isKind(of: PopUpTableViewController.self){

                let mainStoryboard: UIStoryboard = UIStoryboard(name: "Main", bundle: nil)
                let child = mainStoryboard.instantiateViewController(withIdentifier: "PopUpTableViewController") as! PopUpTableViewController
                child.dicData = userInfo as [NSObject : AnyObject]?
                (topRootViewController as! UINavigationController).pushViewController(child, animated: false)

            }

        }else if topRootViewController!.isKind(of: TabBarController.self){

            (topRootViewController as! TabBarController).showPopUp(userInfo)

        }

    }

    //MARK: - 푸시 오픈 체크
    func checkPush(_ UserInfo : [AnyHashable : Any]){

        finger.sharedData().requestPushCheck(withBlock: UserInfo , { (posts, error) -> Void in

            log("posts: \(String(describing: posts)) error: \(String(describing: error))")

        })
    }

// showPopUp 함수에 필요한 PopUpTableViewController, TabBarController

import UIKit

class TabBarController: UITabBarController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.

        if(segue.identifier == "PopUpSegue"){
            let navi = segue.destination as! UINavigationController
            let child = navi.viewControllers.first as! PopUpTableViewController
            child.dicData = (sender as! [AnyHashable: Any] as [NSObject : AnyObject]?)
        }

    }

    // MARK: - 팝업
    func showPopUp(_ param:[AnyHashable: Any]){
        performSegue(withIdentifier: "PopUpSegue", sender:param)
    }

}

import UIKit

class PopUpTableViewController: UITableViewController ,UITextViewDelegate{

    var dicData:[AnyHashable: Any]?

    private var myTitle: String = "푸시 컨텐츠"

    private let fingerManager = finger.sharedData()
    private var dicPushContents = [String:String]()

    override func viewDidLoad() {
        super.viewDidLoad()

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()

        self.navigationItem.title = myTitle
        self.tableView.tableFooterView = UIView()

        let buttonItemDicData = UIBarButtonItem(barButtonSystemItem: .compose, target: self, action: #selector(self.showDicData))
        self.navigationItem.rightBarButtonItem = buttonItemDicData

        let buttonItemFlex = UIBarButtonItem(barButtonSystemItem: .flexibleSpace, target: nil, action: nil)
        let buttonItemClose = UIBarButtonItem(barButtonSystemItem: .done, target: self, action: #selector(self.closeSelf))
        self.setToolbarItems([buttonItemFlex, buttonItemClose, buttonItemFlex], animated: false)

        self.navigationController!.setToolbarHidden(false, animated: false)
        self.navigationController?.toolbar.tintColor = .black

        getPushContents()

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows

        return dicPushContents.count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCell(withIdentifier: "PopUpCellIdentifier", for: indexPath)
        // Configure the cell...

        let strKey = dicPushContents.keys.sorted()[indexPath.row]
        cell.textLabel?.text = strKey
        cell.detailTextLabel?.text = dicPushContents[strKey]

        cell.textLabel?.numberOfLines = 0
        cell.detailTextLabel?.numberOfLines = 0

        return cell

    }

    // MARK: -
    @objc func closeSelf(){
        self.dismiss(animated: true, completion: nil)
    }

    @objc func showDicData(){
        //
        do {
            let jsonData = try JSONSerialization.data(withJSONObject: self.dicData as Any, options: JSONSerialization.WritingOptions.prettyPrinted)

            do {
                let json = try JSONSerialization.jsonObject(with: jsonData, options: .mutableContainers)
                log("\(json)")

                //내용 얼럿
                let alert = UIAlertController(title: "", message: "\(json)", preferredStyle: .alert)
                alert.addAction(UIAlertAction(title: "확인", style: .default, handler: nil))
                self.present(alert, animated: true)

            } catch let jsonErr {
                log("\(jsonErr)")
            }

        } catch let error {
            log("\(error)")
        }

    }

    // MARK: - finger

    /**푸시 정보 가져오기*/
    func getPushContents(){

        UIApplication.shared.isNetworkActivityIndicatorVisible = true
        self.navigationItem.title = myTitle + " 확인 중"

        fingerManager?.requestPushContent(withBlock: self.dicData) { (posts, error) -> Void in

            if error != nil {
                log("error : \(error.debugDescription)")
            }

            if posts != nil{
                log("posts : \(posts!)")

                for (key, value) in posts ?? [:] {
                    self.dicPushContents[key as! String] = (value as! String)
                }

                self.tableView.reloadData()
            }

            UIApplication.shared.isNetworkActivityIndicatorVisible = false
            self.navigationItem.title = self.myTitle

        }

    }

}
```

```swift
// Objective C/
***
UNUserNotificationCenterDelegate
***/
- (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler{

    completionHandler(UNNotificationPresentationOptionAlert);

}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)())completionHandler {

    completionHandler();
}
```

### AppDelegate 세팅

```swift
//
//  AppDelegate.swift
//  FingerPushExample
//
//  Copyright (c) 2015년 kissoft. All rights reserved.
//

import UIKit
import UserNotifications

@UIApplicationMain

class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {

    var window: UIWindow?
    private let fingerManager = finger.sharedData()

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        //핑거 푸시 sdk 버전
        log("SdkVer : " + finger.getSdkVer())

        /*핑거 푸시*/
				// 디버그용과 생성방식이 다르다.
        forBuildStyle(debug: {
            //디버그일 경우
            fingerManager?.setAppKey("핑거푸시 APP KEY를 등록해주세요.")
            fingerManager?.setAppScrete("핑거푸시 APP SECRET KEY를 등록해주세요.")

        }) {
            fingerManager?.setAppKey("핑거푸시 APP KEY를 등록해주세요.")
            fingerManager?.setAppScrete("핑거푸시 APP SECRET KEY를 등록해주세요.")
        }

        /*apns 등록*/
        registeredForRemoteNotifications(application: application)

        return true
    }

    //MARK: - 푸시 등록
    func registeredForRemoteNotifications(application: UIApplication) {

        #if !targetEnvironment(simulator)

        if #available(iOS 10.0, *) {

            let center = UNUserNotificationCenter.current()
            center.delegate = self
            // 카테고리를 이용한 NotificationAction
            //payload category 는 fp (이미지가 있을 경우 fp가 자동으로 함께 전송됩니다.)
            /*
            let acceptAction = UNNotificationAction(identifier: "com.kissoft.yes", title: "확인", options: .foreground)
            let declineAction = UNNotificationAction(identifier: "com.kissoft.no", title: "닫기", options: .destructive)
            let category = UNNotificationCategory(identifier: "fp", actions: [acceptAction,declineAction], intentIdentifiers: [], options: .customDismissAction)
            center.setNotificationCategories([category])
             */
            center.requestAuthorization(options: [.alert,.badge,.sound], completionHandler: { (granted, error) in

                log("granted : \(granted) / error : \(String(describing: error))")

                DispatchQueue.main.async(execute: {
                    application.registerForRemoteNotifications()
                })

            })

        }

        #endif
    }

    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {

        log("DeviceToken: \(deviceToken.description)")

        fingerManager?.registerUser(withBlock: deviceToken, { (posts, error) -> Void in

            log("finger token : " + ((self.fingerManager?.getToken()) ?? "없음"))
            log("finger DeviceIdx : " + ((self.fingerManager?.getDeviceIdx()) ?? "없음"))

            log("posts: \(String(describing: posts)) error: \(String(describing: error))")

        })
    }

    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {

        if let dicAps = userInfo["aps"] as? Dictionary<String,Any> {

            if let ca = dicAps["content-available"] {
                //
                if ca as! Int == 1 {
                    //사일런트 푸시일 경우 처리
                    completionHandler(UIBackgroundFetchResult.newData)
                    return
                }

            }

        }

        /*핑거푸시 읽음처리*/
        checkPush(userInfo)

        completionHandler(UIBackgroundFetchResult.noData)
    }

    func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
        log("\(error)")
    }

    //MARK: - 푸시 얼럿
    func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {

        completionHandler([.alert,.sound])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {

        let userInfo = response.notification.request.content.userInfo
        log("\(userInfo)")

        /*핑거푸시 읽음처리*/
        checkPush(userInfo)

        let strAction = response.actionIdentifier
        log(strAction)
        if strAction.contains("yes") || strAction.contains("UNNotificationDefaultActionIdentifier") {
            showPopUp(userInfo: userInfo)
        }

        completionHandler()
    }

    func applicationWillResignActive(_ application: UIApplication) {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
        // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }

    func applicationWillTerminate(_ application: UIApplication) {
        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
    }

    //MARK: -
    func showPopUp(userInfo:[AnyHashable: Any]){

        var topRootViewController = UIApplication.shared.keyWindow!.rootViewController

        while topRootViewController!.presentedViewController != nil
        {
            topRootViewController = topRootViewController!.presentedViewController
        }

        if topRootViewController!.isKind(of: UINavigationController.self){

            let root = (topRootViewController as! UINavigationController).viewControllers.first

            if root!.isKind(of: PopUpTableViewController.self){

                let mainStoryboard: UIStoryboard = UIStoryboard(name: "Main", bundle: nil)
                let child = mainStoryboard.instantiateViewController(withIdentifier: "PopUpTableViewController") as! PopUpTableViewController
                child.dicData = userInfo as [NSObject : AnyObject]?
                (topRootViewController as! UINavigationController).pushViewController(child, animated: false)

            }

        }else if topRootViewController!.isKind(of: TabBarController.self){

            (topRootViewController as! TabBarController).showPopUp(userInfo)

        }

    }

    //MARK: - 푸시 오픈 체크
    func checkPush(_ UserInfo : [AnyHashable : Any]){

        finger.sharedData().requestPushCheck(withBlock: UserInfo , { (posts, error) -> Void in

            log("posts: \(String(describing: posts)) error: \(String(describing: error))")

        })
    }

}
```
