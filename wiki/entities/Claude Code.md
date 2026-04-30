---
title: "Claude Code"
type: entity
tags: [Anthropic, ClaudeCode, AI코딩도구, 에이전트]
created: 2026-04-29
updated: 2026-04-29
sources: ["Claude Code loop — Here Are 3 Autonomous Loops For My Daily Work!.md", "Seeing like an agent how we design tools in Claude Code.md", "클로드 코드 소스 유출에서 배우는 에이전트 구조.md"]
---

## 개요

Claude Code는 Anthropic이 개발한 AI 코딩 도구. 2026년 3월 npm 배포 사고로 소스맵 파일이 유출되어 내부 구조가 공개되었다.

## 주요 특징

- 모든 행동이 **도구 호출(tool calling)**을 통해 이루어짐
- 내부적으로 **42개 이상의 도구**를 상황에 따라 동적 배치
- 모든 대화가 단 하나의 함수 `submitMessage()` 통과
- 메모리 계층: 프로젝트 → 사용자 → 글로벌

## 유출로 드러난 구조

```
submitMessage() → System Prompt 결합 → 도구 동적 배치
→ 컨텍스트 압축 → 모델 호출 → tool_use 감지
→ 권한 정책 평가 → 실행 → 결과 재주입 → 반복
```

## 주요 기능 및 도구

| 기능 | 설명 |
|------|------|
| **CLAUDE.md** | 지속 규칙 파일, 에이전트 운영 매뉴얼 역할 |
| **/loop** | 자율 반복 에이전트 (최대 3일, 격리된 worktree) |
| **Subagents** | 독립된 context window + system prompt + tool access |
| **AskUserQuestion** | 구조화된 질문 도구 (모달 표시 + 루프 차단) |
| **Frustration Detector** | regex 기반 사용자 감정 신호 감지 |

## /loop 명령어

```bash
claude /loop "태스크 설명" --every 2h --for 3d
```

특징:
- git worktree에서 격리 실행
- 매 사이클마다 CLAUDE.md 재독
- **3일 만료**: 구식 컨텍스트에서 동작하는 에이전트 방지

## 도구 설계 철학

"에이전트처럼 보기(Seeing like an agent)":
- 도구는 에이전트의 능력에 맞게 설계
- 모델 역량이 향상되면 기존 도구가 제약이 될 수 있음
- 도구 추가 기준은 높게 유지 (~20개)

## 짜증 감지 기능

```javascript
const NEGATIVE_REGEX = /wtf|wth|ffs|omfg|so frustrating|this sucks/i
analytics.track("tengu_input_prompt", { is_negative: isNegative })
```

활용: 위험 작업 일시 중지, human handoff 후보, 운영 지표

## 관련 개념

- [[에이전트 하네스]]
- [[컨텍스트 엔지니어링]]
- [[Progressive Disclosure (점진적 공개)]]
- [[멀티에이전트 시스템]]
- [[Anthropic]]
