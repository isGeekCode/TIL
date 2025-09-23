# Integrity Cert.100.CSR-CER

## 1. 개요  
CSR(Certificate Signing Request)과 CER(Certificate) 발급 과정은 iOS 앱 개발에서 인증 체계를 이해하는 기본 단계이다.  
CSR은 공개키와 신청자 정보를 담아 인증서를 요청하는 파일이며, 이 과정에서 개인키/공개키 쌍이 생성된다.  

Keychain Access에서 CSR 생성 시 개인키와 공개키 쌍이 로컬에 생성되고, 개인키는 Keychain 내부에 안전하게 보관된다.  

CSR 파일은 공개키와 신청자 정보를 포함하며, Apple Developer Portal에 업로드되어 Apple이 해당 공개키를 기반으로 CER(인증서)를 발급한다. 
 
최종적으로 Keychain에서는 개인키와 CER이 결합되어 완전한 인증서 체인을 구성하며, 이 체인을 통해 코드 서명(Signing)이 이루어진다.

---

## 2. CSR (Certificate Signing Request)

### 2-1. CSR 생성 목적  
- 개발자의 개인키(Private Key)와 공개키(Public Key) 쌍을 생성한다.  
- 공개키와 신청자 정보를 Apple 서버에 제출하여 서명 가능한 인증서를 요청한다.  
- 생성 시 개인키는 자동으로 Keychain에 저장된다.

### 2-2. CSR 생성 방법  
1. Mac의 Keychain Access 실행  
2. 메뉴에서 `Certificate Assistant > Request a Certificate From a Certificate Authority` 선택  
3. 이메일, Common Name 입력 후 Key Size(2048 이상), RSA 선택  
4. `.certSigningRequest` 파일 저장

### 2-3. 결과  
- Keychain에 개인키가 저장된다.  
- 디스크에 CSR 파일이 생성된다.

---

## 3. CER (Certificate)

### 3-1. CER 발급 과정  
1. Apple Developer Portal 접속  
2. Certificates 메뉴에서 `+` 버튼 클릭  
3. **인증서 종류 선택**
   - Development (개발용): 로컬 디바이스 디버깅/개발 빌드 서명에 사용  
   - Distribution (배포용): TestFlight, Ad Hoc, App Store 배포 서명에 사용  
4. CSR 파일 업로드  
5. 발급 완료 후 `.cer` 파일 다운로드

#### 선택 가이드
- **개발 단계에서 디바이스 테스트가 목적**이면 → Development  
- **TestFlight/Ad Hoc/App Store 배포가 목적**이면 → Distribution  
※ 팀에서 둘 다 필요할 수 있으며, 각각 별도의 CER을 발급받아 관리한다.

### 3-2. CER 설치  
- `.cer` 파일을 더블클릭하면 Keychain에 등록된다.  
- Keychain에서 개인키와 연결되어 하나의 서명 가능한 인증서로 완성된다.

### 3-3. CER의 역할  
- 앱 서명(Signing)에 사용되는 인증서이다.  
- Provisioning Profile과 연결되어 빌드에 포함된다.  
- 기기에서 앱 실행 시 유효성 검증을 수행한다.

---

## 4. Keychain과의 관계  
- CSR 생성 시 개인키는 로컬 Keychain에 안전하게 보관된다.  
- CER은 Apple이 서명한 공개키 인증서이다.  
- Keychain에서는 개인키와 CER이 매칭되어 완전한 인증서 체인을 구성한다.  
- 이 체인이 코드 서명과 앱 실행 시 인증 검증에 사용된다.

---

## 5. 요약  
- CSR은 공개키와 신청자 정보를 담아 인증서를 요청하는 파일이다.  
- CER은 Apple이 CSR을 검증하여 발급하는 인증서이다.  
- Keychain은 개인키와 CER을 결합하여 서명 가능한 인증서 체인을 구성한다.  
- 이 과정이 iOS 인증 체계의 기본 뼈대이다.

---

## HISTORY  
- 250917 : 최초 작성
