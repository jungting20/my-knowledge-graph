---
title: "Autopus-ADK: 에이전트를 위한, 에이전트에 의한 하네스"
type: source
tags: [Autopus, 멀티에이전트, 하네스, ClaudeCode, AX, 에이전트팀]
created: 2026-04-29
updated: 2026-04-29
sources: ["autopus-adk/README.md"]
original_source: "https://github.com/Insajin/autopus-adk"
---

## 요약

Claude Code, Codex, Gemini CLI 등 AI 코딩 도구들이 실제 엔지니어링 팀처럼 동작하게 만드는 오픈소스 하네스 프레임워크. "Of the agents, By the agents, For the agents"라는 철학으로 16개 전문 에이전트, 40개 스킬, 하나의 설정 파일로 모든 플랫폼을 지원한다.

## 핵심 철학: AX (Agent Experience)

> UX가 사용자를 위해, DX가 개발자를 위해 설계하듯, **AX는 AI 에이전트를 위해 설계한다.**

| 원칙 | 의미 |
|------|------|
| **Of the Agents** | 16개 전문 에이전트가 실제 엔지니어링 팀 구성 |
| **By the Agents** | 에이전트가 파이프라인을 자율적으로 실행 |
| **For the Agents** | 모든 파일, 규칙, 문서가 에이전트가 파싱하기 좋게 설계됨 |
| **Every Session is Day One** | 세션 간 컨텍스트 전달이 없으므로 하네스가 기관 메모리 역할 |

## 핵심 문제 해결

- **플랫폼 락인**: Claude → Codex 전환 시 규칙/프롬프트 전면 재작성 → 단일 `autopus.yaml`로 해결
- **희망 주도 개발**: AI가 코드 작성 후 테스트·보안·문서 누락 → 구조화된 파이프라인으로 해결
- **세션 간 기억상실**: 결정 이유 소실 → Lore 시스템으로 해결
- **단일 에이전트 한계**: 멀티 파일 리팩터링 → 16개 전문 에이전트 팀으로 해결

## 7단계 멀티에이전트 파이프라인

```
Phase 1    │ 🧠 Planner         │ SPEC → 태스크 분해 + 에이전트 배정
Phase 1.5  │ 🧪 Tester          │ 실패 테스트 스캐폴드 (RED, TDD)
Phase 2    │ ⚡ Executor ×N      │ 병렬 worktree에서 TDD 구현
Phase 2.5  │ 📝 Annotator       │ @AX 문서 태그 관리
Gate  2    │ ✅ Validator        │ 빌드 + lint + vet
Phase 3    │ 🧪 Tester          │ 커버리지 → 85% 이상
Phase 4    │ 🔍 Reviewer + 🛡️   │ TRUST 5 + OWASP 감사
```

## RALF 자기 수복 루프

**RED → GREEN → REFACTOR → LOOP**

- 품질 게이트 실패 시 자동으로 수정 후 재시도
- 3회 진전 없으면 Circuit Breaker 작동
- `--auto --loop` 플래그로 완전 자율 실행

## 코드 파일 300줄 제한

에이전트가 읽기 좋은 코드 설계:
- 1,200줄 파일 → 에이전트가 컨텍스트 중간에 잃어버림
- 300줄 이하 파일 → 하나의 컨텍스트 윈도우에 맞게 전체 파악 가능

## 멀티 모델 오케스트레이션

`--multi` 플래그로 Claude · Codex · Gemini가 서로 검토:
- **Consensus**: 합의 병합
- **Debate**: 적대적 리뷰 + 익명 심판 점수
- **Pipeline**: 이전 모델 출력을 다음 모델 입력으로
- **Fastest**: 첫 완료 응답 사용

## TRUST 5 코드 리뷰

| | 차원 | 검사 항목 |
|---|------|---------|
| **T** | Tested | 85%+ 커버리지, 엣지 케이스, 레이스 컨디션 |
| **R** | Readable | 명확한 명명, 단일 책임, ≤300 LOC |
| **U** | Unified | gofmt, golangci-lint, 일관된 패턴 |
| **S** | Secured | OWASP Top 10, 시크릿 없음 |
| **T** | Trackable | 의미 있는 로그, 에러 컨텍스트, SPEC 참조 |

## Lore 시스템: 코드베이스 기억

모든 커밋에 Why, Decision, Alternatives 구조화된 트레일러 첨부:
```
feat(auth): OAuth2 provider 추상화 추가

Why: Google + GitHub 지원 필요, 추후 확장 가능성
Decision: 직접 SDK 호출 대신 인터페이스 기반 추상화
Alternatives: 직접 SDK 호출 (거절: 과도한 결합)
```

## 관련 개념

- [[에이전트 하네스]]
- [[AX (Agent Experience)]]
- [[멀티에이전트 시스템]]
- [[RALF 루프]]
- [[TRUST 5 코드 리뷰]]
- [[컨텍스트 엔지니어링]]
- [[Claude Code]]
