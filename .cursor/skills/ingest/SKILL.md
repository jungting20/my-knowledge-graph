---
name: ingest
description: raw/ 폴더의 소스 파일을 읽어 wiki/ 페이지를 생성·업데이트하는 지식 그래프 수집 워크플로우. "/ingest", "ingest 해줘", "raw 업데이트", "wiki 반영", "소스 수집" 등의 요청 시 사용.
---

# Ingest

`raw/`에 있는 소스 파일을 wiki 페이지로 변환하는 워크플로우.

## 실행 방법

사용자가 `/ingest` 또는 "ingest 해줘"라고 하면 아래 순서를 따른다.

## 워크플로우

### 1. raw/ 파일 목록 파악

`wiki/log.md`의 ingest 이력과 `wiki/sources/` 디렉토리를 확인해 이미 반영된 소스와 아직 반영되지 않은 소스를 구분한다.

### 2. 소스별 처리 (미반영 파일만)

각 소스 파일에 대해:

1. **소스 읽기** — `raw/<파일명>` 내용 파악
2. **`wiki/sources/<파일명>.md` 생성** — 아래 frontmatter + 한글 요약
3. **개념/엔티티 페이지 생성·업데이트** — `wiki/concepts/`, `wiki/entities/`
4. **모순 발견 시** — 해당 페이지 상단에 `> ⚠️ 모순: ...` 형식으로 명시

### 3. wiki/index.md 업데이트
새로 생성된 페이지를 카탈로그에 추가.

### 4. wiki/log.md에 기록
```
## [YYYY-MM-DD] ingest | <소스 제목>
```

### 5. graphify 그래프 재빌드

```bash
python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"
```

## 페이지 frontmatter 형식

```yaml
---
title: 페이지 제목
type: source | concept | entity | analysis
tags: [태그1, 태그2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [소스파일명]
---
```

## 규칙

- 본문은 **반드시 한국어**로 작성 (영어 고유명사 제외)
- `raw/` 파일은 절대 수정하지 않는다
- 페이지 간 교차 참조는 `[[파일명]]` 형식 사용
