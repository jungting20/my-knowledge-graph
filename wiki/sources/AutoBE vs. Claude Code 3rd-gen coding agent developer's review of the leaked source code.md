---
title: "AutoBE vs. Claude Code: 3세대 코딩 에이전트 개발자의 유출 소스 코드 리뷰"
type: source
tags: [AI에이전트, FunctionCalling, Agentica, TypeScript, MCP]
created: 2026-04-29
updated: 2026-04-29
sources: ["AutoBE vs. Claude Code 3rd-gen coding agent developer's review of the leaked source code.md"]
original_source: "https://dev.to/samchon/agentica-do-you-know-function-then-youre-ai-developer-1d9d"
author: samchon
published: 2025-04-29
---

## 요약

TypeScript AI 프레임워크 [[Agentica]]를 소개하는 글. "함수를 만들 줄 안다면 AI 개발자"라는 철학 아래, Function Calling을 핵심으로 삼아 TypeScript 클래스, Swagger/OpenAPI 문서, MCP 서버를 통합하는 방식으로 AI 에이전트를 구축하는 접근법을 설명한다.

## 핵심 개념

### AI Function Calling의 부활

OpenAI가 2023년 6월에 발표한 [[AI Function Calling]]은 초기 복잡한 스펙과 낮은 성공률로 인해 주류가 되지 못했다. 대신 특수 목적 에이전트 워크플로우가 유행했으나, Agentica는 이 패러다임을 되살리고자 4가지 전략을 사용한다:

1. **Compiler Driven Development**: 컴파일러가 function calling 스키마를 자동 생성
2. **JSON Schema Conversion**: LLM 벤더 간 스펙 차이를 자동 처리
3. **Validation Feedback**: AI의 인자 조합 오류를 감지·수정
4. **Selector Agent**: 후보 함수를 필터링해 컨텍스트 사용 최적화

### 통합 방식

- **TypeScript 클래스**: `typia.llm.application<ClassName, Model>()` 으로 AI 에이전트에 클래스 함수를 노출
- **Swagger/OpenAPI**: 백엔드 `swagger.json` 파일만 제공하면 289개 API 함수도 모두 이해
- **MCP 서버**: Claude Desktop에서 8/10 실패하는 GitHub MCP가 Agentica 통해서는 100% 성공

## 시사점

- 함수 기반 AI 개발은 백엔드 개발자에게 유리한 패러다임
- 복잡한 UI 없이 "함수"만 정의하면 AI 에이전트 구축 가능
- [[하네스 엔지니어링]]의 중요성: 에이전트를 감싸는 실행 구조가 완성도를 좌우

## 관련 개념

- [[AI Function Calling]]
- [[Agentica]]
- [[MCP (Model Context Protocol)]]
- [[에이전트 하네스]]
