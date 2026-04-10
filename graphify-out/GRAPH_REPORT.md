# Graph Report - ./raw  (2026-04-10)

## Corpus Check
- Corpus is ~937 words - fits in a single context window. You may not need a graph.

## Summary
- 23 nodes · 30 edges · 5 communities detected
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Identity Provider (IdP)` - 8 edges
2. `Relying Party (RP) / Service Provider (SP)` - 7 edges
3. `OpenID Connect (OIDC)` - 5 edges
4. `Clear centralized sign-in session at IdP` - 5 edges
5. `OIDC back-channel logout` - 5 edges
6. `OIDC sign-out mechanisms` - 4 edges
7. `Sign-in session / Authentication session` - 3 edges
8. `ID Token` - 3 edges
9. `Implementing OIDC logout and session management: A complete guide` - 2 edges
10. `Authorization Code flow` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Identity Provider (IdP)` --shares_data_with--> `ID Token`  [INFERRED]
  raw/oidc-session-management_logto-blog.md → raw/oidc-session-management_logto-blog.md  _Bridges community 0 → community 2_
- `Implementing OIDC logout and session management: A complete guide` --references--> `OpenID Connect (OIDC)`  [EXTRACTED]
  raw/oidc-session-management_logto-blog.md → raw/oidc-session-management_logto-blog.md  _Bridges community 1 → community 4_
- `OpenID Connect (OIDC)` --conceptually_related_to--> `Identity Provider (IdP)`  [EXTRACTED]
  raw/oidc-session-management_logto-blog.md → raw/oidc-session-management_logto-blog.md  _Bridges community 4 → community 0_
- `OpenID Connect (OIDC)` --conceptually_related_to--> `Relying Party (RP) / Service Provider (SP)`  [EXTRACTED]
  raw/oidc-session-management_logto-blog.md → raw/oidc-session-management_logto-blog.md  _Bridges community 4 → community 2_
- `Clear centralized sign-in session at IdP` --conceptually_related_to--> `Identity Provider (IdP)`  [EXTRACTED]
  raw/oidc-session-management_logto-blog.md → raw/oidc-session-management_logto-blog.md  _Bridges community 0 → community 1_

## Hyperedges (group relationships)
- **OIDC authentication flow (RP redirect, IdP session, code, token exchange)** — oidc-session-management_logto-blog_relying_party, oidc-session-management_logto-blog_identity_provider, oidc-session-management_logto-blog_sign_in_session, oidc-session-management_logto-blog_grant, oidc-session-management_logto-blog_authorization_code_flow [EXTRACTED 0.91]
- **Multi-faceted OIDC sign-out (client, IdP session, back-channel)** — oidc-session-management_logto-blog_oidc_sign_out, oidc-session-management_logto-blog_client_sign_out, oidc-session-management_logto-blog_idp_sign_out, oidc-session-management_logto-blog_back_channel_logout [EXTRACTED 0.92]
- **Client-side authentication status via IdP-issued tokens** — oidc-session-management_logto-blog_relying_party, oidc-session-management_logto-blog_id_token, oidc-session-management_logto-blog_access_token, oidc-session-management_logto-blog_refresh_token [EXTRACTED 0.90]

## Communities

### Community 0 - "IdP 세션 & SSO"
Cohesion: 0.33
Nodes (6): Grant, Identity Provider (IdP), RP sign-in session management, Session cookie (HttpOnly, Secure), Sign-in session / Authentication session, Single Sign-On (SSO)

### Community 1 - "로그아웃 흐름"
Cohesion: 0.4
Nodes (6): Clear tokens and local session at client, End-session endpoint, Implementing OIDC logout and session management: A complete guide, Clear centralized sign-in session at IdP, OIDC sign-out mechanisms, Active IdP session causes automatic re-auth after client token clear

### Community 2 - "클라이언트 토큰 관리"
Cohesion: 0.5
Nodes (5): Access Token, ID Token, offline_access scope, Refresh Token, Relying Party (RP) / Service Provider (SP)

### Community 3 - "Back-Channel Logout"
Cohesion: 0.67
Nodes (3): OIDC back-channel logout, OpenID Connect Back-Channel Logout 1.0, Sign out all RPs without extra user interaction

### Community 4 - "OIDC 프로토콜"
Cohesion: 0.67
Nodes (3): Authorization Code flow, OAuth 2.0, OpenID Connect (OIDC)

## Knowledge Gaps
- **10 isolated node(s):** `OAuth 2.0`, `Grant`, `Single Sign-On (SSO)`, `RP sign-in session management`, `Session cookie (HttpOnly, Secure)` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Identity Provider (IdP)` connect `IdP 세션 & SSO` to `로그아웃 흐름`, `클라이언트 토큰 관리`, `Back-Channel Logout`, `OIDC 프로토콜`?**
  _High betweenness centrality (0.571) - this node is a cross-community bridge._
- **Why does `Relying Party (RP) / Service Provider (SP)` connect `클라이언트 토큰 관리` to `IdP 세션 & SSO`, `Back-Channel Logout`, `OIDC 프로토콜`?**
  _High betweenness centrality (0.299) - this node is a cross-community bridge._
- **Why does `Clear centralized sign-in session at IdP` connect `로그아웃 흐름` to `IdP 세션 & SSO`?**
  _High betweenness centrality (0.238) - this node is a cross-community bridge._
- **What connects `OAuth 2.0`, `Grant`, `Single Sign-On (SSO)` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._