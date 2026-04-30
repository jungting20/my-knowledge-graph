---
title: "에이전트처럼 보기: Claude Code의 도구 설계 방식"
type: source
tags: [ClaudeCode, 도구설계, 프로그레시브디스클로저, Anthropic, 에이전트UX]
created: 2026-04-29
updated: 2026-04-29
sources: ["Seeing like an agent how we design tools in Claude Code.md"]
original_source: "https://claude.com/blog/seeing-like-an-agent"
author: "Thariq Shihipar (Anthropic)"
published: 2001-04-10
---

## 요약

Anthropic의 Claude Code 팀이 에이전트 도구를 설계하는 방법론을 소개하는 글. 핵심 질문은 "에이전트에게 어떤 도구를 줄 것인가?"이며, 그 답을 "에이전트처럼 보기(Seeing like an agent)"라는 접근법으로 제시한다.

## 도구 설계 철학

> 도구는 에이전트 자신의 능력에 맞게 설계해야 한다.

비유: 어려운 수학 문제를 풀 때 원하는 도구는 자신의 스킬셋에 따라 다르다.
- 종이 → 최소한이지만 수동 계산에 제한
- 계산기 → 더 좋지만 고급 기능 사용법 필요
- 컴퓨터 → 가장 강력하지만 코드 작성 능력 필요

## 사례 1: AskUserQuestion 도구 개발 과정

**시도 1 - ExitPlanTool 확장**: 계획과 질문을 동시에 요청 → 모델 혼란 → 실패

**시도 2 - 출력 형식 변경**: 마크다운 형식으로 질문 리스트 → Claude가 형식을 일관되게 유지하지 못함 → 실패

**시도 3 - 전용 도구 생성**: 모달 표시 + 에이전트 루프 차단 → 성공
- 구조화된 출력 강제 가능
- 사용자에게 다중 선택지 제공
- Claude가 이 도구를 "좋아하는" 것이 중요

## 사례 2: Todo 목록 → Task 도구로 진화

**초기**: TodoWrite 도구로 할 일 목록 관리 + 5턴마다 시스템 알림

**문제**: 모델이 발전하면서 Todo 목록이 제약으로 작용, 방향 전환 어렵게 만듦

**해결**: TodoWrite → **Task 도구**로 교체
- Todo: 모델 추적 중심
- Task: 에이전트 간 소통 중심 (의존성, 업데이트 공유, 수정 가능)

> 모델 역량이 향상되면, 과거에 필요했던 도구가 이제 오히려 제약이 될 수 있다.

## 사례 3: 검색 인터페이스 진화

**초기**: RAG (벡터 데이터베이스 사전 인덱싱) → 컨텍스트를 "받는" 방식

**개선**: Grep 도구 → 컨텍스트를 스스로 "찾는" 방식

**현재**: [[Progressive Disclosure (점진적 공개)]]
- Agent Skills로 파일을 재귀적으로 탐색
- 도구를 추가하지 않고도 기능 확장 가능

## Progressive Disclosure 원칙

**Claude Code Guide 에이전트** 예시:
- 문서 전체를 시스템 프롬프트에 넣으면 컨텍스트 오염 (context rot)
- 문서 링크만 제공하면 필요 없는 대형 청크를 당겨옴
- 해결: Claude Code에 대한 질문을 전담하는 **서브에이전트** 생성
  - 해당 서브에이전트가 문서 검색을 자체 컨텍스트에서 수행
  - 메인 에이전트는 답변만 받음 → 컨텍스트 깨끗하게 유지

## 핵심 교훈

1. **자주 실험하고 출력을 읽어라**
2. **모델 역량에 맞게 도구를 재설계하라**
3. **도구 추가 기준은 높게** — 모델이 생각해야 할 옵션이 하나 더 늘어남
4. **Progressive Disclosure**: 도구 추가 없이 기능을 확장하는 기법

## 관련 개념

- [[Claude Code]]
- [[에이전트 도구 설계]]
- [[Progressive Disclosure (점진적 공개)]]
- [[컨텍스트 엔지니어링]]
- [[서브에이전트]]
