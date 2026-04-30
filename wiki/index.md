# Wiki 인덱스

이 지식 그래프는 raw/ 폴더의 소스 파일들을 처리하여 구축된 지식 베이스입니다.

---

## 소스 (Sources)

raw/ 파일에서 직접 추출한 페이지들.

| 제목 | 태그 | 날짜 |
|------|------|------|
| [[sources/AutoBE vs. Claude Code 3rd-gen coding agent developer's review of the leaked source code\|AutoBE vs. Claude Code: Agentica와 Function Calling]] | AI에이전트, FunctionCalling, Agentica | 2025-04-29 |
| [[sources/Claude Code loop — Here Are 3 Autonomous Loops For My Daily Work!\|Claude Code /loop — 자율 루프 3가지 워크플로우]] | ClaudeCode, 자율에이전트, CI | 2026-03-09 |
| [[sources/HyperAgents by Meta\|HyperAgents: 스스로 하네스를 구축하는 에이전트]] | HyperAgents, Meta, 자기개선 | 2026-04-08 |
| [[sources/Seeing like an agent how we design tools in Claude Code\|에이전트처럼 보기: Claude Code 도구 설계]] | ClaudeCode, 도구설계, 프로그레시브디스클로저 | 2026-04-10 |
| [[sources/oidc-session-management_logto-blog\|OIDC 로그아웃 및 세션 관리 완전 가이드]] | OIDC, 인증, SSO, 보안 | 2026-04-10 |
| [[sources/클로드 코드 소스 유출에서 배우는 에이전트 구조\|클로드 코드 소스 유출에서 배우는 에이전트 구조]] | ClaudeCode, 하네스, 멀티에이전트 | 2026-04-28 |
| [[sources/Refreshing your Neovim config for 0.12.0\|Neovim 0.12.0 설정 리프레시]] | Neovim, LSP, 플러그인 | 2026-04-06 |
| [[sources/autopus-adk\|Autopus-ADK: 에이전트를 위한 하네스]] | Autopus, 멀티에이전트, AX | 2026-04-29 |

---

## 개념 (Concepts)

여러 소스에 걸쳐 등장하는 핵심 개념들.

| 개념 | 설명 |
|------|------|
| [[concepts/에이전트 하네스\|에이전트 하네스]] | AI 에이전트의 실행 구조를 관장하는 소프트웨어 시스템 |
| [[concepts/컨텍스트 엔지니어링\|컨텍스트 엔지니어링]] | 에이전트에게 무엇을 보여주고, 숨기고, 전달할지 다루는 방식 |
| [[concepts/멀티에이전트 시스템\|멀티에이전트 시스템]] | 역할이 나뉜 복수 에이전트들의 협력 구조 |
| [[concepts/AI Function Calling\|AI Function Calling]] | 개발자가 함수를 제공하면 AI가 선택·실행하는 기술 |
| [[concepts/Progressive Disclosure\|Progressive Disclosure (점진적 공개)]] | 에이전트가 필요할 때 점진적으로 컨텍스트를 탐색하는 기법 |

---

## 엔티티 (Entities)

등장하는 제품, 시스템, 연구 프로젝트들.

| 엔티티 | 유형 | 설명 |
|--------|------|------|
| [[entities/Claude Code\|Claude Code]] | 제품 | Anthropic의 AI 코딩 도구 |
| [[entities/Agentica\|Agentica]] | 프레임워크 | TypeScript Function Calling 특화 AI 프레임워크 |
| [[entities/HyperAgents\|HyperAgents]] | 연구 | Meta/UBC의 자기 개선 에이전트 연구 |

---

## 커뮤니티 / 주제별 클러스터

### AI 에이전트 구조
- 공통 개념: [[concepts/에이전트 하네스]], [[concepts/멀티에이전트 시스템]], [[concepts/컨텍스트 엔지니어링]]
- 관련 소스: Claude Code 유출 분석, HyperAgents, /loop 워크플로우, Seeing like an agent, Autopus-ADK

### Claude Code 생태계
- 도구: [[entities/Claude Code]]
- 관련 소스: /loop 워크플로우, 소스 유출 분석, 도구 설계

### 인증 / 보안
- 관련 소스: OIDC 세션 관리

### 개발 도구
- 관련 소스: Neovim 0.12.0 설정 리프레시
