---
title: "OIDC 로그아웃 및 세션 관리: 완전 가이드"
type: source
tags: [OIDC, OAuth2, 세션관리, 로그아웃, SSO, 인증]
created: 2026-04-10
updated: 2026-04-10
sources: [oidc-session-management_logto-blog.md]
---

# OIDC 로그아웃 및 세션 관리: 완전 가이드

**원본 출처:** https://blog.logto.io/oidc-session-management  
**수집일:** 2026-04-10

---

## 개요

OpenID Connect(OIDC)는 OAuth 2.0 위에 구축된 인증 레이어로, Identity Provider(IdP)와 Relying Party(RP) 간의 세션 및 인증 상태 관리를 다룬다. 본 문서는 Logto 블로그의 OIDC 세션 관리 가이드를 요약한다.

---

## 핵심 용어

| 용어 | 설명 |
|------|------|
| **Identity Provider (IdP)** | 사용자 신원을 저장하고 인증하는 서비스 |
| **Relying Party (RP) / Service Provider (SP)** | 인증을 IdP에 의존하는 웹 애플리케이션 또는 서비스 |
| **Sign-in Session** | 사용자가 IdP에 로그인할 때 수립되는 세션 |
| **Grant** | IdP가 생성·관리하는 중앙화된 인증 및 인가 정보 |
| **SSO** | 하나의 로그인 자격증명으로 여러 애플리케이션에 접근하는 세션 서비스 |

---

## OIDC 인증 흐름

1. 사용자가 웹 애플리케이션(RP)에 접속
2. RP가 사용자를 IdP로 리디렉션
3. IdP가 사용자의 sign-in 세션 상태 확인 (없거나 만료된 경우 로그인 요청)
4. 사용자가 로그인 페이지에서 인증
5. 로그인 페이지가 상호작용 결과를 IdP로 제출
6. IdP가 새 sign-in 세션과 인증 grant 생성
7. IdP가 인증 코드(Authorization Code)를 포함하여 사용자를 RP로 리디렉션
8. RP가 인증 코드를 받아 토큰으로 교환

→ 관련 개념: [[oidc-auth-flow]]

---

## RP 세션 관리

### 단일 RP 세션

- 사용자가 다른 기기/브라우저에서 접속할 때마다 별도의 sign-in 세션이 수립됨
- 한 RP에서 로그아웃해도 다른 RP의 세션은 유지됨

### 다중 RP 세션 (중앙화)

- 동일한 사용자 에이전트(기기/브라우저)에서 요청이 오는 한, IdP는 여러 RP 간에 일관된 인증 상태를 유지
- 이를 통해 [[sso]] 기능이 가능해짐

---

## 클라이언트 측 인증 상태

RP는 IdP가 발급한 토큰으로 사용자의 인증 및 인가 상태를 검증한다.

| 토큰 | 설명 |
|------|------|
| **ID Token** | 단기 토큰. 인증된 사용자의 신원 확인에 사용 |
| **Access Token** | 보호된 리소스 접근 권한 부여. 만료 또는 삭제 시 재인증 필요 |
| **Refresh Token** | `offline_access` 스코프 요청 시 발급. 재인증 없이 인증 상태 연장 가능 |

**토큰 저장 전략:**
- SPA: 브라우저의 `localStorage` 또는 `sessionStorage`
- 웹 애플리케이션: 서버 측 세션 데이터 또는 쿠키

---

## OIDC 로그아웃 메커니즘

OIDC 로그아웃은 IdP 중앙 세션과 분산된 클라이언트 토큰 양쪽을 모두 처리해야 한다.

### 1. 클라이언트 측 토큰 및 로컬 세션 삭제

- 브라우저/메모리에서 ID 토큰, Access 토큰, Refresh 토큰을 제거
- 웹 애플리케이션의 경우 세션 쿠키와 세션 데이터도 삭제

### 2. IdP의 중앙 Sign-in 세션 종료

- IdP 세션이 활성 상태이면 클라이언트 토큰이 삭제돼도 자동 재인증될 수 있음
- 완전한 로그아웃을 위해서는 RP가 IdP의 **end-session endpoint**로 리디렉션하여 세션 종료 필요

### 3. OIDC Back-Channel Logout

- 사용자가 한 RP에서 로그아웃 시 추가 사용자 조작 없이 모든 RP에서 자동 로그아웃
- 근거: OpenID Connect Back-Channel Logout 1.0 명세
- IdP가 sign-out 요청을 수신하면 해당 세션을 공유하는 모든 RP의 back-channel logout endpoint로 알림 전송
- 알림을 받은 RP는 사용자 세션과 토큰을 정리

→ 관련 개념: [[oidc-logout]], [[oidc-back-channel-logout]]
