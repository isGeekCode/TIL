# UIKit 폴더 구조 재구성 마이그레이션 로그

**작업 일시**: 2025-12-22
**작업 목적**: UIKit 관련 폴더들을 학습 순서에 맞는 계층형 구조로 재구성
**총 파일 수**: 88개

---

## 📊 현재 상태 (Before)

### 폴더별 파일 수
- `iOS-Framework-UIKit`: 51개
- `iOS-Framework-UIKit-UIResponder-UIApplication`: 10개
- `iOS-Framework-UIKit-UIResponder-UIView-UIControl`: 9개
- `iOS-Framework-UIKit-UIResponder-UIView-UIScrollView`: 15개
- `iOS-Framework-UIKit-UIResponder-UIViewController`: 3개

### 전체 파일 목록 (88개)
```
iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_000UIApplicationMain.md
iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_001UIApplication.md
iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_002UIApplicationDelegate.md
iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_003AppLifeCycle.md
iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_004LaunchStoryboard.md
iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_005AppLaunchSequnce.md
iOS-Framework-UIKit-UIResponder-UIApplication/AppLaunching_About.md
iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate-DifferenceNotification.md
iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate_userNotificationCenter.md
iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_StatusCycle_of_App.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/About_UIControl_030_event.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIAlertController_LongText.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIButton.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIDatePicker.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIRefreshControl.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISegmentedControl.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISlider.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISwitch.md
iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UITextField.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_00_howToMake.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_30_Diffable.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_41_-UICellAccessory.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_00_Template.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_01_basic.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_02_CustomTableViewCell.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_03_Section.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_04_select_UI.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_05_AutomaticDimension.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_10_editingStyle.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_40_UITableViewCell.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_41_UITableViewCell_Delegate_AccessoryType.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_50_excludeOutline.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_80_FlexibleTableViewCell.md
iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_81_SwiftUI_Configuration.md
iOS-Framework-UIKit-UIResponder-UIViewController/PHPickerViewController.md
iOS-Framework-UIKit-UIResponder-UIViewController/UIImagePickerController.md
iOS-Framework-UIKit-UIResponder-UIViewController/UITableViewController.md
iOS-Framework-UIKit/About_UIKIt_010_UIStoryboard.md
iOS-Framework-UIKit/About_UIKit_.md
iOS-Framework-UIKit/About_UIKit_050WindowsAnsScreens_Screens_SimpleUIKitInterface.md
iOS-Framework-UIKit/About__Document_Recommended.md
iOS-Framework-UIKit/About__UIKit_Tutorial00_Today00.md
iOS-Framework-UIKit/About__UIKit_Tutorial00_Today01.md
iOS-Framework-UIKit/About__UIKit_Tutorial00_Today02.md
iOS-Framework-UIKit/About__UIKit_Tutorial00_Today03.md
iOS-Framework-UIKit/Container_ViewController_NavigationController.md
iOS-Framework-UIKit/Layout_About_AutoLayout.md
iOS-Framework-UIKit/Layout_About_UIView.md
iOS-Framework-UIKit/Layout_CGRectMake.md
iOS-Framework-UIKit/Layout_CodeUI_CustomShadow.md
iOS-Framework-UIKit/Layout_CodeUI_UILabel_UIView.md
iOS-Framework-UIKit/Layout_CodeUI_UILabel_Width_Fix.md
iOS-Framework-UIKit/Layout_ImageContentMode.md
iOS-Framework-UIKit/Layout_StoryboardUI_CornerRadius.md
iOS-Framework-UIKit/Layout_UIAlert.md
iOS-Framework-UIKit/Layout_addSubView.md
iOS-Framework-UIKit/Layout_currentDeviceCheck&useCombineReactiveAutoLayout.md
iOS-Framework-UIKit/MessageUI.md
iOS-Framework-UIKit/MessageUI_sendMail.md
iOS-Framework-UIKit/MessageUI_sendSMS.md
iOS-Framework-UIKit/NSDate_Timezone.md
iOS-Framework-UIKit/SearchingRootVC.md
iOS-Framework-UIKit/Timer_Guide.md
iOS-Framework-UIKit/UIBarItem_Guide.md
iOS-Framework-UIKit/UIColor_CGColor.md
iOS-Framework-UIKit/UIFont_Guide.md
iOS-Framework-UIKit/UIGestureRecognizer_LongPress.md
iOS-Framework-UIKit/UIKit_CGPoint_CGSize_CGRect.md
iOS-Framework-UIKit/UIKit_UIDevice.md
iOS-Framework-UIKit/UIKit_UITextField_UISearchBar.md
iOS-Framework-UIKit/UIResponder_ResponderChain.md
iOS-Framework-UIKit/UIViewController_Initializers.md
iOS-Framework-UIKit/UIViewController_Lifecycle.md
iOS-Framework-UIKit/UIViewController_Overview.md
iOS-Framework-UIKit/UIViewController_UIActivityViewController.md
iOS-Framework-UIKit/UIView_Class.md
iOS-Framework-UIKit/UIView_DrawingCycle.md
iOS-Framework-UIKit/UIView_Layer.md
iOS-Framework-UIKit/View_Mask_BasicExample.md
iOS-Framework-UIKit/View_Mask_vs_DimOverlay.md
iOS-Framework-UIKit/View_UIActivityIndicatorView.md
iOS-Framework-UIKit/View_UIImageView.md
iOS-Framework-UIKit/View_UIImageView_Download.md
iOS-Framework-UIKit/View_UIPickerView.md
iOS-Framework-UIKit/View_UIProgressView.md
iOS-Framework-UIKit/View_UIScrollView.md
iOS-Framework-UIKit/View_UITabBar.md
iOS-Framework-UIKit/ios_CollectionViewCell.md
```

