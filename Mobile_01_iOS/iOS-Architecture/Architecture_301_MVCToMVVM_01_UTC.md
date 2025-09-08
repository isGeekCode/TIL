# MVC to MVVM : 01. UTC 오늘, 현재, 내일 시간보기

## 화면
<img width="471" alt="스크린샷 2023-06-16 오후 2 14 41" src="https://github.com/isGeekCode/TIL/assets/76529148/f52a94b1-5789-4e5e-8a68-5a926b6b04c4">

## 기존구조

### Model
```swift

struct UtcTimeModel: Codable {
    let id: String
    let currentDateTime: String
    let utcOffset: String
    let isDayLightSavingsTime: Bool
    let dayOfTheWeek: String
    let timeZoneName: String
    let currentFileTime: Int
    let ordinalDate: String
    let serviceResponse: String?

    enum CodingKeys: String, CodingKey {
        case id = "$id"
        case currentDateTime
        case utcOffset
        case isDayLightSavingsTime
        case dayOfTheWeek
        case timeZoneName
        case currentFileTime
        case ordinalDate
        case serviceResponse
    }
}

/*
 API RESPONSE
 {
 "$id": "1",
 "currentDateTime": "2023-06-16T05:10Z",
 "utcOffset": "00:00:00",
 "isDayLightSavingsTime": false,
 "dayOfTheWeek": "Friday",
 "timeZoneName": "UTC",
 "currentFileTime": 133313658149914960,
 "ordinalDate": "2023-167",
 "serviceResponse": null
 }
 */

```

### View

```swift
@IBOutlet var datetimeLabel: UILabel!

@IBAction func onYesterday() {
    guard let yesterday = Calendar.current.date(byAdding: .day, value: -1, to: currentDateTime) else { return }
    currentDateTime = yesterday
    updateDateTime()
}

@IBAction func onNow() {
    fetchNow()
}

@IBAction func onTomorrow() {
    guard let tomorrow = Calendar.current.date(byAdding: .day, value: +1, to: currentDateTime) else { return }
    currentDateTime = tomorrow
    updateDateTime()
}
```

### Controller
```swift

override func viewDidLoad() {
    super.viewDidLoad()
    fetchNow()
}

private var currentDateTime = Date()

private func fetchNow() {
    let url = "http://worldclockapi.com/api/json/utc/now"

    datetimeLabel.text = "Loading.."

    URLSession.shared.dataTask(with: URL(string: url)!) { [weak self] data, _, _ in

        guard let data = data else { return }
        guard let model = try? JSONDecoder().decode(UtcTimeModel.self, from: data) else { return }
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd'T'HH:mm'Z'"

        guard let now = formatter.date(from: model.currentDateTime) else { return }
        self?.currentDateTime = now

        DispatchQueue.main.async {
            self?.updateDateTime()
        }
    }.resume()
}

private func updateDateTime() {
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
    datetimeLabel.text = formatter.string(from: currentDateTime)
}

```



