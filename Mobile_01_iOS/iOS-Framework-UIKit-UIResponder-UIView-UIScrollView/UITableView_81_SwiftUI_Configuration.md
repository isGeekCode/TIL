# NSObject_UIResponder_UIView_UIScrollView_UITableView : SwiftUI로 셀 구현하기



기본적으로 UITableView에는 UITableViewCell 만 사용할 수있다.

그래서 이 셀 내부에 UIHostingViewController 역할을 하는  UIHostingConfiguration을 사용하여 구현할 수 있다. 

```swift

  
import UIKit
import SwiftUI
  
class ViewController: UIViewController {

    let CellIdentifier = "CellIdentifier"
    let products = ["Apple", "Banana", "Orange", "Pineapple", "Mango",
                    "Kiwi", "Strawberry", "Blueberry", "Blackberry", "Peach"]
  

    lazy var tableView: UITableView = {
        let t = UITableView()
        t.delegate = self
        t.dataSource = self
        t.register(UITableViewCell.self, forCellReuseIdentifier: CellIdentifier)
        t.translatesAutoresizingMaskIntoConstraints = false
        return t
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(tableView)
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
        ])
        tableView.backgroundColor = .systemYellow
    }
}

  

extension ViewController: UITableViewDelegate, UITableViewDataSource {

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return products.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let cell = tableView.dequeueReusableCell(
            withIdentifier: CellIdentifier,
            for: indexPath
        )
        let product = self.products[indexPath.row]
        
        // ✅ UIHosting 처리
        cell.contentConfiguration = UIHostingConfiguration {
            HStack {
                Text(product)
                    .font(.headline)
                Spacer()
                Button("Add to cart") {
                    print("add to cart")
                }
            }
            .swipeActions {
                Button(
                    role: .destructive
                ) {
                    print(**#function**)
                } label: {
                    Label("Delete", systemImage: "trash")
                }
            }
        }
        return cell
    }
}

  

  

import SwiftUI

struct ViewControllerPreview: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> ViewController {
        return ViewController()
    }
    func updateUIViewController(_ uiViewController: ViewController, context: Context) { }
}

struct ViewController_Preview: PreviewProvider {
    static var previews: some View {
        ViewControllerPreview()
    }
}

```

![|325](https://i.imgur.com/wPWmj8s.png)



이번엔 셀을 분리해보자.



```swift
import UIKit
import SwiftUI
  

class ViewController: UIViewController {
  
    let CellIdentifier = "CellIdentifier"
    let products = ["Apple", "Banana", "Orange", "Pineapple", "Mango",
                    "Kiwi", "Strawberry", "Blueberry", "Blackberry", "Peach"]


    lazy var tableView: UITableView = {
        let t = UITableView()
        t.delegate = self
        t.dataSource = self
        t.register(ProductCell.self, forCellReuseIdentifier: ProductCell.identifier) // ✅ 커스텀 셀 등록
        t.translatesAutoresizingMaskIntoConstraints = false
        return t

    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(tableView)
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
        ])
        tableView.backgroundColor = .systemYellow
    }

}

  

extension ViewController: UITableViewDelegate, UITableViewDataSource {

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return products.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    
        guard let cell = tableView.dequeueReusableCell(withIdentifier: ProductCell.identifier, for: indexPath) as? ProductCell else {
            return UITableViewCell()
        }
        cell.configure(with: products[indexPath.row]) // ✅ 제품 정보 설정
        return cell
    }
}

  
import UIKit
import SwiftUI

class ProductCell: UITableViewCell {

    static let identifier = "ProductCell"

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // 기존 UI그대로 
    func configure(with product: String) {
        contentConfiguration = UIHostingConfiguration {
            HStack {
                Text(product)
                    .font(.headline)
                Spacer()
                Button("Add to cart") {
                    print("add to cart")
                }
            }
            .swipeActions {
                Button(
                    role: .destructive
                ) {
                    print(**#function**)
                } label: {
                    Label("Delete", systemImage: "trash")
                }
            }
        }
    }

    private func setupUI() {
        selectionStyle = .none  // 셀 선택 효과 제거
    }

}
```



이번엔 셀을 SwfitUI로 구현하는 경우


```swift

import SwiftUI

struct ProductRowView: View {

    let product: String

    var body: some View {
        HStack {
            Text(product)
                .font(.headline)
            Spacer()
            Button("Add to cart") {
                print("add to cart")
            }
            .padding()
        }
        .swipeActions {
            Button(
                role: .destructive
            ) {
                print(#function)
            } label: {
                Label("Delete", systemImage: "trash")
            }
        }
    }
}

// VC는 그대로 유지

  
import UIKit
import SwiftUI
  

class ProductCell: UITableViewCell {

    static let identifier = "ProductCell"
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {

        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    func configure(with product: String) {
        contentConfiguration = UIHostingConfiguration {
            ProductRowView(product: product) // ✅ SwiftUI 뷰를 로드
        }
    }
    
    private func setupUI() {
        selectionStyle = .none  // 셀 선택 효과 제거
    }
}
```

<br><br>

---
## History
250304 : 초안 및 예제 작성
