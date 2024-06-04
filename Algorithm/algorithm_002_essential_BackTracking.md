# 필수 알고리즘 - 백트래킹
백트래킹은 "되돌아가기"라는 뜻을 가진 단어로,로 찾기 게임을 할 때 막다른 길에 다다랐을 때, 다시 돌아가서 새로운 길을 찾아보는 것과 비슷하다.  
우리가 숫자로 특별한 수열을 만들어야 할 때, 백트래킹을 사용해서 모든 가능한 조합을 찾아볼 수 있다.

## 문제 상황 설명
예를 들어, 우리에게 1, 2, 3의 숫자가 있고, 이 중에서 2개의 숫자로 수열을 만들어야 한다고 해 보자.  
가능한 모든 조합을 찾아내려면, 각 숫자가 시작점이 될 차례를 주고, 다음 숫자를 고르는 식으로 진행하면 된다.  

## 백트래킹 과정
- 숫자 선택하기: 첫 번째 숫자로 1을 선택
- 다음 숫자 고르기: 1을 고른 후, 다음 숫자로 2를 고를 수 있다.  

이제 1과 2로 수열을 하나 완성했다. 이 수열은 "1 2"다.

- 돌아가서 다른 수 시도하기: "1 2"를 만들고 나면, 다른 조합도 만들어 봐야 하니까, 다시 1로 돌아가서 다음 숫자인 3을 선택한다.  
그러면 "1 3"이라는 새 수열을 만들 수 있다. 

- 다른 숫자로 시작하기: 이제 1로 시작하는 조합은 다 찾았으니, 2로 시작하는 수열을 생성한다.  
"2 1", "2 3" 이렇게 만들 수 있고, 마찬가지로 3으로 시작해서 "3 1", "3 2"를 만든다.


### 왜 다시 false로 바꾸고 숫자를 지울까?
각 숫자를 사용했다는 표시를 해 두었다가, 다른 조합을 시도할 때는 그 표시를 지워야 한다.  
그래야만 다른 조합을 자유롭게 만들 수 있다.  
이렇게 표시를 지우고 다시 시도하는 것을 "백트래킹"이라고 한다. 

예시: "1 2"를 만든 후에는 2의 사용 표시를 지워야 한다.  그래야 "1 3"을 만들 때 2를 사용할 수 있다. 

### 결론
백트래킹을 이해하는 것은 마치 크레용으로 그림을 그리다가 지우개로 지우고 다시 다른 색을 칠하는 것과 비슷하다.  
모든 색을 사용해 보고 가장 예쁜 그림을 찾는 것처럼, 백트래킹도 모든 숫자의 조합을 시도해 보며 문제의 답을 찾아가는 과정이다.   




## 사용하는 경우
모든 경우의 수를 확인해야할 때 사용한다. 

- 백트래킹은 N이 10언저리만 가능하기 때문에 문제에서 힌트를 얻을 수 있다.


ex) 순열
m개의 숫자중 n개의 숫자를 뽑을 때, 상관이 있는것
3개의 숫자 중 2개의 숫자를 뽑는것
1, 2
1, 3
2, 1
2, 3
3, 1
3, 2

### For Loop로 사용 가능한가?
For Loop로 확인불가한 경우에 사용한다.

for로 확인이 가능하긴 하다.

ex) 

```swift
for i in 1...3 {
    // x 를 선택했다면
    for j in 1...3 {
        // 여기선 x를 제외해야한다.
    }
}
```
깊이가 깊어지게 되면.. 복잡해지기 때문에 안된다.


## 구동 방식
트리라고 생각해보자
<img width="507" alt="스크린샷 2024-06-02 오후 11 34 17" src="https://github.com/isGeekCode/TIL/assets/76529148/a33e409d-6433-4409-a1b3-8f5f84a60b8d">

각 분기점을 만나는 것이 재귀함수 한번의 동작이다. 
```swfit
func recur(num: Int) {

    // 재귀는 항상 끝나는 시점을 정해야한다.
    if num == n {
        return 
    }

    for i in 0..<n {
        // 결과값 추가
        recur(num)
    }
}
```

## 기본 문제 
백준 15649 : N과 M(1)

- 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)


### 아이디어
- For Loop
    - 1...n 까지에서 1개 선택
    - 결과값에 추가
    - 재귀함수 (num + 1)
        Foor Loop
        - 방문여부 체크

- 재귀함수는 항상 끝나는 조건을 생각할 것

## 시간복잡도
- 중복이 가능한 경우 : N의 N제곱 -> N이 8까지 가능
- 중복이 불가한 경우 : N!      -> N이 10까지 가능

백트래킹은 N이 10언저리만 가능하기 때문에 문제에서 힌트를 얻을 수 있다.

## 자료구조
- 방문여부 배열 : [Bool]
- 선택값 배열 : [Int]