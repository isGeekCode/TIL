# UITableView - 셀 경계선 없는 테이블뷰


## 셀경계선 없애기

Separator는 셀과 셀 사이에 있는 선을 말하고, 셀을 시각적으로 구분하기 위해 사용한다. 
###SeparatorStyle
- none: 선을 표지하지 않거나 커스텀 separator를 위해 사용
- default, single line: 선을 하나만 표시
- single line etched: 지금은 더 이상 사용하지 않는다.

```
    tableView.separatorStyle = .none
```
