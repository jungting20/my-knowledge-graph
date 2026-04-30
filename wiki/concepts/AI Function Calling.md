---
title: "AI Function Calling"
type: concept
tags: [FunctionCalling, AI, OpenAI, Agentica, 도구호출]
created: 2026-04-29
updated: 2026-04-29
sources: ["AutoBE vs. Claude Code 3rd-gen coding agent developer's review of the leaked source code.md"]
---

## 정의

AI Function Calling은 개발자가 함수를 제공하면 AI가 적절한 함수를 선택하고 파라미터 값을 채워 실행하는 기술이다. OpenAI가 2023년 6월에 발표했다.

## 역사

- **2023년 6월**: OpenAI 발표 → 많은 개발자들이 "함수만 만들면 AI가 다 해결"이라는 비전 공유
- **이후**: 복잡한 스펙과 낮은 파라미터 조합 성공률로 주류화 실패
- **대안**: 특수 목적 에이전트 워크플로우가 주류로 떠오름
- **MCP 등장**: 인기를 얻었으나 불안정성 비판으로 에이전트 워크플로우로 회귀
- **현재**: [[Agentica]] 등이 Function Calling을 부활시키려 시도

## 왜 실패했나 (초기)

1. **복잡한 스펙**: LLM 벤더마다 다른 JSON Schema 형식
2. **낮은 성공률**: 파라미터 값 조합에서 AI 오류 빈번
3. **컨텍스트 과부하**: 함수 수가 늘어날수록 성능 저하

## Agentica의 해결책 4가지

1. **Compiler Driven Development**: 컴파일러가 function calling 스키마 자동 생성
2. **JSON Schema Conversion**: LLM 벤더 간 스펙 차이 자동 처리
3. **Validation Feedback**: AI의 인자 조합 오류 감지·수정
4. **Selector Agent**: 후보 함수를 필터링해 컨텍스트 최적화

## Claude Code와의 관계

Claude Code의 모든 행동이 도구 호출을 통해 이루어진다:
- 파일 읽기/쓰기
- 터미널 명령 실행
- 외부 API 호출 (MCP 포함)
- 42개+ 도구를 상황에 따라 동적 배치

## 관련 개념

- [[Agentica]]
- [[MCP (Model Context Protocol)]]
- [[에이전트 하네스]]
- [[Claude Code]]