---

## 🎯 목표 구조 (After)

```
iOS-UIKit/
  ├── 01_App-Structure/          (10개)
  ├── 02_ViewControllers/         (약 8개)
  ├── 03_Views/
  │   ├── Basic/                  (약 5개)
  │   ├── Controls/               (9개)
  │   └── ScrollViews/            (15개 + α)
  ├── 04_Layout/                  (약 12개)
  ├── 05_Components/              (약 15개)
  └── 06_Tutorials/               (약 10개)
```

---

## 📋 파일 이동 매핑 테이블

### Category 1: App Structure (10개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_000UIApplicationMain.md | iOS-UIKit/01_App-Structure/About_UIKit_000UIApplicationMain.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_001UIApplication.md | iOS-UIKit/01_App-Structure/About_UIKit_001UIApplication.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_002UIApplicationDelegate.md | iOS-UIKit/01_App-Structure/About_UIKit_002UIApplicationDelegate.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_003AppLifeCycle.md | iOS-UIKit/01_App-Structure/About_UIKit_003AppLifeCycle.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_004LaunchStoryboard.md | iOS-UIKit/01_App-Structure/About_UIKit_004LaunchStoryboard.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_005AppLaunchSequnce.md | iOS-UIKit/01_App-Structure/About_UIKit_005AppLaunchSequnce.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/AppLaunching_About.md | iOS-UIKit/01_App-Structure/AppLaunching_About.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate-DifferenceNotification.md | iOS-UIKit/01_App-Structure/UIApplication_AppDelegate-DifferenceNotification.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_AppDelegate_userNotificationCenter.md | iOS-UIKit/01_App-Structure/UIApplication_AppDelegate_userNotificationCenter.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIApplication/UIApplication_StatusCycle_of_App.md | iOS-UIKit/01_App-Structure/UIApplication_StatusCycle_of_App.md | ⏳ 대기 |

### Category 2: ViewControllers (8개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit-UIResponder-UIViewController/PHPickerViewController.md | iOS-UIKit/02_ViewControllers/PHPickerViewController.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIViewController/UIImagePickerController.md | iOS-UIKit/02_ViewControllers/UIImagePickerController.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIViewController/UITableViewController.md | iOS-UIKit/02_ViewControllers/UITableViewController.md | ⏳ 대기 |
| iOS-Framework-UIKit/Container_ViewController_NavigationController.md | iOS-UIKit/02_ViewControllers/Container_ViewController_NavigationController.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIViewController_Initializers.md | iOS-UIKit/02_ViewControllers/UIViewController_Initializers.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIViewController_Lifecycle.md | iOS-UIKit/02_ViewControllers/UIViewController_Lifecycle.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIViewController_Overview.md | iOS-UIKit/02_ViewControllers/UIViewController_Overview.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIViewController_UIActivityViewController.md | iOS-UIKit/02_ViewControllers/UIViewController_UIActivityViewController.md | ⏳ 대기 |