## MVC 전체코드
```swift
//
//  MainViewController.swift
//  UTCTime
//
//  Created by bang_hyeonseok on 2023/06/16.
//

import UIKit

class MainViewController: UIViewController {
    
    // MARK: - VIEW
    @IBOutlet var datetimeLabel: UILabel!
    
    @IBAction func onYesterday() {
        guard let yesterday = Calendar.current.date(byAdding: .day, value: -1, to: currentDateTime) else { return }
        currentDateTime = yesterday
        updateDateTime()
    }

    @IBAction func onNow() {
        fetchNow()
    }

    @IBAction func onTomorrow() {
        guard let tomorrow = Calendar.current.date(byAdding: .day, value: +1, to: currentDateTime) else { return }
        currentDateTime = tomorrow
        updateDateTime()
    }

    // MARK: - CONTROLLER

    override func viewDidLoad() {
        super.viewDidLoad()
        fetchNow()
    }

    private var currentDateTime = Date()

    private func fetchNow() {
        let url = "http://worldclockapi.com/api/json/utc/now"

        datetimeLabel.text = "Loading.."

        URLSession.shared.dataTask(with: URL(string: url)!) { [weak self] data, _, _ in

            guard let data = data else { return }
            guard let model = try? JSONDecoder().decode(UtcTimeModel.self, from: data) else { return }
            
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy-MM-dd'T'HH:mm'Z'"

            guard let now = formatter.date(from: model.currentDateTime) else { return }
            self?.currentDateTime = now

            DispatchQueue.main.async {
                self?.updateDateTime()
            }
        }.resume()
    }

    private func updateDateTime() {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
        datetimeLabel.text = formatter.string(from: currentDateTime)
    }


    // MARK: - MODEL

    struct UtcTimeModel: Codable {
        let id: String
        let currentDateTime: String
        let utcOffset: String
        let isDayLightSavingsTime: Bool
        let dayOfTheWeek: String
        let timeZoneName: String
        let currentFileTime: Int
        let ordinalDate: String
        let serviceResponse: String?

        enum CodingKeys: String, CodingKey {
            case id = "$id"
            case currentDateTime
            case utcOffset
            case isDayLightSavingsTime
            case dayOfTheWeek
            case timeZoneName
            case currentFileTime
            case ordinalDate
            case serviceResponse
        }
    }

    /*
     API RESPONSE
     {
     "$id": "1",
     "currentDateTime": "2023-06-16T05:10Z",
     "utcOffset": "00:00:00",
     "isDayLightSavingsTime": false,
     "dayOfTheWeek": "Friday",
     "timeZoneName": "UTC",
     "currentFileTime": 133313658149914960,
     "ordinalDate": "2023-167",
     "serviceResponse": null
     }
     */
}
```

## MVVM 작업하기

### Model과 View의 관계

View는 화면이고 Model은 화면에 그려지기 위한 데이터이다. 
Model은 여러가지 형태로 변형되게 된다.
최초로 서버에서 가져온건 JSON이다
JSON에서부터 화면에 보여지기 까진 아래와 같은 과정을 거친다.
```
JSON
-> UTCTimeModel  
-> String       // 실제 currentDateTime만 사용
-> Date
-> String
```

여기서 실제로 모델이라 보여줄 만한것은 `Date`뿐이다. 
실제 시간이라는 값을 가지고 있다. 그래서 데이터로서 시간이라는 것을 갖고 있는 부분이 이 부분인 것이다.  

또한 이 시간을 화면에 보여주기 위해선 Date타입으로만 가지고 있을게 아니라 String 타입으로 변형이 일어나야한다. 
따라서 모델은 한가지로만 존재하는 것이 아니라 상황에 따라 여러가지 형태로 존재하게 된다. 

```
서버 Model // 서버에서 가져온 모델
-> UTCTimeModel  

Model    // 실제 데이터로서의 역할을 수행하는 모델 
-> Date

화면 Model // 화면에 보여지기 위한 모델
-> String
```

앱에서는 Model 자체로만 화면에 보여줄 수 없기 때문에 View용 모델을 따로 만든것이 ViewModel이다. 
```
Entity   // Server Model 혹은 DB Model을 통칭

Model 

ViewModel 
```
이 세가지는 모두 Model이다. 
그렇다면 Entity를 가져오는 것은 뭘까
Entity를 Fetch 하는 것은 보통 Repository라고 하고 Entity는 그 결과물이다. 
Entity를 만들면 그걸 가지고 Model을 만드는 존재인 Mapper가 있다. Model은 그 결과물이다.

그리고 이 Model을 가지고 Logic을 수행한다. 
이 Logic을 수행하고 화면에 보여주기 위해선 ViewModel을 거치고 View에 보여주게 된다. 

```
Repository
- Entity
Mapper
- Model 
Logic
- ViewModel
View 
```

### Entity 나누기
- Entity.swift 생성
- 기존 MVC로 구성했던 부분중 Model 부분을 분리한다. 

