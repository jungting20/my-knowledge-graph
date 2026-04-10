---
title: Identity Provider가 5개 커뮤니티 전체를 연결하는 유일한 브릿지인 이유
type: analysis
tags: [OIDC, IdP, 그래프분석, 브릿지노드, 세션관리]
created: 2026-04-10
updated: 2026-04-10
sources: [oidc-session-management_logto-blog.md]
---

# Identity Provider가 5개 커뮤니티 전체를 연결하는 유일한 브릿지인 이유

## 그래프 수치

`Identity Provider (IdP)`는 그래프 내 23개 노드 중 **8 edges**로 1위 god node이며, betweenness centrality 0.571로 압도적인 브릿지 역할을 한다. 다음 순위인 `Relying Party (RP)` (0.299)와도 큰 격차를 보인다.

---

## 핵심 이유: IdP는 OIDC 아키텍처의 유일한 "전역 상태 소유자"

OIDC 시스템에서 각 커뮤니티가 다루는 영역은 다음과 같다.

| 커뮤니티 | 다루는 영역 |
|----------|------------|
| 0 - IdP 세션 & SSO | 중앙 sign-in 세션, SSO, 세션 쿠키 |
| 1 - 로그아웃 흐름 | End-session endpoint, 토큰 삭제 절차 |
| 2 - 클라이언트 토큰 관리 | ID/Access/Refresh Token, RP 로컬 세션 |
| 3 - Back-Channel Logout | 서버 간 로그아웃 알림, 전체 RP 동기화 |
| 4 - OIDC 프로토콜 | Authorization Code flow, OAuth 2.0 |

이 5개 커뮤니티는 각각 독립적인 관심사를 가지지만, **모두 IdP를 통해서만 작동한다.**

---

## 커뮤니티별 의존성 분석

### Community 0 (IdP 세션 & SSO) → IdP가 곧 커뮤니티 자체
IdP는 중앙 sign-in 세션을 소유하고 SSO를 가능하게 하는 주체다. 커뮤니티 0은 IdP의 내부 상태를 직접 기술하므로, IdP는 이 커뮤니티의 핵심 노드다.

### Community 1 (로그아웃 흐름) → IdP 세션 종료가 완전한 로그아웃의 전제 조건
1단계(클라이언트 토큰 삭제)만으로는 불완전하다. IdP의 중앙 세션이 살아있으면 RP 재접근 시 **자동 재인증**이 발생한다. 따라서 `Clear centralized sign-in session at IdP` → IdP 연결이 필수적이다.

### Community 2 (클라이언트 토큰 관리) → 모든 토큰은 IdP가 발급
ID Token, Access Token, Refresh Token은 모두 IdP가 생성하고 서명한다. RP는 토큰을 보유하지만, 그 유효성 판단 권한은 IdP에 있다. `IdP --shares_data_with--> ID Token` 엣지가 이 의존성을 표현한다.

### Community 3 (Back-Channel Logout) → IdP가 알림의 발신자
Back-channel logout에서 IdP는 수동적 당사자가 아니라 **세션을 공유하는 모든 RP에 알림을 능동적으로 전송하는 오케스트레이터**다. RP들은 IdP의 알림 없이 다른 RP의 로그아웃을 알 수 없다.

### Community 4 (OIDC 프로토콜) → OIDC 자체가 IdP 중심 설계
`OpenID Connect (OIDC) --conceptually_related_to--> Identity Provider (IdP)` 엣지가 명시하듯, OIDC 프로토콜은 IdP를 신뢰의 근원(root of trust)으로 전제한다. Authorization Code flow의 모든 단계가 IdP를 거친다.

---

## 구조적 결론

IdP가 유일한 전-커뮤니티 브릿지인 이유는 아키텍처적 필연이다:

1. **상태의 중앙화**: 세션, 토큰 발급 권한, 로그아웃 조율 권한이 모두 IdP에 집중된다.
2. **프로토콜의 설계 철학**: OIDC는 분산된 RP들이 하나의 IdP를 신뢰하는 허브-앤-스포크(hub-and-spoke) 모델이다.
3. **로그아웃 완전성의 병목**: 완전한 로그아웃(1단계+2단계+3단계)은 반드시 IdP를 경유해야 하므로, 로그아웃 흐름·토큰 관리·back-channel 커뮤니티가 모두 IdP에 수렴한다.

RP는 각 애플리케이션의 지역적 상태를 관리하지만, IdP는 **모든 RP가 공유하는 전역 상태**를 관리한다. 이것이 betweenness centrality 0.571이라는 수치의 아키텍처적 의미다.

---

## 관련 개념

- [[oidc]] — 기반 프로토콜
- [[oidc-session-management]] — 세션 이중 구조
- [[oidc-logout]] — 로그아웃 3단계 메커니즘
- [[sso]] — IdP 중앙 세션의 SSO 활용
