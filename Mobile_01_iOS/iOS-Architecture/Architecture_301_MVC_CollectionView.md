# VC -> MVC : Custom UICollectionView

### 동작설명

아래 구조체가 있다.  
```swift
struct Student {
    var name: String
    var className: String
    var hasHomework: Bool
}

/*
Student(name: "Student 1", className: "Class A", hasHomework: false),
Student(name: "Student 2", className: "Class A", hasHomework: false),
...
*/
```

- 셀을 클릭하면 해당 셀에서 기본값이 false로 되어있는 hasHomework가 true로 변경


<br><br>

## 동작영상



<br><br>


## 예시코드 간결화 시키기

```swift
var students: [Student] = []

func generateDummyData() {
    for i in 1...20 {
        students.append(Student(name: "Student \(i)", className: "Class A", hasHomework: false))
    }
}

// 혹은 
var students: [Student] = (1...20).map { Student(name: "Student \($0)",
                                         className: "Class A",
                                         hasHomework: false) }
```

## 




<br><br>


# 📌 단일 ViewController
한 파일에서 전부 구현하였다. 


<br><br>

### 전체코드

<details><summary>예시 코드</summary>

```swift

```

</details>


<br><br>


# 📌 
한 파일에서 전부 구현하였다.   



<br><br>

### 전체코드

<details><summary>예시 코드</summary>

```swift

```

</details>


<br><br>


## History
- 230830 : 초안작성