```swift
// MARK: - MODEL

struct UtcTimeModel: Codable {
    let id: String
    let currentDateTime: String
    let utcOffset: String
    let isDayLightSavingsTime: Bool
    let dayOfTheWeek: String
    let timeZoneName: String
    let currentFileTime: Int
    let ordinalDate: String
    let serviceResponse: String?

    enum CodingKeys: String, CodingKey {
        case id = "$id"
        case currentDateTime
        case utcOffset
        case isDayLightSavingsTime
        case dayOfTheWeek
        case timeZoneName
        case currentFileTime
        case ordinalDate
        case serviceResponse
    }
}

/*
 API RESPONSE
 {
 "$id": "1",
 "currentDateTime": "2023-06-16T05:10Z",
 "utcOffset": "00:00:00",
 "isDayLightSavingsTime": false,
 "dayOfTheWeek": "Friday",
 "timeZoneName": "UTC",
 "currentFileTime": 133313658149914960,
 "ordinalDate": "2023-167",
 "serviceResponse": null
 }
 */

```

### Entity를 fetch할 Repository 만들기
- Repository.swift 생성
- Fetch 동작을 하는 코드 이전
    - Repository 빈 클래스 생성
    - 내부에 fetch 부분을 이동처리
- 파일분리로 인하여 코드수정
    - FIXME: 1. 외부 클래스이기 때문에 private 삭제
    - FIXME: 2. 직접적으로 View의 text를 지정하는 부분을 삭제
    - FIXME: 3. 외부 클래스로 전달을 위해 탈출클로저로 수정처리
    - FIXME: 4. View 내용을 변경시킬 데이터를 탈출클로저 변수에 세팅


```swift
class Repository {
    
    // FIXME: 1. private 삭제
    // FIXME: 3. fetchNow()를 탈출클로저로 변경

    // private func fetchNow()
    func fetchNow(onCompleted: @escaping (Date) -> Void) {
        let url = "http://worldclockapi.com/api/json/utc/now"

        // FIXME: 2. 삭제
        // datetimeLabel.text = "Loading.."

        URLSession.shared.dataTask(with: URL(string: url)!) { [weak self] data, _, _ in

            guard let data = data else { return }
            guard let model = try? JSONDecoder().decode(UtcTimeModel.self, from: data) else { return }
            
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy-MM-dd'T'HH:mm'Z'"

            guard let now = formatter.date(from: model.currentDateTime) else { return }
            
            // FIXME: 2. 삭제
            // self?.currentDateTime = now

            DispatchQueue.main.async {
                // FIXME: 4. 탈출클로저 변수에 세팅
                onCompleted(now)
                // self?.updateDateTime()
            }
        }.resume()
    }
}
```

### Entity에서 가져올 Model 만들기
- Model.swift 생성
- Model을 생성하는 코드 이전
    - Model 빈 클래스 생성
    - 내부에 Model 생성 부분을 이동처리

```swift
class Model {

    // FIXME: 1. private 삭제
    //  private var currentDateTime = Date()
    var currentDateTime = Date()

}
```

### Model로부터 비즈니스로직을 수행할 Logic 만들기
- Logic.swift 생성
- 비즈니스로직을 수행하는 코드 이전
    - Logic 빈 클래스 생성
    - 로직에 해당하는 부분을 이동처리
- 파일분리로 인하여 코드수정
    - FIXME: 1. 외부 클래스이기 때문에 private 삭제
    - FIXME: 2. 기존 IBAction 어노테이션 삭제
    - FIXME: 3. now를 통해서 다른 

```swift

/// Model을 이용해 비즈니스 로직을 수행할  클래스
class Logic {
    
    func onYesterday(now: Date) -> Date {
        guard let yesterday = Calendar.current.date(byAdding: .day,
                                                    value: -1,
                                                    to: now) else { return now }
        return yesterday
    }
    /*
     @IBAction func onYesterday() {
         guard let yesterday = Calendar.current.date(byAdding: .day, value: -1, to: currentDateTime) else { return }
         currentDateTime = yesterday
         updateDateTime()
     }
     */
    
    
    func onNow() {
    }
    /*
     @IBAction func onNow() {
         fetchNow()
     }
     */
    
     func onTomorrow(now: Date) -> Date {
        guard let tomorrow = Calendar.current.date(byAdding: .day,
                                                   value: +1,
                                                   to: now) else { return now }
        return tomorrow
    }
    /*
     @IBAction func onTomorrow() {
        guard let tomorrow = Calendar.current.date(byAdding: .day, value: +1, to: currentDateTime) else { return }
        currentDateTime = tomorrow
        updateDateTime()
    }
     */
}

```