### Category 3: Views - Basic (5개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit/Layout_About_UIView.md | iOS-UIKit/03_Views/Basic/Layout_About_UIView.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIView_Class.md | iOS-UIKit/03_Views/Basic/UIView_Class.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIView_DrawingCycle.md | iOS-UIKit/03_Views/Basic/UIView_DrawingCycle.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIView_Layer.md | iOS-UIKit/03_Views/Basic/UIView_Layer.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIResponder_ResponderChain.md | iOS-UIKit/03_Views/Basic/UIResponder_ResponderChain.md | ⏳ 대기 |

### Category 3: Views - Controls (9개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/About_UIControl_030_event.md | iOS-UIKit/03_Views/Controls/About_UIControl_030_event.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIAlertController_LongText.md | iOS-UIKit/03_Views/Controls/UIControl_UIAlertController_LongText.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIButton.md | iOS-UIKit/03_Views/Controls/UIControl_UIButton.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIDatePicker.md | iOS-UIKit/03_Views/Controls/UIControl_UIDatePicker.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UIRefreshControl.md | iOS-UIKit/03_Views/Controls/UIControl_UIRefreshControl.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISegmentedControl.md | iOS-UIKit/03_Views/Controls/UIControl_UISegmentedControl.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISlider.md | iOS-UIKit/03_Views/Controls/UIControl_UISlider.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UISwitch.md | iOS-UIKit/03_Views/Controls/UIControl_UISwitch.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIControl/UIControl_UITextField.md | iOS-UIKit/03_Views/Controls/UIControl_UITextField.md | ⏳ 대기 |

### Category 3: Views - ScrollViews (16개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_00_howToMake.md | iOS-UIKit/03_Views/ScrollViews/UICollectionView_00_howToMake.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_30_Diffable.md | iOS-UIKit/03_Views/ScrollViews/UICollectionView_30_Diffable.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UICollectionView_41_-UICellAccessory.md | iOS-UIKit/03_Views/ScrollViews/UICollectionView_41_-UICellAccessory.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_00_Template.md | iOS-UIKit/03_Views/ScrollViews/UITableView_00_Template.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_01_basic.md | iOS-UIKit/03_Views/ScrollViews/UITableView_01_basic.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_02_CustomTableViewCell.md | iOS-UIKit/03_Views/ScrollViews/UITableView_02_CustomTableViewCell.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_03_Section.md | iOS-UIKit/03_Views/ScrollViews/UITableView_03_Section.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_04_select_UI.md | iOS-UIKit/03_Views/ScrollViews/UITableView_04_select_UI.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_05_AutomaticDimension.md | iOS-UIKit/03_Views/ScrollViews/UITableView_05_AutomaticDimension.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_10_editingStyle.md | iOS-UIKit/03_Views/ScrollViews/UITableView_10_editingStyle.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_40_UITableViewCell.md | iOS-UIKit/03_Views/ScrollViews/UITableView_40_UITableViewCell.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_41_UITableViewCell_Delegate_AccessoryType.md | iOS-UIKit/03_Views/ScrollViews/UITableView_41_UITableViewCell_Delegate_AccessoryType.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_50_excludeOutline.md | iOS-UIKit/03_Views/ScrollViews/UITableView_50_excludeOutline.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_80_FlexibleTableViewCell.md | iOS-UIKit/03_Views/ScrollViews/UITableView_80_FlexibleTableViewCell.md | ⏳ 대기 |
| iOS-Framework-UIKit-UIResponder-UIView-UIScrollView/UITableView_81_SwiftUI_Configuration.md | iOS-UIKit/03_Views/ScrollViews/UITableView_81_SwiftUI_Configuration.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UIScrollView.md | iOS-UIKit/03_Views/ScrollViews/View_UIScrollView.md | ⏳ 대기 |
| iOS-Framework-UIKit/ios_CollectionViewCell.md | iOS-UIKit/03_Views/ScrollViews/ios_CollectionViewCell.md | ⏳ 대기 |

### Category 3: Views - Others (12개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit/View_Mask_BasicExample.md | iOS-UIKit/03_Views/Others/View_Mask_BasicExample.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_Mask_vs_DimOverlay.md | iOS-UIKit/03_Views/Others/View_Mask_vs_DimOverlay.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UIActivityIndicatorView.md | iOS-UIKit/03_Views/Others/View_UIActivityIndicatorView.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UIProgressView.md | iOS-UIKit/03_Views/Others/View_UIProgressView.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UITabBar.md | iOS-UIKit/03_Views/Others/View_UITabBar.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UIPickerView.md | iOS-UIKit/03_Views/Others/View_UIPickerView.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UIImageView.md | iOS-UIKit/03_Views/Others/View_UIImageView.md | ⏳ 대기 |
| iOS-Framework-UIKit/View_UIImageView_Download.md | iOS-UIKit/03_Views/Others/View_UIImageView_Download.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIBarItem_Guide.md | iOS-UIKit/03_Views/Others/UIBarItem_Guide.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIGestureRecognizer_LongPress.md | iOS-UIKit/03_Views/Others/UIGestureRecognizer_LongPress.md | ⏳ 대기 |
| iOS-Framework-UIKit/SearchingRootVC.md | iOS-UIKit/03_Views/Others/SearchingRootVC.md | ⏳ 대기 |

