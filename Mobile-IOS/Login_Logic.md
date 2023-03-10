# Login Logic (feat. UserDefault)

### userDefault를 이용해 login정보를 저장, 로드하고 그걸 통해 로그인화면을 띄워주는 방법



```swift
        let isLogin = CommonMethod.getUserDefaultIsLoginInfo()
        var msg: String


        
        override func viewDidLoad() {
        super.viewDidLoad()


     if !(isLogin) {
            msg = "isLoginInfo: \(isLogin) 로그인화면 present"
            moveLoginVC()
        } else {
            msg = "isLoginInfo: \(isLogin) -> 페이지 유지"
        }
    }
   


    func moveLoginVC() {
        guard let LoginVc = self.storyboard?.instantiateViewController(withIdentifier: "LoginViewController") as? LoginViewController else {return}
        LoginVc.modalPresentationStyle = UIModalPresentationStyle.fullScreen
        self.present(LoginVc, animated: true, completion: nil)
    }

```
