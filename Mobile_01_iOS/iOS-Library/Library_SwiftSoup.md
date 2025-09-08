# 라이브러리 - swiftSoup

## 세팅

```swift
let urlString = "https://www.serveq.co.kr/recipe/BAK/recipe_view?R_IDX=1417&PAGESIZE=12&SORTCOL=&SORTDIR=&SEL_R_CATE_CODE=BAK001&SEARCH_COL=&SEARCH_KEYWORD="
guard let url = URL(string: urlString) else { return }

do {
    //  크롤링하는 부분
    let webString = try String(contentsOf: url)
  let document = try SwiftSoup.parse(webString)
    
} catch{
    print("error: \(error.localizedDescription)")
}
```

## element

element타입

## select

- element를 리턴한다.

개발자도구에서 선택자를 복사하면 아래의 경로를 가져올 수 있다.

`#a-page > section > div.empty-view > div.empty-view__text-container > p.a-spacing-large`

위 경로를 정리하면 이렇게 될것이다. 

`#a-page > section > div > div > p`

 이 경로를 가지고 아래와 같이 `select()` 함수 안에 경로를 넣어 사용할 수 있다.

하지만 이 구조에 반드시 하나만 있지않을 수 있다. 그래서 이걸 배열에 넣고 확인한 다음, 원하는 값을 특정하여 `text()`함수로 파싱한다. 

### 한번에 이어서 입력하기

```swift
let elementArray = try document.select("#a-page > section > div > div > p").array()
let text = try elementArray.first?.text()
print("elementArray: \(elementArray)")
print("text: \(text)")

```

하나씩 분리하기

```swift
let elementArray = try document.select("#a-page").select("section").select("div").select("div").select("p").array()
let text = try elementArray.first?.text()
print("elementArray: \(elementArray)")
print("text: \(text)")
```

## getElementByClass()

- element를 리턴한다.

### 특정 클래스 지정하고 하위 element 입력하기

`#a-page > section > div.empty-view > div.empty-view__text-container > p.a-spacing-large`

첫 div의 클래스명이 empty-view라서 특정할 수 가 있다. 그리고 하위는 동일하게 타고 들어간다. 

```swift
let elementArray = try document.getElementsByClass("empty-view").select("div").select("p").array()
let text = try elementArray.first?.text()
print("elementArray: \(elementArray)")
print("text: \(text)")
```

### 특정클래스 지정하고 하위 element 이어서 입력하기

```swift
let elementArray = try document.getElementsByClass("empty-view").select("div > p").array()
```

# tagName()

태그명으로 가져오기

```swift
let elementArray = try document.tagName("empty-view").select("div > p").array()
```

이밖에도  아래 링크에서 **Description ( 설명 )** 부분에서  다양하게 element를 선택할 수 있도록 제공하고 있다.

