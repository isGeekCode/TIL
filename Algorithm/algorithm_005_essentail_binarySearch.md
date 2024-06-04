# 필수 알고리즘 - 이진탐색 (Binary Search)

어떤 값을 찾을 때 정렬의 특징을 이용해 빨리 찾음
- 정렬이 되어있을 경우, 어떤 값을 찾을 때 ::: O(N) ->> O(lgN)
- 처음부터 생각하기 어려움.. 
- 시간 복잡도를 따져보고 시간이 초과하는 거라면 이진탐색을 떠올리도록 한다.  

## 시간 복잡도 
N개의 수 정렬 ::: `O(NlgN)`
M개의 수 이진 탐색::: `O(M * lgN)`


## 이진탐색의 느낌

N개의 숫자가 있을 때,A라는 숫자를 찾으려면

만약 전체를 계산하는 거라면 `for 0..<n` 의 비교를 하게 되는 것이다.   
### 이진 탐색
- 전체의 배열을 정렬
- 전체를 반으로 분할하여 해당 위치의 숫자와 찾을 숫자 A와 비교한다.  
- 만약 못찾으면 나머지 부분에서 또 절반을 나누어서 숫자 A와 비교한다. 

### 다른 예시
1,2,3,4  라는 4개의 수가 있고 거기서 3을 찾으려고 한다. 

가장 먼저 떠올릴 수 있는 for문으로 4개를 모두 탐색하면 O(N) = 4
먼저 절반을 나누어 작은 수가 2가 나오고, 2보다 3이 크기 때문에  다음 남은 우측을 또 반을 쪼개서 작은 수가 3인것을 찾음 O(lgN) = 2


<br><br>

### 코드로 보는 예제

두개의 입력을 받을 예정이다. 
찾을 숫자는 4이고 
1부터 6까지 총 6개의 숫자의 배열에서 4를 찾는 과정이다.  

```swift
let input2 = """
            4
            1 2 3 4 5 6
            """


let input3 = input2.split(separator: "\n")
let target = Int(input3[0])!
let arr = input3[1].split(separator: " ").map{ Int(String($0))!}
let (st, en) = (arr.first!, arr.last!)
binarySearch(st, en, target)

func binarySearch(_ start: Int, _ end: Int, _ target: Int) {
    if start == end {
        print(start)
        return
    }
    
    let mid = (start + end) / 2
    if arr[mid] < target {
        binarySearch(mid+1, end, target)
    } else {
        binarySearch(start, mid, target)
    }
}

```

이 부분에서 binarySearch의 기본 골조는 아래와 같다.  


```swift
func binarySearch(_ start: Int, _ end: Int, _ target: Int) {
    if start == end {
        print(start)
        return
    }
    
    let mid = (start + end) / 2
    if arr[mid] < target {
        binarySearch(mid+1, end, target)
    } else {
        binarySearch(start, mid, target)
    }
}

```

## 기본 문제
백준 1920
