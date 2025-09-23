# UIDatePicker

```swift
func setDatePicker() {

		let datePicker = UIDatePicker()
		
		self.view.addSubview(datePicker)
		
		datePicker.snp.makeConstraints {
		  $0.centerX.centerY.equalTo(self.datePickerView)
		  $0.width.equalTo(self.datePickerView).multipliedBy(0.8)
		}
		
		datePicker.contentHorizontalAlignment = .center
		    datePicker.datePickerMode = .time
		    datePicker.locale = Locale(identifier: "ko-KR")
		    datePicker.timeZone = .autoupdatingCurrent
		    datePicker.minuteInterval = 10
		    datePicker.addTarget(self, action: #selector(changed), for: .valueChanged)
		    if #available(iOS 13.4, *) {
		      datePicker.preferredDatePickerStyle = .wheels
		}
}

/// DatePicker 의 변화 캐치
  @objc func changed(){
        let dateformatter = DateFormatter()

          dateformatter.dateFormat = "a hh시 mm분"
        let dateStr = dateformatter.string(from: datePicker.date)
        self.willSaveTimeValue = datePicker.date

        self.myLabel.text = dateStr
        print("text: \(text)")
  }
```

## DatePickerMode

데이트 피커의 모드는 아래와 같은 종류를 가지고 있다.

- date
- dateAndTIme
- time
- countDownTimer

## dateFormatter

Date타입을 원하는 형태로 변경하여 보여주기위해 사용하는 객체이다. 

Style세팅을 통해 날짜나 시간을 프리셋을 통하여 설정할수 있고

원하는 세팅이 없다면 dateFormat에서 직접 지정할 수 있다.

- style 세팅
    - dateStyle
        - none
        - short
        - medium
        - long
        - full
    - timeStyle
        - none
        - short
        - medium
        - long
        - full
- dateFormat 커스텀

## Convert

`string(from date: Date)` 함수는 Date타입을 String으로 반환한다.

`date(from string: String)` 함수는 String으로 들어온 것을 Date?로 반환한다.

Date에는 ?(물음표)가 있다. String의 format이 안 맞으면 `nil`로 반환한다.

### Date to String

들어온 Date타입을 String으로 바꾸기위해

dateformatter를 생성하여 dateFormat을 설정하고 String으로 변환한다.

```swift

let date = Date()

let dateformatter = DateFormatter()
dateformatter.dateStyle = .none
dateformatter.timeStyle = .short

//dateformatter.dateFormat = "a hh시 mm분"

let text = dateformatter.string(from: date)
```

### String to Date

1. String이 어떤 format으로 되어있는지 확인한다.

2. String을 Date로 변환한다.

3. Date를 내가 원하는 format으로 변경한다.

```swift
let dateStr = "2020-08-13 16:30" // Date 형태의 String
        
let dateFormatter = DateFormatter()
dateFormatter.dateFormat = "yyyy-MM-dd HH:mm" // 2020-08-13 16:30
        
let convertDate = dateFormatter.date(from: dateStr) // Date 타입으로 변환
        
let myDateFormatter = DateFormatter()
myDateFormatter.dateFormat = "yyyy년 MM월 dd일 a hh시 mm분" // 2020년 08월 13일 오후 04시 30분
myDateFormatter.locale = Locale(identifier:"ko_KR") // PM, AM을 언어에 맞게 setting (ex: PM -> 오후)
let convertStr = myDateFormatter.string(from: convertDate!)
```

## 참고

[https://formestory.tistory.com/6](https://formestory.tistory.com/6)
