# NSObject_UIResponder_UIView_UIScrollView_UITableView : 셀 클릭시 높이가 변경되는 테이블뷰



```swift
//
//  testViewController.swift
//  SwiftApp
//
//  Created by bang_hyeonseok on 2023/05/26.
//

import Foundation

import UIKit

class MyTableViewController: UITableViewController {
    var selectedRowIndex: Int?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.delegate = self
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let selectedRowIndex = selectedRowIndex, selectedRowIndex == indexPath.row {
            self.selectedRowIndex = nil
        } else {
            self.selectedRowIndex = indexPath.row
        }
        
        let indexPathsToReload = [indexPath, IndexPath(row: indexPath.row - 1, section: indexPath.section), IndexPath(row: indexPath.row + 1, section: indexPath.section)].filter {
            $0.row >= 0 && $0.row < tableView.numberOfRows(inSection: $0.section)
        }
        tableView.reloadRows(at: indexPathsToReload, with: .automatic)
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        if let selectedRowIndex = selectedRowIndex, indexPath.row == selectedRowIndex {
            return 100.0
        } else {
            return 50.0
        }
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = "Row \(indexPath.row + 1)"
        return cell
    }
}

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let tableViewController = MyTableViewController()
        tableViewController.tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
        
        addChild(tableViewController)
        view.addSubview(tableViewController.tableView)
        tableViewController.tableView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            tableViewController.tableView.topAnchor.constraint(equalTo: view.topAnchor),
            tableViewController.tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableViewController.tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            tableViewController.tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
        tableViewController.didMove(toParent: self)
    }
}

```