### 화면에 보여질 ViewModel만들기
- ViewModel.swift 생성
    - Logic 빈 클래스 생성
    - 비즈니스로직에 해당하는 부분을 이동처리
- 파일분리로 인하여 코드수정
    - FIXME: 1. 외부에서 접근하기위한 모델로 사용할 변수 생성
    - FIXME: 2. 재사용가능하도록 파라미터값 추가, 변수 dateTimeString를 변경처리.
- ViewController에서 변수 dateTimeString를 가져오기 전에 Fetch하기위한 함수 생성
```swift
class ViewModel {
    // FIXME: 1. 외부에서 접근하기 위한 변수 세팅
    var dateTimeString: String = "Loading.."
    
    // FIXME: 2. 재사용가능하도록 파라미터값 추가, 변수 dateTimeString를 변경처리
    private func dateToString(date: Date) {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
        dateTimeString = formatter.string(from: date)
    }

    /*
     private func updateDateTime() {
         let formatter = DateFormatter()
         formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
         datetimeLabel.text = formatter.string(from: currentDateTime)
     }
     */
     
     

}

```

여기까지 분리하면 이제 기존 ViewController는 아래처럼 된다.

```swift
class MainViewController: UIViewController {

    @IBOutlet var datetimeLabel: UILabel!
    
    @IBAction func onYesterday() { }

    @IBAction func onNow() { }

    @IBAction func onTomorrow() { }

    override func viewDidLoad() {
        super.viewDidLoad()
    }
}
```
이제 이렇게 나눈 모듈을 연결한다. 

### 화면에 보여질 ViewController애서 
View입장에서는 화면에 보여지는걸 ViewModel로부터 얻어와야한다. 

```swift

    @IBOutlet var datetimeLabel: UILabel!

    // 1. viewModel생성
    let viewModel = ViewModel()

    override func viewDidLoad() {
        super.viewDidLoad()
        // 2. dateTimeLabel의 스트링값을 ViewModel에서 가져오기
        datetimeLabel.text = viewModel.dateTimeString
    }
```

이제 datetimeLabel.text는 viewModel로 부터 가져오게 되는데 가져올 값이 Fetch 되어야한다.
그래서 그전에 viewModel.viewDidLoad() 처럼 viewModel에서 Fetch를 위한 함수를 실행해주어야한다.
```swift

    let viewModel = ViewModel()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // MARK: 3. viewModel의 변수 dateTimeString를 Fetch해야하기 때문에 Fetch를 위한 함수 실행
        viewModel.viewDidLoad()
        datetimeLabel.text = viewModel.dateTimeString
    }
```

### viewModel의 Fetch 함수 구현
viewModel 자체에는 Fetch를 하기위한 메서드가 존재하지 않고 Logic에 요청한다. 이제 Logic은 Service라고 이름을 바꿔보자

Service라는 객체에서 fetchNow라는 함수를 하나 생성해서 실행시킨다.
```swift
class ViewModel {

    var dateTimeString: String = "Loading.."
    
    // FIXME: 1. ViewModel의 변수를 Fetch시킬 Service(비즈니스로직) 객체를 생성
    let service = Service()
    
    func viewDidLoad() {
        // FIXME: 2. Service(비즈니스로직) 객체로부터 FetchNow를 요청
        service.fetchNow()
    }
    
    private func dateToString(date: Date) {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
        dateTimeString = formatter.string(from: date)
    }
}
```

### Service의 Fetch 함수 구현
Service(Logic)부분도 아직 정보를 가져오지않기 떄문에 Service에서 Fetch를 위한 함수를 구현한다.
이때 repository 객체를 이닛해서 정보를 가져온다.

```swift

class Service {

    let repository = Repository()
    
    func fetchNow() {
        repository.fetchNow(onCompleted: <#T##(Date) -> Void#>)

}
    
    // 이미 완성됐기때문에 생략
    func onYesterday(now: Date) -> Date {}
    
    // 이미 완성됐기때문에 생략
    func onTomorrow(now: Date) -> Date {}

}
```

