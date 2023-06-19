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






## History
- 230616 : 예제1,2 생성
- 230619 : 예제 파일 분리
