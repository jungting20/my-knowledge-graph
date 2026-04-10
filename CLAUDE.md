# My Knowledge Graph — Schema

LLM이 이 위키를 유지·관리하기 위한 규칙과 워크플로우입니다.

---

## 디렉토리 구조

```
my-knowledge-graph/
├── raw/          # 원본 소스 (불변 — LLM은 읽기만 함)
│   └── assets/   # 이미지 등 첨부 파일
├── wiki/         # LLM이 작성·관리하는 마크다운 페이지
│   ├── index.md  # 전체 페이지 카탈로그 (graphify-out/wiki/index.md가 없을 때만 사용)
│   ├── log.md    # 작업 이력 (append-only)
│   ├── sources/  # 소스 요약 페이지
│   ├── concepts/ # 개념·아이디어 페이지
│   ├── entities/ # 인물·프로젝트·조직 페이지
│   └── analysis/ # 비교·분석·종합 페이지
├── graphify-out/ # graphify가 생성하는 지식 그래프 (자동 생성)
│   ├── GRAPH_REPORT.md   # 그래프 구조 요약 (god nodes, community)
│   └── wiki/index.md     # graphify가 생성한 탐색 인덱스 (우선 사용)
└── CLAUDE.md     # 이 파일
```

---

## 기본 규칙

- **raw/** 파일은 절대 수정하지 않는다.
- **wiki/** 파일만 생성·수정한다.
- 모든 작업 후 `wiki/log.md`에 항목을 추가한다.
- 새 페이지를 만들거나 기존 페이지를 수정하면 `wiki/index.md`를 업데이트한다.
- 페이지 간 교차 참조는 `[[파일명]]` 형식으로 작성한다.
- 모든 wiki 페이지 상단에 YAML frontmatter를 포함한다.
- **모든 wiki 페이지의 본문은 반드시 한국어(한글)로 작성한다.** 영어 고유명사(OIDC, OAuth, API 등)는 그대로 쓰되, 설명·분석·요약 텍스트는 전부 한글로 작성한다.
- **LLM이 사용자에게 응답할 때도 한국어를 기본으로 사용한다.**

---

## YAML Frontmatter 형식

```yaml
---
title: 페이지 제목
type: source | concept | entity | analysis
tags: [태그1, 태그2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [소스파일명1, 소스파일명2]  # 근거가 된 원본 소스
---
```

---

## graphify (주 워크플로우)

이 프로젝트는 graphify 지식 그래프를 중심으로 운영됩니다.

### 탐색 우선순위

1. `graphify-out/wiki/index.md` 가 존재하면 → 이것을 탐색 시작점으로 사용
2. 존재하지 않으면 → `wiki/index.md` 를 사용

### 아키텍처·구조 질문 시

`graphify-out/GRAPH_REPORT.md`를 먼저 읽어 god nodes와 community 구조를 파악한 후 답변한다.

### wiki 파일 수정 후

```bash
python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"
```

위 명령으로 그래프를 최신 상태로 유지한다.

---

## 워크플로우

### 1. Ingest (소스 수집)

새 소스가 `raw/`에 추가되면:

1. 소스를 읽고 핵심 내용을 파악한다
2. `wiki/sources/` 에 요약 페이지를 생성한다
3. 관련 개념·엔티티 페이지를 생성하거나 업데이트한다
4. 새 내용이 기존 내용과 모순되면 해당 페이지에 명시한다
5. `wiki/index.md`를 업데이트한다
6. `wiki/log.md`에 항목을 추가한다: `## [YYYY-MM-DD] ingest | 소스 제목`
7. graphify 그래프를 재빌드한다

### 2. Query (질의 응답)

질문을 받으면:

1. `graphify-out/wiki/index.md` (없으면 `wiki/index.md`)를 읽어 관련 페이지를 파악한다
2. 아키텍처·구조 관련이면 `graphify-out/GRAPH_REPORT.md`를 추가로 읽는다
3. 관련 페이지들을 읽고 답변을 합성한다
4. 답변이 독립적인 가치가 있으면 `wiki/analysis/`에 새 페이지로 저장한다
5. `wiki/log.md`에 항목을 추가한다: `## [YYYY-MM-DD] query | 질문 요약`

### 3. Lint (위키 점검)

점검 요청 시:

- 모순된 내용이 있는 페이지 쌍 찾기
- 인바운드 링크가 없는 고아 페이지 찾기
- 언급은 되지만 페이지가 없는 개념·엔티티 찾기
- 새 소스로 업데이트가 필요한 오래된 내용 찾기
- `wiki/log.md`에 항목을 추가한다: `## [YYYY-MM-DD] lint | 점검 결과 요약`

---

## 로그 빠른 탐색

```bash
grep "^## \[" wiki/log.md | tail -10   # 최근 10개 작업
grep "ingest" wiki/log.md               # 수집 이력만
grep "query" wiki/log.md                # 질의 이력만
```

---

## 세션 시작 시

새 세션을 시작할 때마다:

1. `graphify-out/wiki/index.md` (없으면 `wiki/index.md`)를 읽어 위키 현황을 파악한다
2. `wiki/log.md`의 마지막 5~10개 항목을 읽어 최근 작업을 파악한다
