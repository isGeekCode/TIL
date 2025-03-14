# Swift Concurrency - Async / Await / Task

## 기본개념

**핵심**
• async : 비동기 함수 선언
• await : 비동기 작업이 끝날 때까지 기다림
• Task {} : 비동기 함수를 실행할 때 사용


**🔹 왜 async/await를 사용할까?*
1. 기존의 **Completion Handler** 방식보다 **코드가 직관적**이다.
2. 네트워크 요청, 파일 읽기, 애니메이션 등 **시간이 걸리는 작업을 중단하지 않고 실행** 가능하다.
3. async를 함수 앞에 붙이면 **비동기 함수**가 되고, 이를 호출할 때 await을 사용하면 **결과를 기다렸다가 실행**할 수 있다.

<br><br>

## 📌 3. Task 이해하기

**🔹 Task의 역할*
• Swift에서 **비동기 작업을 실행하는 컨테이너** 역할을 한다.
• **await을 만나면 작업이 끝날 때까지 대기하지만, 전체 앱이 멈추지는 않는다.**
• Task가 끝나면 결과를 반환한다.
• **새로운 쓰레드를 생성하는 것이 아니라 컨텍스트에 따라 실행 방식이 결정됨**.

**🔹 Task는 새로운 쓰레드를 만드는 것이 아니다!**
Swift의 Task {}는 **현재 실행 중인 컨텍스트를 고려하여 실행**된다.

즉, **메인 스레드에서 실행되면 메인 스레드에서 실행**되지만, 백그라운드에서 실행될 수도 있다.

```swift
Task {
    print(Thread.isMainThread ? "🟢 메인 스레드에서 실행됨" : "🔵 백그라운드 스레드에서 실행됨")
}
```

<br><br>

## 📌 4. Async/Await 사용법
#### 기본적인 async/await 사용법
```swift
// async 키워드로 비동기 함수 선언
func fetchData() async -> String {
    return "✅ 데이터 가져오기 완료"
}

// await 키워드를 붙여야 실행 가능
Task {
    let result = await fetchData()
    print(result)
}
```

<br><br>

#### 비동기 작업중 기다리기
```swift
func fetchData() async -> String {
    try? await Task.sleep(nanoseconds: 2 * 1_000_000_000) // 2초 대기
    return "✅ 데이터 가져오기 완료"
}

Task {
    let result = await fetchData()
    print(result)
}
```

<br><br>

####  여러 비동기 작업을 동시에 실행 (async let)
두 개의 작업이 동시에 실행되어 실행 속도가 빨라진다

```swift
func fetchUserData() async -> String {
    try? await Task.sleep(nanoseconds: 2 * 1_000_000_000)
    return "👤 사용자 데이터 완료"
}

func fetchPosts() async -> String {
    try? await Task.sleep(nanoseconds: 3 * 1_000_000_000)
    return "📝 게시글 데이터 완료"
}

Task {
    async let user = fetchUserData()
    async let post = fetchPosts()
    
    print(await user)
    print(await post)
}

```

<br><br>

## 📌 5. UI 업데이트 시 주의 사항

> ⚠️ 비동기 함수에서 UI 업데이트는 반드시 메인 스레드에서 실행해야 한다!



**🔹 기존 방식 (DispatchQueue.main.async)**
```swift
func updateUI() async {
    let data = await fetchData()
    DispatchQueue.main.async {
        print("✅ UI 업데이트: \(data)")
    }
}
```

**🔹 @MainActor 활용 (Swift 추천 방식)**

Swift에서는 @MainActor를 사용하면 **자동으로 메인 스레드에서 실행**되도록 할 수 있다.

```swift
@MainActor
func updateUI(data: String) {
    print("✅ UI 업데이트: \(data)")
}

```

또는 **클래스 전체에 적용할 수도 있음!**

```swift
@MainActor
class MyViewModel {
    func updateUI(data: String) {
        print("✅ UI 업데이트: \(data)")
    }
}
```

**🔹 @MainActor를 무분별하게 사용하면 성능 저하 발생!**

모든 코드가 메인 스레드에서 실행되면 **UI 업데이트 외의 작업도 메인 스레드에서 처리**하여 앱의 응답성이 저하될 수 있음.

  

✅ **해결 방법**: **UI 관련 작업만 @MainActor 적용하고, 나머지는 백그라운드에서 처리**


```swift
func fetchData() async -> String {
    try? await Task.sleep(nanoseconds: 2_000_000_000)
    return "✅ 데이터 가져오기 완료"
}

func updateUI() async {
    let data = await fetchData() // 백그라운드에서 실행됨
    await MainActor.run { // UI 업데이트 부분만 메인 스레드에서 실행
        print("🔄 UI 업데이트: \(data)")
    }
}


// 혹은 업데이트 메서드를 따로 분리
@MainActor
func updateUI(data: String) {
    print("✅ UI 업데이트: \(data)")
}

Task {
    let fetchedData = await fetchData()
    await updateUI(data: fetchedData)
}

```