[https://github.com/scinfu/SwiftSoup](https://github.com/scinfu/SwiftSoup)

# 함수 분리하여 switch문에서 처리하기

## 1. 함수 세팅하기

크롤링을 할때 먼저 document를 가지고 element를 만들어사용하기때문에  크롤링할 것이 많은경우 최대한 재사용을 하는 방향으로 세팅하였다.

```swift
/// 입력된 document에서  입력된 경로의 text값을 크롤링하여 completion에 담는 함수.
    /// - Parameters:
    ///   - className: 클래스명으로 찾는 경우사용. 어레이에 하위경로를 담을 경우, 하위경로를 배열의 1번에 넣는다
    ///   - htmlPath: 셀렉터로만 찾는 경우 경로를 어레이에 담아 사용
func getString(document: Document, className: String? = "", htmlPath: String? = "", pageType currentPageType: PageType, completion: @escaping([Element]) -> ()) {
        guard let htmlPath = htmlPath,
              let className = className else { return }

        var arr = [Element]()

        do {
            if !htmlPath.isEmpty {
                print("htmlPath")
                arr = try document.select(htmlPath).array()
            }

            if !className.isEmpty {
                print("className")
                let classArray = className.components(separatedBy: "/")
                if classArray.count == 1 {
                    arr = try document.getElementsByClass(classArray[0]).array()
                } else {
                    arr = try document.getElementsByClass(classArray[0]).select(classArray[1]).array()
                }
            }

            print("크롤링 Array Value: \(arr)")
            completion(arr)

        }catch {
            print("error: \(error.localizedDescription)")
        }
    }

```

## 2. Path만들기

해당 함수에서는 3가지의 경우가 있다. 예시에 따라 path를 다르게 구성한다. 

- 사용하려는 클래스명 하나로 원하는 정보를 캐치할 수 있을 때
    - `pt-status-main-status` 이라는 클래스안에 들어있는 값
    - `path = "pt-status-main-status"`  를 className 파라미터에 넣는다.

- 특정 클래스와 그의 하위 경로 의 형태로 원하는 정보를 캐치할 수 있을 때
    - `empty-view` 라는 클래스안에 div 안에 p에 들어있는 값일때
    - `path = "empty-view/div > p"` 를 className 파라미터에 넣는다.

- 오로지 경로로만 원하는 정보를 캐치할 수 있을 때
    - #a-page 안에 section 안에 div 안에 div 안에 p에 들어있는 값일때
    - `path = “#a-page > section > div > div > p”`를 htmlPath 파라미터에 넣는다.

## 3. getString함수안에서 구현한 Completion으로 데이터 가공

getString에서는 타겟 텍스트가 들어있는 정보가 담긴 Element Array를 Completion으로 담아 내보낸다. 

그럼 해당 어레이안의 element를 text()로 변환하여 아래와 같이 사용한다.

 

```swift
  path = "pt-status-main-status"
  getString(document: doc, className: path, pageType: currentPageType) { arr in
          do {
              guard let text =  try arr.first?.text() else { return }
              Dprint("사용하려는 텍스트: \(text)")
          } catch {
              print("error: \(error.localizedDescription)")
          }
  }

```

## 4. 함수 사용하기

```swift
func crawlingStart() {

        guard let mainWebString = mainWebView.url?.absoluteString,
                            let url = URL(string: mainWebString ) else { return }

        var path = ""
        
        do {
            let webString = try String(contentsOf: url)
            let doc = try SwiftSoup.parse(webString)

            switch currentPageType {

                                case .trackPackage:

                        print("\(currentPageType)")
        
// MARK: 1. 사용하려는 클래스명 하나로 특정될 때 path를 구성하여 className에 담는다. 
                        path = "pt-status-main-status"
                        getString(document: doc, className: path, pageType: currentPageType) { arr in
                                do {
                                    guard let text =  try arr.first?.text() else { return }
                                    Dprint("사용하려는 텍스트: \(text)")
                                } catch {
                                    print("error: \(error.localizedDescription)")
                                }
                        }

                            case .otherPage:

// MARK: 2. 특정 클래스 / 하위 경로 의 형태로 path를 구성하여 className에 담는다.
                        path = "empty-view/div > p"
                        getString(document: doc, className: path, pageType: currentPageType) { arr in
                            do {
                                guard let text =  try arr.first?.text() else { return }
                                print("사용하려는 텍스트:: \(text)")
                            } catch {
                                print("error: \(error.localizedDescription)")
                            }
                        }
                                
// MARK: 3. // 경로로만 특정해야할 경우 path를 구성하여 htmlPath에 담는다. 
                        path = "#a-page > section > div > div > p"
                        getString(document: doc, htmlPath: path, pageType: currentPageType) { arr in
                            do {
                                guard let text =  try arr.first?.text() else { return }
                                print("사용하려는 텍스트:: \(text)")
                            } catch {
                                print("error: \(error.localizedDescription)")
                            }
                        }
                        
                        }

```