이때 repository의 fetchNow는 탈출클로저인데, Service의 fetchNow도 이걸 그대로 받아서 넘길 수 있도록 repository의 fetchNow메서드의 탈출클로저를 동일하게 구현한다.

차이점은 Service에서는 Model을 전달한다. 
```swift

class Service {

    let repository = Repository()
    
    // FIXME: repository의 fetchNow와 동일하게 구현하지만 Model을 가져온다.
    func fetchNow(onCompleted: @escaping (Model) -> Void) {
    //func fetchNow() {
        repository.fetchNow(onCompleted: <#T##(Date) -> Void#>)
    }
    
    // 이미 완성됐기때문에 생략
    func onYesterday(now: Date) -> Date {}
    
    // 이미 완성됐기때문에 생략
    func onTomorrow(now: Date) -> Date {}

}
```

그러면 Repository 내부에서도 탈출클로저에 Model를 담아서 넘기는 것으로 수정한다.

```swift

class Repository {

    func fetchNow(onCompleted: @escaping (UtcTimeModel) -> Void) {

        let url = "http://worldclockapi.com/api/json/utc/now"

        URLSession.shared.dataTask(with: URL(string: url)!) { [weak self] data, _, _ in

            guard let data = data else { return }
            guard let model = try? JSONDecoder().decode(UtcTimeModel.self, from: data) else { return }
                        
            // FIXME: 6. onCompleted()안에는 model만 보내는 것으로 수정
            onCompleted(model)
            
        }.resume()
    }
}
```
그러면 이젠 Repository는 fetchNow를 통해 Entity를 생성해서 넘길수가 있게 된다.
이제 Service를 마저 완성해보자

Service에서는 Repository부터 받은 Entity를 탈출클저를 통해 가공한다.

```swift
class Service {
    let repository = Repository()
    
    func fetchNow(onCompleted: @escaping (Model) -> Void) {
        
        // - FIXME: 6. 가져온 entity는 viewModel로 넘기기위해 Model로 가공한다.
        repository.fetchNow { entity in
            
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy-MM-dd'T'HH:mm'Z'"

            guard let now = formatter.date(from: entity.currentDateTime) else { return }

            let model = Model(currentDateTime: now)

            onCompleted(model)
            
            /*
            // Repository에서 가져온 부분
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy-MM-dd'T'HH:mm'Z'"

            guard let now = formatter.date(from: model.currentDateTime) else { return }
             */
        }
    }
```


다음 viewModel에서는 Service로 부터 받은 Model을 가지고 String타입으로 변환한다.
이 값은 viewModel의 변수인 dateTimeString에 담는다. 
그러면 ViewController에서 viewModel의 변수에 접근해 String값을 가져올 수 있다.

```swift
class ViewModel {
    
    var dateTimeString: String = "Loading.."
    
    let service = Service()
    
    func viewDidLoad() {
        // FIXME: 7. 탈출클로저로 넘어온 Model을 String으로 바꿔서 View에서 접근하도록 처리
        service.fetchNow { [weak self] model in
            guard let self = self else { return }
            let dateString = self.dateToString(date: model.currentDateTime)
            self.dateTimeString = dateString
        }
    }
    
    // FIXME: 8. return 형식을 String으로 변경
    private func dateToString(date: Date) -> String {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
        dateTimeString = formatter.string(from: date)
        return formatter.string(from: date)
    }
}
```

이렇게만 하면 변경이 view가 변경이 되지않는다. fetch가 완료되는 시점에 콜백으로 String값을 View로 불러와야한다. 
이제 ViewModel의 변수가 바뀌는 시점을 바인딩 해준다.

이 시점에서 몇개의 메서드들을 수정했다.

```swift
class ViewModel {
    
    var onUpdated: () -> Void = {}
    
    var dateTimeString: String = "Loading.." // 화면에 보여져야할 모델
    {
        didSet {
            onUpdated()
        }
    }
}
```
viewModel에 위와 같이 onUpdated를 생성하고 ViewModel의 변수가 수정될때마다 후행클로저를 실행하도록 하고

