# iOS_Hierachy - UIKit

UIKit은 사용자 인터페이스(UI)를 구축하고 관리하는 데 필요한 클래스와 기능을 제공하는 프레임워크다.

주로 iOS 앱 개발에 사용되며, 화면에 표시되는 버튼, 레이블, 텍스트 필드, 테이블 뷰 등의 UI 요소를 생성하고, 이벤트 처리, 애니메이션, 화면 전환 등을 다루는 데 사용된다.

UIKit은 Foundation과 같이 앱 개발에 필수적인 프레임워크 중 하나이며, Foundation과 함께 iOS 앱의 기반을 이루는 역할을 한다.




### 위치

UIKit 프레임워크는 아래 경로에 위치해 있다.

```
/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/System/Library/Frameworks/UIKit.framework
```



### Tree
```swift
├── Headers
│   ├── DocumentManager.h
│   ├── NSAttributedString.h
│   ├── NSDataAsset.h
│   ├── NSDiffableDataSourceSectionSnapshot.h
│   ├── NSFileProviderExtension.h
│   ├── NSIndexPath+UIKitAdditions.h
│   ├── NSItemProvider+UIKitAdditions.h
│   ├── NSLayoutAnchor.h
│   ├── NSLayoutConstraint.h
│   ├── NSLayoutManager.h
│   ├── NSParagraphStyle.h
│   ├── NSShadow.h
│   ├── NSStringDrawing.h
│   ├── NSText.h
│   ├── NSTextAttachment.h
│   ├── NSTextContainer.h
│   ├── NSTextContentManager.h
│   ├── NSTextElement.h
│   ├── NSTextLayoutFragment.h
│   ├── NSTextLayoutManager.h
│   ├── NSTextLineFragment.h
│   ├── NSTextList.h
│   ├── NSTextListElement.h
│   ├── NSTextRange.h
│   ├── NSTextSelection.h
│   ├── NSTextSelectionNavigation.h
│   ├── NSTextStorage.h
│   ├── NSTextViewportLayoutController.h
│   ├── NSToolbar+UIKitAdditions.h
│   ├── NSTouchBar+UIKitAdditions.h
│   ├── NSUserActivity+NSItemProvider.h
│   ├── PrintKitUI.h
│   ├── ShareSheet.h
│   ├── UIAccelerometer.h
│   ├── UIAccessibility.h
│   ├── UIAccessibilityAdditions.h
│   ├── UIAccessibilityConstants.h
│   ├── UIAccessibilityContainer.h
│   ├── UIAccessibilityContentSizeCategoryImageAdjusting.h
│   ├── UIAccessibilityCustomAction.h
│   ├── UIAccessibilityCustomRotor.h
│   ├── UIAccessibilityElement.h
│   ├── UIAccessibilityIdentification.h
│   ├── UIAccessibilityLocationDescriptor.h
│   ├── UIAccessibilityZoom.h
│   ├── UIAction.h
│   ├── UIActionSheet.h
│   ├── UIActivity.h
│   ├── UIActivityIndicatorView.h
│   ├── UIActivityItemProvider.h
│   ├── UIActivityItemsConfiguration.h
│   ├── UIActivityItemsConfigurationReading.h
│   ├── UIActivityViewController.h
│   ├── UIAlert.h
│   ├── UIAlertController.h
│   ├── UIAlertView.h
│   ├── UIAppearance.h
│   ├── UIApplication.h
│   ├── UIApplicationShortcutItem.h
│   ├── UIAttachmentBehavior.h
│   ├── UIBackgroundConfiguration.h
│   ├── UIBandSelectionInteraction.h
│   ├── UIBarAppearance.h
│   ├── UIBarButtonItem.h
│   ├── UIBarButtonItemAppearance.h
│   ├── UIBarButtonItemGroup.h
│   ├── UIBarCommon.h
│   ├── UIBarItem.h
│   ├── UIBehavioralStyle.h
│   ├── UIBezierPath.h
│   ├── UIBlurEffect.h
│   ├── UIButton.h
│   ├── UIButtonConfiguration.h
│   ├── UICalendarSelection.h
│   ├── UICalendarSelectionMultiDate.h
│   ├── UICalendarSelectionSingleDate.h
│   ├── UICalendarView.h
│   ├── UICalendarViewDecoration.h
│   ├── UICellAccessory.h
│   ├── UICellConfigurationState.h
│   ├── UICloudSharingController.h
│   ├── UICollectionLayoutList.h
│   ├── UICollectionView.h
│   ├── UICollectionViewCell.h
│   ├── UICollectionViewCompositionalLayout.h
│   ├── UICollectionViewController.h
│   ├── UICollectionViewFlowLayout.h
│   ├── UICollectionViewItemRegistration.h
│   ├── UICollectionViewLayout.h
│   ├── UICollectionViewListCell.h
│   ├── UICollectionViewTransitionLayout.h
│   ├── UICollectionViewUpdateItem.h
│   ├── UICollisionBehavior.h
│   ├── UIColor.h
│   ├── UIColorPickerViewController.h
│   ├── UIColorWell.h
│   ├── UICommand.h
│   ├── UIConfigurationColorTransformer.h
│   ├── UIConfigurationState.h
│   ├── UIContentConfiguration.h
│   ├── UIContentSizeCategory.h
│   ├── UIContentSizeCategoryAdjusting.h
│   ├── UIContextMenuConfiguration.h
│   ├── UIContextMenuInteraction.h
│   ├── UIContextualAction.h
│   ├── UIControl.h
│   ├── UIDataDetectors.h
│   ├── UIDataSourceTranslating.h
│   ├── UIDatePicker.h
│   ├── UIDeferredMenuElement.h
│   ├── UIDevice.h
│   ├── UIDiffableDataSource.h
│   ├── UIDocument.h
│   ├── UIDocumentBrowserAction.h
│   ├── UIDocumentBrowserViewController.h
│   ├── UIDocumentInteractionController.h
│   ├── UIDocumentMenuViewController.h
│   ├── UIDocumentPickerExtensionViewController.h
│   ├── UIDocumentPickerViewController.h
│   ├── UIDocumentProperties.h
│   ├── UIDragInteraction.h
│   ├── UIDragItem.h
│   ├── UIDragPreview.h
│   ├── UIDragPreviewParameters.h
│   ├── UIDragSession.h
│   ├── UIDropInteraction.h
│   ├── UIDynamicAnimator.h
│   ├── UIDynamicBehavior.h
│   ├── UIDynamicItemBehavior.h
│   ├── UIEditMenuInteraction.h
│   ├── UIEvent.h
│   ├── UIEventAttribution.h
│   ├── UIEventAttributionView.h
│   ├── UIFeedbackGenerator.h
│   ├── UIFieldBehavior.h
│   ├── UIFindInteraction.h
│   ├── UIFindSession.h
│   ├── UIFocus.h
│   ├── UIFocusAnimationCoordinator.h
│   ├── UIFocusDebugger.h
│   ├── UIFocusEffect.h
│   ├── UIFocusGuide.h
│   ├── UIFocusMovementHint.h
│   ├── UIFocusSystem.h
│   ├── UIFont.h
│   ├── UIFontDescriptor.h
│   ├── UIFontMetrics.h
│   ├── UIFontPickerViewController.h
│   ├── UIFontPickerViewControllerConfiguration.h
│   ├── UIFoundation.h
│   ├── UIGeometry.h
│   ├── UIGestureRecognizer.h
│   ├── UIGestureRecognizerSubclass.h
│   ├── UIGraphics.h
│   ├── UIGraphicsImageRenderer.h
│   ├── UIGraphicsPDFRenderer.h
│   ├── UIGraphicsRenderer.h
│   ├── UIGraphicsRendererSubclass.h
│   ├── UIGravityBehavior.h
│   ├── UIGuidedAccess.h
│   ├── UIGuidedAccessRestrictions.h
│   ├── UIHoverGestureRecognizer.h
│   ├── UIImage.h
│   ├── UIImageAsset.h
│   ├── UIImageConfiguration.h
│   ├── UIImagePickerController.h
│   ├── UIImageSymbolConfiguration.h
│   ├── UIImageView.h
│   ├── UIImpactFeedbackGenerator.h
│   ├── UIIndirectScribbleInteraction.h
│   ├── UIInputView.h
│   ├── UIInputViewController.h
│   ├── UIInteraction.h
│   ├── UIInterface.h
│   ├── UIKey.h
│   ├── UIKeyCommand.h
│   ├── UIKeyConstants.h
│   ├── UIKeyboardLayoutGuide.h
│   ├── UIKit.apinotes
│   ├── UIKit.h
│   ├── UIKitCore.h
│   ├── UIKitDefines.h
│   ├── UILabel.h
│   ├── UILargeContentViewer.h
│   ├── UILayoutGuide.h
│   ├── UILexicon.h
│   ├── UIListContentConfiguration.h
│   ├── UIListContentImageProperties.h
│   ├── UIListContentTextProperties.h
│   ├── UIListSeparatorConfiguration.h
│   ├── UILocalNotification.h
│   ├── UILocalizedIndexedCollation.h
│   ├── UILongPressGestureRecognizer.h
│   ├── UIManagedDocument.h
│   ├── UIMenu.h
│   ├── UIMenuBuilder.h
│   ├── UIMenuController.h
│   ├── UIMenuElement.h
│   ├── UIMenuLeaf.h
│   ├── UIMenuSystem.h
│   ├── UIMotionEffect.h
│   ├── UINavigationBar.h
│   ├── UINavigationBarAppearance.h
│   ├── UINavigationController.h
│   ├── UINavigationItem.h
│   ├── UINib.h
│   ├── UINibDeclarations.h
│   ├── UINibLoading.h
│   ├── UINotificationFeedbackGenerator.h
│   ├── UIOpenURLContext.h
│   ├── UIPageControl.h
│   ├── UIPageViewController.h
│   ├── UIPanGestureRecognizer.h
│   ├── UIPasteConfiguration.h
│   ├── UIPasteConfigurationSupporting.h
│   ├── UIPasteControl.h
│   ├── UIPasteboard.h
│   ├── UIPencilInteraction.h
│   ├── UIPickerView.h
│   ├── UIPinchGestureRecognizer.h
│   ├── UIPointerAccessory.h
│   ├── UIPointerInteraction.h
│   ├── UIPointerLockState.h
│   ├── UIPointerRegion.h
│   ├── UIPointerStyle.h
│   ├── UIPopoverBackgroundView.h
│   ├── UIPopoverController.h
│   ├── UIPopoverPresentationController.h
│   ├── UIPopoverPresentationControllerSourceItem.h
│   ├── UIPopoverSupport.h
│   ├── UIPresentationController.h
│   ├── UIPress.h
│   ├── UIPressesEvent.h
│   ├── UIPreviewInteraction.h
│   ├── UIPreviewParameters.h
│   ├── UIPrintError.h
│   ├── UIPrintFormatter.h
│   ├── UIPrintInfo.h
│   ├── UIPrintInteractionController.h
│   ├── UIPrintPageRenderer.h
│   ├── UIPrintPaper.h
│   ├── UIPrintServiceExtension.h
│   ├── UIPrinter.h
│   ├── UIPrinterPickerController.h
│   ├── UIProgressView.h
│   ├── UIPushBehavior.h
│   ├── UIReferenceLibraryViewController.h
│   ├── UIRefreshControl.h
│   ├── UIRegion.h
│   ├── UIResponder+UIActivityItemsConfiguration.h
│   ├── UIResponder.h
│   ├── UIRotationGestureRecognizer.h
│   ├── UIScene.h
│   ├── UISceneActivationConditions.h
│   ├── UISceneDefinitions.h
│   ├── UISceneEnhancedStateRestoration.h
│   ├── UISceneOptions.h
│   ├── UISceneSession.h
│   ├── UISceneWindowingBehaviors.h
│   ├── UIScreen.h
│   ├── UIScreenEdgePanGestureRecognizer.h
│   ├── UIScreenMode.h
│   ├── UIScreenshotService.h
│   ├── UIScribbleInteraction.h
│   ├── UIScrollView.h
│   ├── UISearchBar.h
│   ├── UISearchContainerViewController.h
│   ├── UISearchController.h
│   ├── UISearchDisplayController.h
│   ├── UISearchSuggestion.h
│   ├── UISearchTextField.h
│   ├── UISegmentedControl.h
│   ├── UISelectionFeedbackGenerator.h
│   ├── UISheetPresentationController.h
│   ├── UISlider.h
│   ├── UISnapBehavior.h
│   ├── UISplitViewController.h
│   ├── UISpringLoadedInteraction.h
│   ├── UISpringLoadedInteractionSupporting.h
│   ├── UIStackView.h
│   ├── UIStateRestoration.h
│   ├── UIStatusBarManager.h
│   ├── UIStepper.h
│   ├── UIStoryboard.h
│   ├── UIStoryboardPopoverSegue.h
│   ├── UIStoryboardSegue.h
│   ├── UIStringDrawing.h
│   ├── UISwipeActionsConfiguration.h
│   ├── UISwipeGestureRecognizer.h
│   ├── UISwitch.h
│   ├── UITabBar.h
│   ├── UITabBarAppearance.h
│   ├── UITabBarController.h
│   ├── UITabBarItem.h
│   ├── UITableView.h
│   ├── UITableViewCell.h
│   ├── UITableViewController.h
│   ├── UITableViewHeaderFooterView.h
│   ├── UITapGestureRecognizer.h
│   ├── UITargetedDragPreview.h
│   ├── UITargetedPreview.h
│   ├── UITextChecker.h
│   ├── UITextDragPreviewRenderer.h
│   ├── UITextDragURLPreviews.h
│   ├── UITextDragging.h
│   ├── UITextDropProposal.h
│   ├── UITextDropping.h
│   ├── UITextField.h
│   ├── UITextFormattingCoordinator.h
│   ├── UITextInput.h
│   ├── UITextInputTraits.h
│   ├── UITextInteraction.h
│   ├── UITextItemInteraction.h
│   ├── UITextPasteConfigurationSupporting.h
│   ├── UITextPasteDelegate.h
│   ├── UITextSearching.h
│   ├── UITextView.h
│   ├── UITimingCurveProvider.h
│   ├── UITimingParameters.h
│   ├── UIToolTipInteraction.h
│   ├── UIToolbar.h
│   ├── UIToolbarAppearance.h
│   ├── UITouch.h
│   ├── UITrackingLayoutGuide.h
│   ├── UITraitCollection.h
│   ├── UIUserActivity.h
│   ├── UIUserNotificationSettings.h
│   ├── UIVibrancyEffect.h
│   ├── UIVideoEditorController.h
│   ├── UIView.h
│   ├── UIViewAnimating.h
│   ├── UIViewConfigurationState.h
│   ├── UIViewController.h
│   ├── UIViewControllerTransitionCoordinator.h
│   ├── UIViewControllerTransitioning.h
│   ├── UIViewPropertyAnimator.h
│   ├── UIVisualEffect.h
│   ├── UIVisualEffectView.h
│   ├── UIWebView.h
│   ├── UIWindow.h
│   ├── UIWindowScene.h
│   ├── UIWindowSceneActivationAction.h
│   ├── UIWindowSceneActivationConfiguration.h
│   ├── UIWindowSceneActivationInteraction.h
│   ├── UIWindowSceneActivationRequestOptions.h
│   ├── UIWindowSceneGeometry.h
│   ├── UIWindowSceneGeometryPreferences.h
│   ├── UIWindowSceneGeometryPreferencesIOS.h
│   ├── UIWindowSceneGeometryPreferencesMac.h
│   └── UNNotificationResponse+UIKitAdditions.h
```
