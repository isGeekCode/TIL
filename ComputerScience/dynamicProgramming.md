# Dynamic Programming (DP): 동적프로그래밍


```swift
//func fibo(_ n: Int) -> Int {
//    if n <= 1 { return n }
//    return fibo(n - 1) + fibo(n - 2)
//}

/*
 fibo(2) = fibo(1) + fibo(0) = 1 + 0 = 1
 fibo(3) = fibo(2) + fibo(1) = 1 + 1 = 2
 fibo(4) = fibo(3) + fibo(2) = 2 + 1 = 3
 fibo(5) = fibo(4) + fibo(3) = 3 + 2 = 5
 fibo(6) = fibo(5) + fibo(4) = 5 + 3 = 8
 fibo(7) = fibo(6) + fibo(5) = 8 + 5 = 13
 */

func fibo(_ n: Int) -> Int {
    var cache: [Int] = [0, 1]
    
    for num in 2 ... n {
        let this = cache[num - 1] + cache[num - 2]
        cache.append(this)
    }
    // cache배열 완성
    return cache[n]
}

fibo(6)

```