ViewController에서 아래와 같이 onUpdated를 이용하여 viewDidLoad를 완성한다.
```swift
class MainViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        viewModel.onUpdated = { [weak self] in
            DispatchQueue.main.async {
                self?.datetimeLabel?.text = self?.viewModel.dateTimeString
            }
        }
        viewModel.reload()
}
```


최종적으로 MVVM으로 수정한 코드는 아래와 같다.

### ViewController
```swift
import UIKit

class MainViewController: UIViewController {

    @IBOutlet var datetimeLabel: UILabel!
    
    @IBAction func onYesterday() {
        viewModel.moveDay(day: -1)
    }

    @IBAction func onNow() {
        datetimeLabel.text = "Loading..."
        viewModel.reload()
    }

    @IBAction func onTomorrow() {
        viewModel.moveDay(day: +1)
    }

    let viewModel = ViewModel()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        viewModel.onUpdated = { [weak self] in
            DispatchQueue.main.async {
                self?.datetimeLabel?.text = self?.viewModel.dateTimeString
            }
        }
        viewModel.reload()

    }
}


```
### ViewModel
```swift
import Foundation

class ViewModel {
    
    var onUpdated: () -> Void = {}
    
    var dateTimeString: String = "Loading.." // 화면에 보여져야할 모델
    {
        didSet {
            onUpdated()
        }
    }
    
    let service = Service()
    
    func reload() {
        service.fetchNow { [weak self] model in
            guard let self = self else { return }
            let dateString = self.dateToString(date: model.currentDateTime)
            self.dateTimeString = dateString
        }
    }
        
    private func dateToString(date: Date) -> String {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy년 MM월 dd일 HH시 mm분"
        dateTimeString = formatter.string(from: date)
        return formatter.string(from: date)
    }
    
    func moveDay(day: Int) {
        service.moveDay(day: day)
        dateTimeString = dateToString(date: service.currentModel.currentDateTime)
    }
}

```
### Service
```swift
import Foundation

class Service {
    let repository = Repository()
    
    var currentModel = Model(currentDateTime: Date())
    
    func fetchNow(onCompleted: @escaping (Model) -> Void) {
        
        repository.fetchNow { entity in
            
            let formatter = DateFormatter()
            formatter.dateFormat = "yyyy-MM-dd'T'HH:mm'Z'"

            guard let now = formatter.date(from: entity.currentDateTime) else { return }

            let model = Model(currentDateTime: now)
            self.currentModel = model
            onCompleted(model)
        }
    }
    
    func moveDay(day: Int) {
        guard let moveDay = Calendar.current.date(byAdding: .day,
                                                    value: day,
                                                    to: currentModel.currentDateTime) else { return }
        
        currentModel.currentDateTime = moveDay
    }
    
}

```
### Model
```swift
import Foundation

struct Model {
    var currentDateTime = Date()
}

```
### Repository
```swift
import Foundation

class Repository {

    func fetchNow(onCompleted: @escaping (UtcTimeModel) -> Void) {
        let url = "http://worldclockapi.com/api/json/utc/now"

        URLSession.shared.dataTask(with: URL(string: url)!) { [weak self] data, _, _ in

            guard let data = data else { return }
            guard let model = try? JSONDecoder().decode(UtcTimeModel.self, from: data) else { return }
            
            onCompleted(model)
            
        }.resume()
    }
}

```
### Entity
```swift
struct UtcTimeModel: Codable {
    let id: String
    let currentDateTime: String
    let utcOffset: String
    let isDayLightSavingsTime: Bool
    let dayOfTheWeek: String
    let timeZoneName: String
    let currentFileTime: Int
    let ordinalDate: String
    let serviceResponse: String?

    enum CodingKeys: String, CodingKey {
        case id = "$id"
        case currentDateTime
        case utcOffset
        case isDayLightSavingsTime
        case dayOfTheWeek
        case timeZoneName
        case currentFileTime
        case ordinalDate
        case serviceResponse
    }
}

```


## History
- 230616 : 예제1,2 생성
- 230619 : 예제 파일 분리