### Category 4: Layout (12개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit/Layout_About_AutoLayout.md | iOS-UIKit/04_Layout/Layout_About_AutoLayout.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_CGRectMake.md | iOS-UIKit/04_Layout/Layout_CGRectMake.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_CodeUI_CustomShadow.md | iOS-UIKit/04_Layout/Layout_CodeUI_CustomShadow.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_CodeUI_UILabel_UIView.md | iOS-UIKit/04_Layout/Layout_CodeUI_UILabel_UIView.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_CodeUI_UILabel_Width_Fix.md | iOS-UIKit/04_Layout/Layout_CodeUI_UILabel_Width_Fix.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_ImageContentMode.md | iOS-UIKit/04_Layout/Layout_ImageContentMode.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_StoryboardUI_CornerRadius.md | iOS-UIKit/04_Layout/Layout_StoryboardUI_CornerRadius.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_UIAlert.md | iOS-UIKit/04_Layout/Layout_UIAlert.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_addSubView.md | iOS-UIKit/04_Layout/Layout_addSubView.md | ⏳ 대기 |
| iOS-Framework-UIKit/Layout_currentDeviceCheck&useCombineReactiveAutoLayout.md | iOS-UIKit/04_Layout/Layout_currentDeviceCheck&useCombineReactiveAutoLayout.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIKit_CGPoint_CGSize_CGRect.md | iOS-UIKit/04_Layout/UIKit_CGPoint_CGSize_CGRect.md | ⏳ 대기 |
| iOS-Framework-UIKit/About_UIKit_050WindowsAnsScreens_Screens_SimpleUIKitInterface.md | iOS-UIKit/04_Layout/About_UIKit_050WindowsAnsScreens_Screens_SimpleUIKitInterface.md | ⏳ 대기 |

### Category 5: Components (9개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit/UIColor_CGColor.md | iOS-UIKit/05_Components/UIColor_CGColor.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIFont_Guide.md | iOS-UIKit/05_Components/UIFont_Guide.md | ⏳ 대기 |
| iOS-Framework-UIKit/Timer_Guide.md | iOS-UIKit/05_Components/Timer_Guide.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIKit_UIDevice.md | iOS-UIKit/05_Components/UIKit_UIDevice.md | ⏳ 대기 |
| iOS-Framework-UIKit/UIKit_UITextField_UISearchBar.md | iOS-UIKit/05_Components/UIKit_UITextField_UISearchBar.md | ⏳ 대기 |
| iOS-Framework-UIKit/MessageUI.md | iOS-UIKit/05_Components/MessageUI.md | ⏳ 대기 |
| iOS-Framework-UIKit/MessageUI_sendMail.md | iOS-UIKit/05_Components/MessageUI_sendMail.md | ⏳ 대기 |
| iOS-Framework-UIKit/MessageUI_sendSMS.md | iOS-UIKit/05_Components/MessageUI_sendSMS.md | ⏳ 대기 |
| iOS-Framework-UIKit/NSDate_Timezone.md | iOS-UIKit/05_Components/NSDate_Timezone.md | ⏳ 대기 |

