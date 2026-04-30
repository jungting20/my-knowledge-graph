---
title: "OIDC 로그아웃 및 세션 관리 완전 가이드"
type: source
tags: [OIDC, 인증, 세션관리, OAuth2, SSO, 보안]
created: 2026-04-29
updated: 2026-04-29
sources: ["oidc-session-management_logto-blog.md"]
original_source: "https://blog.logto.io/oidc-session-management"
---

## 요약

OpenID Connect(OIDC) 세션 관리와 로그아웃 메커니즘을 종합적으로 설명하는 가이드. IdP(Identity Provider)와 RP(Relying Party) 간 상호작용, 토큰 관리, 세션 생명주기를 다룬다.

## 핵심 용어

| 용어 | 설명 |
|------|------|
| **IdP (Identity Provider)** | 사용자 신원을 저장·인증하는 서비스 |
| **RP / SP (Relying Party)** | IdP에 의존하는 웹 앱 또는 서비스 |
| **Sign-in Session** | 사용자가 IdP에 로그인할 때 생성되는 세션 |
| **Grant** | IdP가 생성·관리하는 중앙 인증/인가 정보 |
| **SSO** | 하나의 자격증명으로 여러 앱에 접근하는 세션 서비스 |

## OIDC 인증 플로우

1. 사용자가 RP에 접근
2. RP → IdP로 리다이렉트 (인증 요청)
3. IdP가 세션 상태 확인 (없거나 만료 시 로그인 페이지 표시)
4. 사용자 로그인 완료
5. IdP가 새 Sign-in 세션 + Authentication Grant 생성
6. Authorization Code와 함께 RP로 리다이렉트
7. RP가 코드 → 토큰 교환

## 클라이언트 측 인증 상태

| 토큰 | 특징 |
|------|------|
| **ID Token** | 단기 유효, 사용자 신원 검증용 |
| **Access Token** | 단기/장기 가능, 만료 시 재인증 필요 |
| **Refresh Token** | `offline_access` 스코프 필요, 재인증 없이 인증 연장 |

**토큰 저장 전략**:
- SPA: 브라우저 로컬/세션 스토리지
- 웹앱: 서버 측 세션 데이터 또는 쿠키

## OIDC 로그아웃 메커니즘

### 1. 클라이언트 측 토큰/세션 제거
로컬 토큰 삭제만으로는 불완전 — IdP 세션이 살아있으면 자동 재인증 발생

### 2. IdP 중앙 세션 종료
- RP → IdP의 **end-session endpoint**로 리다이렉트
- IdP 세션 쿠키 제거
- 이후 동일 세션을 공유하는 다른 RP들도 재인증 요구됨

### 3. 백채널 로그아웃 (Back-Channel Logout)
- 표준: OpenID Connect Back-Channel Logout 1.0
- 동작: 한 RP에서 로그아웃 시 → IdP가 같은 세션을 공유하는 **모든 RP**에 알림 전송
- RP들은 각자 세션과 토큰을 정리

## 세션 관리 패턴

### 단일 RP
디바이스/브라우저별 독립 세션 → 한 RP 로그아웃이 다른 RP에 영향 없음

### 다중 RP (SSO)
동일 user agent에서 오는 요청은 IdP에서 일관된 인증 상태 유지

## 관련 개념

- [[OpenID Connect (OIDC)]]
- [[OAuth 2.0]]
- [[SSO (Single Sign-On)]]
- [[백채널 로그아웃]]
- [[Identity Provider]]
