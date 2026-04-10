---
title: OIDC (OpenID Connect)
type: concept
tags: [OIDC, OAuth2, 인증, 신원확인, 프로토콜]
created: 2026-04-10
updated: 2026-04-10
sources: [oidc-session-management_logto-blog.md]
---

# OIDC (OpenID Connect)

## 정의

OpenID Connect(OIDC)는 OAuth 2.0 프로토콜 위에 구축된 단순한 신원 레이어(identity layer)이다. 클라이언트가 인가 서버의 인증 결과를 기반으로 최종 사용자의 신원을 검증하고, 상호운용 가능한 REST 방식으로 기본 프로필 정보를 얻을 수 있게 해준다.

## 특징

- **단순성과 유연성**에 초점을 맞춘 설계
- 웹 애플리케이션, 모바일 앱, API에서 SSO 및 신원 검증에 널리 사용됨
- OAuth 2.0의 인가(Authorization) 위에 인증(Authentication) 레이어를 추가

## 핵심 구성요소

| 구성요소 | 역할 |
|----------|------|
| **Identity Provider (IdP)** | 사용자 신원을 저장하고 인증하는 서비스 |
| **Relying Party (RP)** | 인증을 IdP에 의존하는 클라이언트 애플리케이션 |
| **ID Token** | 인증된 사용자의 신원 정보를 담은 단기 토큰 (JWT 형식) |
| **Access Token** | 보호된 리소스 접근 권한을 부여하는 토큰 |
| **Refresh Token** | 재인증 없이 인증 상태를 연장하는 토큰 (`offline_access` 스코프 필요) |

## 인증 흐름 (Authorization Code Flow)

1. 사용자가 RP에 접속
2. RP가 사용자를 IdP로 리디렉션
3. IdP가 세션 상태 확인 후 필요 시 로그인 요청
4. 사용자 인증 완료
5. IdP가 인증 코드를 포함해 RP로 리디렉션
6. RP가 인증 코드를 토큰으로 교환

## 관련 개념

- [[sso]] — OIDC를 기반으로 하는 싱글 사인온
- [[oidc-session-management]] — IdP와 RP 간 세션 상태 관리
- [[oidc-logout]] — 로그아웃 메커니즘

## 참고 소스

- [[oidc-session-management_logto-blog]]
