---
title: "Agentica"
type: entity
tags: [Agentica, TypeScript, FunctionCalling, wrtnlabs, AI프레임워크]
created: 2026-04-29
updated: 2026-04-29
sources: ["AutoBE vs. Claude Code 3rd-gen coding agent developer's review of the leaked source code.md"]
---

## 개요

Agentica는 [wrtnlabs](https://github.com/wrtnlabs/agentica)가 개발한 TypeScript AI 프레임워크로, Function Calling을 전문으로 한다. "함수를 만들 줄 안다면 AI 개발자"라는 철학을 기반으로 한다.

## 지원 통합 방식

1. **TypeScript 클래스**: `typia.llm.application<ClassName, Model>()` 으로 자동 스키마 생성
2. **Swagger/OpenAPI 문서**: `swagger.json`만 제공하면 모든 API 함수 자동 이해
3. **MCP 서버**: Claude Desktop 대비 훨씬 높은 성공률 (100% vs 2/10)

## 4가지 핵심 전략

| 전략 | 설명 |
|------|------|
| Compiler Driven Development | 컴파일러가 function calling 스키마 자동 생성 |
| JSON Schema Conversion | LLM 벤더 간 스펙 차이 자동 처리 |
| Validation Feedback | AI의 인자 조합 오류 감지·수정 |
| Selector Agent | 후보 함수 필터링으로 컨텍스트 최적화 |

## 코드 예시

```typescript
import { Agentica } from "@agentica/core";
import typia from "typia";

const agent = new Agentica({
  vendor: { api: new OpenAI({ apiKey: "..." }), model: "gpt-4o-mini" },
  controllers: [{
    protocol: "class",
    name: "filesystem",
    application: typia.llm.application<FileSystem, "chatgpt">(),
    execute: new FileSystem(),
  }],
});
await agent.conversate("파일 정리해줘");
```

## 강점

- GitHub MCP: Claude Desktop에서 8/10 실패 → Agentica에서 100% 성공
- 289개 API 함수도 한 번에 처리 가능
- 5분 만에 컴퓨터 파일 제어 AI 에이전트 구축 가능

## 관련 개념

- [[AI Function Calling]]
- [[MCP (Model Context Protocol)]]
- [[에이전트 하네스]]
