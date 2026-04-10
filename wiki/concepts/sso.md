---
title: SSO (Single Sign-On)
type: concept
tags: [SSO, 인증, 세션관리, OIDC]
created: 2026-04-10
updated: 2026-04-10
sources: [oidc-session-management_logto-blog.md]
---

# SSO (Single Sign-On)

## 정의

Single Sign-On(SSO)은 사용자가 하나의 로그인 자격증명으로 여러 애플리케이션에 접근할 수 있게 하는 세션 서비스이다.

## 동작 원리

OIDC 기반 SSO에서는 IdP가 여러 RP에 걸쳐 일관된 인증 상태를 유지한다.

- 동일한 사용자 에이전트(기기/브라우저)에서 인증 요청이 오는 한, IdP의 중앙 세션이 유효하게 유지됨
- 사용자가 처음 한 번만 로그인하면, 이후 다른 RP에 접근 시 자동으로 인증됨 (추가 로그인 불필요)

## 세션 모델

### 단일 RP 세션
- 사용자가 다른 기기나 브라우저에서 접속하면 각각 별도의 세션이 수립됨
- 한 세션에서 로그아웃해도 다른 세션에는 영향 없음

### 다중 RP SSO 세션 (중앙화)
- 동일 기기/브라우저에서 같은 IdP를 공유하는 여러 RP에 대해 중앙 세션 유지
- 한 RP에서의 로그아웃이 다른 RP에 자동 전파되려면 [[oidc-back-channel-logout]] 필요

## 로그아웃 복잡성

SSO 환경에서는 로그아웃이 복잡하다:
- 클라이언트 측 토큰 삭제만으로는 완전한 로그아웃이 되지 않음
- IdP의 중앙 세션도 함께 종료해야 함
- 여러 RP에서의 동시 로그아웃을 위해 back-channel logout이 필요

자세한 내용은 [[oidc-logout]] 참조.

## 관련 개념

- [[oidc]] — SSO를 구현하는 프로토콜
- [[oidc-session-management]] — 세션 상태 관리
- [[oidc-logout]] — 로그아웃 메커니즘

## 참고 소스

- [[oidc-session-management_logto-blog]]
