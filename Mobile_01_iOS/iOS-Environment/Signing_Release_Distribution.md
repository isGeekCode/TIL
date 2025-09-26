# Signing - Release 빌드에서 Distribution 프로필 매칭 오류 해결

Xcode에서 Release 빌드 시 다음과 같은 메시지가 나타나면서 서명이 실패하는 경우가 있습니다.

```
No profile for team 'hyeonseok bang' matching 'EscapeLock.provisioning.dist' found:
Xcode couldn't find any provisioning profiles matching 'NHQN2VZC55/EscapeLock.provisioning.dist'.
```

## 원인
- `Signing & Capabilities > Signing (Release)` 항목의 `Code Signing Identity`가 `Apple Development`로 설정되어 있으면, 배포용 Distribution 프로비저닝 프로파일과 매칭되지 않습니다.
- 수동 서명 구성(Manual Signing)을 사용 중일 때 특히 자주 발생합니다.

## 해결 방법
1. **Release 빌드 서명 인증서 교체**  
   `Signing & Capabilities` 탭에서 Release 구성을 `Apple Distribution` 인증서로 변경합니다.
2. **프로비저닝 프로파일 확인**  
   - Apple Developer 사이트의 `Certificates, Identifiers & Profiles`에서 배포용 프로비저닝 프로파일이 활성 상태인지 확인합니다.
   - 프로젝트에 연결된 `Bundle Identifier`와 팀(Team ID)이 프로파일과 일치하는지 검토합니다.
3. **Xcode에 프로파일 설치 여부 확인**  
   최신 프로비저닝 프로파일을 다운로드하여 더블클릭하거나 Xcode Dock 아이콘으로 드래그해 설치합니다.
4. **Clean Build Folder**  
   `Product > Clean Build Folder` 실행 후 다시 Release 빌드를 시도하여 캐시된 서명 정보를 비웁니다.

## 추가 점검 포인트
- 자동 서명(`Automatically manage signing`)을 잠시 활성화해 Release 구성에서도 정상 빌드가 되는지 테스트하면 설정 오류를 빠르게 확인할 수 있습니다.
- CI/CD에서 동일한 문제가 발생한다면, 배포용 키체인에 `Apple Distribution` 인증서가 존재하는지와 프로파일 UUID가 최신인지 함께 확인합니다.

## 함께 보면 좋은 문서
- [Integrity - 인증서와 프로비저닝 프로파일 관리하기](../iOS-Integrity/Integrity_Certificate_Provisioning.md)
- [.ipa 파일 만들기](How_to.make_ipa.md)
- [Scheme - Debug / Release 빌드 분리하기](Scheme_Separate_BuildSet.md)
