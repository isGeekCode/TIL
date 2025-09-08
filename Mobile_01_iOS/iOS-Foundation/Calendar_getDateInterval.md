# Calendar - 캘린더로 두 개의 날짜 비교하기


### 코드보기
```swift

/// 현재 날짜를 저장
static public func saveCurrentDate() {
    let calendar = Calendar.current
    let currentDateComponents = calendar.dateComponents([.year, .month, .day], from: Date())
    if let currentDate = calendar.date(from: currentDateComponents) {
        UserDefaults.standard.set(currentDate, forKey: "SavedDate")
    }
}

/// 저장된 날짜를 체크하고 오늘이면 false , 오늘기록이 아니면 true
static public func checkDateRecord(completion: @escaping (Bool) -> Void) {
    if let savedDate = UserDefaults.standard.object(forKey: "SavedDate") as? Date {
        // 저장된 날짜를 가져옵니다.
        let calendar = Calendar.current
        let currentDateComponents = calendar.dateComponents([.year, .month, .day], from: Date())
        let savedDateComponents = calendar.dateComponents([.year, .month, .day], from: savedDate)
        
        
        if currentDateComponents.year == savedDateComponents.year &&
            currentDateComponents.month == savedDateComponents.month &&
            currentDateComponents.day == savedDateComponents.day {
            // 날짜가 같으면 completion handler에 false를 반환합니다.
            completion(false)
        } else {
            // 날짜가 다르면 completion handler에 true를 반환합니다.
            completion(true)
        }
    } else {
        // 저장된 날짜가 없으면, completion handler에 false를 반환합니다.
        completion(false)
    }
}
```


### 사용방법
```
checkDateRecord { isNotTodayRecord in
    if isNotTodayRecord {
        print("기록이 오늘이 아님")
    } else {
        print("오늘기록이거나 기록 없거나")
    }
}

```
