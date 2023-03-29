# 마크다운 - HTML사용하기

가끔 마크다운문법만으로는 구현할 수 없는 상황이 생긴다.

Markdown을 사용하는 경우 HTML 태그를 사용하여 텍스트를 스타일링할 수 있다. 예를 들어, 텍스트를 가운데 정렬하려면 <center> 태그를 사용할 수 있다.

다만 일반적으로 마크다운에서 HTML을 사용하는 것은 권장되지않는다고 한다.

이유는 일부 Markdown 에디터에서 HTML 태그를 지원하지 않아 의도한 대로 문서가 표시되지 않을 수 있기 때문.

Markdown은 HTML의 대체품이 아니며, 매우 작은 일부 HTML 태그에 해당하는 작은 문법 집합만을 제공한다.


## 텍스트 가운데 정렬

## 기존 사용
```
- 이미지 출처 : [핀터레스트](https://i.pinimg.com/564x/16/22/31/162231131a07dda331e720811b87f9d8.jpg)

```
- 이미지 출처 : [핀터레스트](https://i.pinimg.com/564x/16/22/31/162231131a07dda331e720811b87f9d8.jpg)


### 텍스트만 가운데 정렬하기

```
<p align="center">이미지 출처 : 핀터레스트</p>
```
<p align="center">이미지 출처 : 핀터레스트</p>


### 하이퍼링크를 포함한 텍스트를 가운데 정렬하기 

```
<p align="center">
    <a href="https://i.pinimg.com/564x/16/22/31/162231131a07dda331e720811b87f9d8.jpg" style="text-align: center;">이미지 출처 : 핀터레스트</a>
</p>

```

<p align="center">
    <a href="https://i.pinimg.com/564x/16/22/31/162231131a07dda331e720811b87f9d8.jpg" style="text-align: center;">이미지 출처 : 핀터레스트</a>
</p>

## 참고문서
- [Markdown Guide](https://www.markdownguide.org/extended-syntax/#html)
