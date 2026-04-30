---
title: "Claude Code /loop — 자율 루프 3가지 워크플로우"
type: source
tags: [ClaudeCode, 자율에이전트, 워크플로우, CI, 자동화]
created: 2026-04-29
updated: 2026-04-29
sources: ["Claude Code loop — Here Are 3 Autonomous Loops For My Daily Work!.md"]
original_source: "https://medium.com/@alirezarezvani/claude-code-loop-here-are-3-autonomous-loops-for-my-daily-work-f571c61ff9b5"
author: "Reza Rezvani"
published: 2026-03-09
---

## 요약

Claude Code의 `/loop` 명령어를 2주간 실험한 결과를 정리한 글. 크론 잡과 다른 자율 에이전트로서의 특성, 3일 만료 설계의 의도, 그리고 실제로 살아남은 3가지 워크플로우를 소개한다.

## `/loop`란 무엇인가

```bash
claude /loop "failing tests 체크 후 수정" --every 2h --for 3d
```

- **git worktree** (격리된 저장소 복사본)를 생성해 반복 실행
- 매 사이클마다 `CLAUDE.md`를 읽어 컨텍스트를 갱신
- 크론 잡이 아닌, 자율적으로 판단하고 행동하는 에이전트

## 3일 만료 설계의 의도

단순한 제약이 아니라 **의도적 설계**:
- 코드베이스가 변하면 에이전트의 가정도 구식이 됨
- 구식 맥락에서 자율적으로 작업하는 에이전트는 새 문제를 만들어냄
- "3일 제한 = 72시간마다 재평가 강제"라는 스프린트 태스크 사고방식

## 살아남은 3가지 워크플로우

### 1. PR 베이비시팅
```bash
claude /loop "PR CI 실패 시 오류 읽고 수정 후 push" --every 30m --for 2d
```
- lint 실패, 타입 오류, 레이스 컨디션 등 실제 문제 3가지 수정
- flaky 테스트는 "수정"하려 하지 않고 불안정하다는 코멘트 남김

### 2. 의존성 모니터링
```bash
claude /loop "npm audit 실행, 고위험 취약점 발견 시 PR 생성" --every 4h --for 3d
```
- 이상적인 태스크: 명확한 성공 기준, 최소한의 비즈니스 컨텍스트 필요

### 3. 데일리 스탠드업 다이제스트
```bash
claude /loop "지난 24시간 main 커밋 요약 → standup-$(date).md 저장" --every 24h --for 3d
```
- Slack MCP 없이 파일 출력만으로 스탠드업 리포트 자동 생성

## 실패 패턴

- **모호한 태스크**: "더 유지보수하기 좋게 리팩터"처럼 판단이 필요한 지시는 반복마다 다른 결과
- **컨텍스트 드리프트**: 3일 내에도 빠르게 변하는 코드베이스에서 충돌 발생
- **비용**: 30분마다 3일 = 144번 반복 → API 비용 주의

## 핵심 교훈

> CLAUDE.md는 문서가 아니라 두 번째 교대의 운영 매뉴얼이다.

**루프 품질은 지시문의 정확도에 비례한다.**

## 관련 개념

- [[Claude Code]]
- [[자율 에이전트 루프]]
- [[CLAUDE.md]]
- [[컨텍스트 엔지니어링]]
- [[에이전트 하네스]]
