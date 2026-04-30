---
title: "Progressive Disclosure (점진적 공개)"
type: concept
tags: [ProgressiveDisclosure, 컨텍스트, 에이전트설계, ClaudeCode]
created: 2026-04-29
updated: 2026-04-29
sources: ["Seeing like an agent how we design tools in Claude Code.md"]
---

## 정의

Progressive Disclosure(점진적 공개)는 에이전트가 **필요할 때 점진적으로 관련 컨텍스트를 탐색**하게 하는 기법이다. 모든 정보를 한꺼번에 제공하는 대신, 에이전트가 스스로 필요한 정보를 발견해 나간다.

## 탄생 배경

Claude Code에서 Agent Skills를 도입하면서 공식화:
- skill 파일을 읽으면 다른 파일을 참조
- 에이전트가 그 파일을 재귀적으로 읽음
- 필요한 컨텍스트를 여러 레이어에 걸쳐 발견

## 도구 추가 vs. Progressive Disclosure

| 방식 | 장점 | 단점 |
|------|------|------|
| **새 도구 추가** | 명확한 기능 | 모델 선택지 증가 → 인지 부하 |
| **Progressive Disclosure** | 도구 수 유지 | 파일 구조 설계 필요 |

> Claude Code는 현재 약 20개 도구를 유지하며 자주 필요한지 재검토한다.

## 실제 사례: Claude Code Guide 에이전트

**문제**: Claude Code 사용법 질문에 Claude가 답변 불가

**해결 시도 1**: 시스템 프롬프트에 문서 전체 포함
→ Context rot (불필요한 컨텍스트가 주 작업 방해)

**해결 시도 2**: 문서 링크만 제공
→ Claude가 필요 이상으로 큰 청크를 당겨옴

**최종 해결**: Claude Code Guide **전용 서브에이전트** 생성
- 서브에이전트가 자체 컨텍스트에서 문서 검색
- 메인 에이전트는 답변만 수신
- 메인 컨텍스트 깨끗하게 유지

## RAG → Progressive Disclosure의 전환

| 단계 | 방식 | 특징 |
|------|------|------|
| **초기** | RAG (벡터 DB 사전 인덱싱) | 컨텍스트를 "받는" 방식 |
| **개선** | Grep 도구 | 컨텍스트를 스스로 "찾는" 방식 |
| **현재** | Progressive Disclosure | 여러 레이어에 걸쳐 발견 |

## 관련 개념

- [[컨텍스트 엔지니어링]]
- [[에이전트 도구 설계]]
- [[서브에이전트]]
- [[Claude Code]]