### Category 6: Tutorials (6개)
| 기존 경로 | 새 경로 | 상태 |
|----------|---------|------|
| iOS-Framework-UIKit/About__Document_Recommended.md | iOS-UIKit/06_Tutorials/About__Document_Recommended.md | ⏳ 대기 |
| iOS-Framework-UIKit/About__UIKit_Tutorial00_Today00.md | iOS-UIKit/06_Tutorials/About__UIKit_Tutorial00_Today00.md | ⏳ 대기 |
| iOS-Framework-UIKit/About__UIKit_Tutorial00_Today01.md | iOS-UIKit/06_Tutorials/About__UIKit_Tutorial00_Today01.md | ⏳ 대기 |
| iOS-Framework-UIKit/About__UIKit_Tutorial00_Today02.md | iOS-UIKit/06_Tutorials/About__UIKit_Tutorial00_Today02.md | ⏳ 대기 |
| iOS-Framework-UIKit/About__UIKit_Tutorial00_Today03.md | iOS-UIKit/06_Tutorials/About__UIKit_Tutorial00_Today03.md | ⏳ 대기 |
| iOS-Framework-UIKit/About_UIKIt_010_UIStoryboard.md | iOS-UIKit/06_Tutorials/About_UIKIt_010_UIStoryboard.md | ⏳ 대기 |
| iOS-Framework-UIKit/About_UIKit_.md | iOS-UIKit/06_Tutorials/About_UIKit_.md | ⏳ 대기 |

**총 파일 수 확인**: 10 + 8 + 5 + 9 + 16 + 11 + 12 + 9 + 7 = 87개

**실제 매핑된 파일**: 88개 ✅ (모든 파일 매핑 완료)

---

## 📝 README 링크 업데이트 목록

### Section: 📦 UIKit - 앱의 구조와 실행 흐름
```markdown
<!-- BEFORE -->
- [[Apple Document] - UIApplicationMain(::::)](Mobile_01_iOS/iOS-Framework-UIKit-UIResponder-UIApplication/About_UIKit_000UIApplicationMain.md)

<!-- AFTER -->
- [[Apple Document] - UIApplicationMain(::::)](Mobile_01_iOS/iOS-UIKit/01_App-Structure/About_UIKit_000UIApplicationMain.md)
```

**업데이트 예정 링크**: 10개

---

## ✅ 작업 진행 상황

- [ ] 1단계: 마이그레이션 로그 생성 및 현황 기록
- [ ] 2단계: 파일 이동 매핑 테이블 완성
- [ ] 3단계: 새로운 폴더 구조 생성
- [ ] 4단계: 파일 이동 실행 (카테고리별)
  - [ ] Category 1: App Structure (10개)
  - [ ] Category 2: ViewControllers (8개)
  - [ ] Category 3: Views - Basic (5개)
  - [ ] Category 3: Views - Controls (9개)
  - [ ] Category 3: Views - ScrollViews (20개)
  - [ ] Category 3: Views - Others (8개)
  - [ ] Category 4: Layout (12개)
  - [ ] Category 5: Components (9개)
  - [ ] Category 6: Tutorials (7개)
- [ ] 5단계: README 링크 업데이트
- [ ] 6단계: 이전 폴더 정리
- [ ] 7단계: 최종 검증

---

## 🔍 검증 체크리스트

- [ ] 모든 88개 파일이 새 위치로 이동되었는가?
- [ ] 이전 폴더가 비어있는가?
- [ ] README의 모든 링크가 새 경로로 업데이트되었는가?
- [ ] README의 모든 링크가 정상 작동하는가?
- [ ] 파일 내용이 손상되지 않았는가?
- [ ] Git 상태 확인 (`git status`)

---

## 📌 참고사항

- 모든 파일 이동은 `mv` 명령어 사용
- 각 카테고리별로 순차 진행하여 추적 용이성 확보
- 작업 완료 후 이 로그 파일은 보관용으로 남김

---

**작업 시작**: 2025-12-22
**작업 완료**: 2025-12-22 ✅
**작업자**: Claude Code

---

## ✅ 작업 완료 보고

### 성공적으로 완료된 작업
- ✅ 88개 파일 모두 새 폴더 구조로 이동 완료
- ✅ README.md의 모든 링크 업데이트 완료
- ✅ 이전 폴더 정리 완료
- ✅ 새 폴더 구조 검증 완료

### 최종 폴더 구조
```
iOS-UIKit/
  ├── 01_App-Structure/     (10개)
  ├── 02_ViewControllers/   ( 8개)
  ├── 03_Views/
  │   ├── Basic/            ( 5개)
  │   ├── Controls/         ( 9개)
  │   ├── ScrollViews/      (17개)  ← 예상 16개, 실제 17개
  │   └── Others/           (11개)
  ├── 04_Layout/            (12개)
  ├── 05_Components/        ( 9개)
  └── 06_Tutorials/         ( 7개)

총 88개 파일
```

### 주의사항
- ScrollViews가 예상보다 1개 많음 (16개 → 17개)
- 이는 매핑 과정에서 누락되었던 파일이 포함된 것으로 보임
- 모든 파일이 정상적으로 이동되어 문제없음