<br><br>


## 📌 6. 기존 Completion Handler 방식과 비교
전통적인 방식이다. 

👉 기존 방식은 **전화로 연락해서 확인하는 느낌**
👉 async/await는 **알람을 맞춰놓고 기다리는 것처럼 자연스럽다**

**🔹 기존의 Completion Handler 방식**
```swift
func boilWater(completion: @escaping () -> Void) {
    print("💧 물을 끓이기 시작합니다...")
    DispatchQueue.global().asyncAfter(deadline: .now() + 3) {
        print("🔥 물이 끓었습니다!")
        completion()  // 나중에 결과를 알려줌
    }
}

boilWater {
    print("🍜 라면을 넣고 끓입니다.")
}
```

**🔹 Async / Await 방식**
```swift
func boilWater() async {
    print("💧 물을 끓이기 시작합니다...")
    try? await Task.sleep(nanoseconds: 3 * 1_000_000_000)
    print("🔥 물이 끓었습니다!")
}

func makeRamen() async {
    await boilWater()
    print("🍜 라면을 넣고 끓입니다.")
}

Task {
    await makeRamen()
}
```

<br><br>

## withCheckedContinuation 사용하기

### ✅ withCheckedContinuation이란?

`withCheckedContinuation`은 **콜백 기반 API를 `async/await` 방식으로 변환**할 때 사용한다.  
비동기 작업을 **중단(suspend)** 후 **재개(resume)** 하여, 기존의 Completion Handler 패턴을 개선할 수 있다.

#### 📌 언제 사용해야 할까?
- 기존 **Completion Handler 기반 API를 `async/await`으로 변환**할 때  
- 비동기 라이브러리(Firebase, CoreBluetooth 등)와 연동할 때  
- 비동기 작업의 결과를 `async` 함수에서 반환해야 할 때  

#### ❌ 사용하지 않아도 되는 경우
- 이미 `async` 함수로 제공되는 API 사용 (`URLSession.shared.data(from:)` 등)  

### 🛠 기본 사용법
```swift
func fetchRemoteConfig() async -> Bool {
    return await withCheckedContinuation { continuation in
        remoteConfig.fetchAndActivate { status, error in
            if let error = error {
                print("❌ Error: \(error.localizedDescription)")
                continuation.resume(returning: false) // 실패 시 false 반환
            } else {
                continuation.resume(returning: true) // 성공 시 true 반환
            }
        }
    }
}
```

### ✅ 동작 방식
- 1️⃣ withCheckedContinuation 실행 시 함수가 일시 중단(suspend)
- 2️⃣ 비동기 작업 완료 후 continuation.resume(returning:)을 호출하여 값 반환
- 3️⃣ await이 해제되며 호출한 쪽에서 값이 반환됨



### ✅ 기존 Completion Handler 방식과 비교

```swift
// 기존 방식 (Completion Handler)
func fetchRemoteConfig(completion: @escaping (Bool) -> Void) {

    remoteConfig.fetchAndActivate { status, error in
        if let error = error {
            print("❌ RemoteConfig Fetch Error: \(error.localizedDescription)")
            completion(false)
        } else {
            completion(true)
        }
    }
}

fetchRemoteConfig { result in
    if result {
        print("✅ RemoteConfig 가져오기 성공")
    } else 
        print("❌ RemoteConfig 가져오기 실패")
    }
}




// withCheckedContinuation 사용 (async/await 변환)

func fetchRemoteConfig() async -> Bool {

    return await withCheckedContinuation { continuation in

        remoteConfig.fetchAndActivate { status, error in

            if let error = error {

                print("❌ RemoteConfig Fetch Error: \(error.localizedDescription)")

                continuation.resume(returning: false)

            } else {

                continuation.resume(returning: true)

            }
        }
    }
}

  

Task {
    let result = await fetchRemoteConfig()
    print(result ? "✅ RemoteConfig 가져오기 성공" : "❌ RemoteConfig 가져오기 실패")
}

```

💡 결과
- withCheckedContinuation을 사용하면 콜백 없이 await fetchRemoteConfig()로 직관적으로 호출 가능
- 기존 Completion Handler 대비 가독성이 좋아지고, 체이닝이 용이

⸻

🚀 결론
- withCheckedContinuation은 기존의 콜백 기반 비동기 API를 async/await으로 변환하는 데 유용하다.
- 사용하지 않아도 되는 경우: 이미 async API로 제공되는 기능 사용 시.


## 히스토리
- 2025-03-10: 최초 작성
- 2025-03-11: withCheckedContinuation 추가
