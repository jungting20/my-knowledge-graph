---
title: OIDC 로그아웃 메커니즘
type: concept
tags: [OIDC, 로그아웃, 세션관리, back-channel-logout, end-session]
created: 2026-04-10
updated: 2026-04-10
sources: [oidc-session-management_logto-blog.md]
---

# OIDC 로그아웃 메커니즘

## 개요

OIDC 로그아웃은 IdP 중앙 세션과 RP의 분산된 클라이언트 토큰을 모두 처리해야 하기 때문에 복잡하다. 세 가지 메커니즘을 단계적으로 적용하는 것이 권장된다.

---

## 1단계: 클라이언트 측 토큰 및 로컬 세션 삭제

가장 기본적인 로그아웃 단계.

**처리 항목:**
- ID Token 삭제
- Access Token 삭제
- Refresh Token 삭제
- 세션 쿠키 삭제 (웹 애플리케이션의 경우)
- 서버 측 세션 데이터 삭제 (해당하는 경우)

**한계:** IdP의 중앙 세션이 여전히 활성 상태이면, 사용자가 다시 RP에 접근할 때 토큰이 삭제되었어도 자동 재인증될 수 있다.

---

## 2단계: IdP End-Session Endpoint 호출

IdP의 중앙 sign-in 세션을 종료한다.

**동작 방식:**
1. RP가 IdP의 **end-session endpoint**로 사용자를 리디렉션
2. IdP가 세션 쿠키를 삭제하고 sign-in 세션 종료
3. 세션 종료 후, 동일 세션을 공유하던 모든 RP에서 재인증이 요구됨

이 단계를 거쳐야 완전한 로그아웃이 이루어진다.

---

## 3단계: Back-Channel Logout

사용자 상호작용 없이 여러 RP에서 동시 로그아웃을 수행한다.

**근거 명세:** OpenID Connect Back-Channel Logout 1.0

**동작 방식:**
1. 사용자가 한 RP에서 로그아웃 요청
2. IdP가 sign-out 요청을 처리하고 세션 종료
3. IdP가 해당 세션을 공유하는 모든 RP의 back-channel logout endpoint로 알림 전송
4. 알림을 받은 각 RP가 독립적으로 사용자 세션과 토큰을 정리

**특징:**
- 사용자 브라우저를 통하지 않고 서버 간(server-to-server) 통신으로 진행
- [[sso]] 환경에서 완전한 글로벌 로그아웃 구현에 필수

---

## 로그아웃 완전성 비교

| 방법 | 클라이언트 세션 종료 | IdP 세션 종료 | 다른 RP 로그아웃 |
|------|---------------------|--------------|-----------------|
| 토큰 삭제만 | ✅ | ❌ | ❌ |
| + End-Session | ✅ | ✅ | ❌ |
| + Back-Channel | ✅ | ✅ | ✅ |

## 관련 개념

- [[oidc]] — 기반 프로토콜
- [[oidc-session-management]] — 세션 구조
- [[sso]] — 멀티 RP 환경

## 참고 소스

- [[oidc-session-management_logto-blog]]
