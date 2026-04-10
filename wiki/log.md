# Wiki Log

위키의 모든 작업 이력을 시간순으로 기록합니다. append-only.

빠른 탐색: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-10] ingest | OIDC 로그아웃 및 세션 관리: 완전 가이드

- **소스:** `raw/oidc-session-management_logto-blog.md`
- **생성된 페이지:**
  - `wiki/sources/oidc-session-management_logto-blog.md` — 소스 요약
  - `wiki/concepts/oidc.md` — OpenID Connect 개념
  - `wiki/concepts/sso.md` — Single Sign-On 개념
  - `wiki/concepts/oidc-session-management.md` — OIDC 세션 관리
  - `wiki/concepts/oidc-logout.md` — OIDC 로그아웃 메커니즘 (3단계: 토큰 삭제, end-session, back-channel logout)
- **index.md** 신규 생성

## [2026-04-10] query | Identity Provider가 5개 커뮤니티 전체를 연결하는 유일한 브릿지인 이유

- GRAPH_REPORT.md 분석: IdP betweenness centrality 0.571, 8 edges (1위 god node)
- 분석 결과 → `wiki/analysis/why-idp-bridges-all-communities.md` 저장
- **핵심 결론**: IdP는 OIDC 아키텍처에서 유일한 "전역 상태 소유자" (세션 발급·로그아웃 조율·토큰 서명 권한 집중)

