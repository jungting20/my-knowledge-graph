---
title: OIDC 세션 관리
type: concept
tags: [OIDC, 세션관리, 인증, IdP, RP]
created: 2026-04-10
updated: 2026-04-10
sources: [oidc-session-management_logto-blog.md]
---

# OIDC 세션 관리

## 개요

OIDC 세션 관리는 Identity Provider(IdP)와 Relying Party(RP) 간의 인증 상태를 추적하고 유지하는 메커니즘이다.

## Sign-in Session 구성 요소

IdP에서 사용자 로그인 시 수립되는 세션은 다음을 포함한다:

- 사용자 신원 (User Identity)
- 인증 시각 (Authentication Time)
- 세션 만료 시각 (Session Expiration Time)

세션 상태는 브라우저에 **세션 쿠키**로 안전하게 저장된다. 이 쿠키는 일반적으로 `HttpOnly`와 `Secure` 플래그로 설정되어 클라이언트 측 접근을 차단하고 보안 통신을 보장한다.

## 클라이언트 측 인증 상태

RP는 IdP가 발급한 토큰을 통해 사용자의 인증/인가 상태를 관리한다:

| 토큰 | 수명 | 용도 |
|------|------|------|
| **ID Token** | 단기 | 사용자 신원 확인 |
| **Access Token** | 단기~장기 | 보호된 리소스 접근 |
| **Refresh Token** | 장기 (`offline_access` 필요) | 재인증 없이 인증 상태 연장 |

### 토큰 저장 전략

- **SPA (Single Page Application):** `localStorage` 또는 `sessionStorage`
- **전통적인 웹 애플리케이션:** 서버 측 세션 또는 쿠키

## 세션의 이중 구조

OIDC에서는 두 층위의 세션이 존재한다:

1. **IdP 중앙 세션**: IdP에서 관리하는 사용자의 전역 인증 상태
2. **RP 로컬 세션**: 각 RP가 독립적으로 관리하는 애플리케이션 세션

이 이중 구조로 인해 로그아웃 시 양쪽 모두를 처리해야 완전한 로그아웃이 이루어진다.

## 관련 개념

- [[oidc]] — 기반 프로토콜
- [[sso]] — 중앙화 세션을 활용한 싱글 사인온
- [[oidc-logout]] — 세션 종료 메커니즘

## 참고 소스

- [[oidc-session-management_logto-blog]]
