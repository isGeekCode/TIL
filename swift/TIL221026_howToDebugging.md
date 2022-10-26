Xcode 디버깅으로 변수변화 캐치하기

Xcode 디버깅 중 변수 변화 캐치하기: watch point

### watchpoint

- 디버깅 중에 변수값이 언제 어디서 바뀌는지 알고 싶을 때가 있다. 하지만 로직이 복잡할수록 어디서 변하는지 일일이 체크하기는 쉽지 않다.
- watchpoint는 변수값이 수정되는 곳에 일일이 breakpoint를 만들지 않아도 break가 걸리도록 해준다.
- 일단, 트래킹 하고 싶은 변수가 처음 생성되거나 사용하는 곳에 breakpoint를 걸어준다. (예제에서는 count라는 변수를 트래킹)

![10(1)](https://user-images.githubusercontent.com/76529148/197956797-c951f262-584d-41c3-accc-927d21014105.png)

앱 실행 후 break가 걸리면 아래 콘솔 왼쪽 화면에서 트래킹할 변수를 오른쪽 클릭하고 **"Watch {변수}"**를 클릭

![11(1)](https://user-images.githubusercontent.com/76529148/197956859-cdbd2135-db48-4c40-bf24-c9dc636c15f1.png)

이제 변수값이 수정되면, 수정하는 곳에 break가 걸리게 된다.

- Increase, Decrease 버튼으로 count 변수값을 바꿀 때마다 break가 걸리는 것을 볼 수 있다.
  ![12](https://user-images.githubusercontent.com/76529148/197956874-6d031e0f-8229-4ff1-add6-767309a87d5b.gif)

[출처](https://meetup.toast.com/posts/315)
