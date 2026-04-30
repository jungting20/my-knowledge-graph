---
title: "Neovim 0.12.0을 위한 설정 리프레시"
type: source
tags: [Neovim, 설정, LSP, Treesitter, 플러그인관리]
created: 2026-04-29
updated: 2026-04-29
sources: ["Refreshing your Neovim config for 0.12.0.md"]
original_source: "https://justinhj.github.io/2026/04/06/refreshing-your-neovim-config-for-0-12-0.html"
author: "Functional[Justin]"
published: 2026-04-06
---

## 요약

Neovim 0.12.x의 대규모 업데이트(외부 플러그인 기능들이 빌트인으로 통합)를 계기로 설정을 전면 재구성한 경험 공유. 핵심 변경사항: 새 플러그인 매니저 `vim.pack`, 빌트인 LSP 완성, `ui2` 등.

## 주요 변경사항

### vim.pack — 빌트인 플러그인 매니저

lazy.nvim에서 이전:
```lua
-- lazy.nvim 방식
{ 'shaunsingh/nord.nvim', lazy = false, priority = 1000, config = ... }

-- vim.pack 방식
vim.pack.add({ { src = "https://github.com/shaunsingh/nord.nvim" } })
vim.cmd('colorscheme nord')
```

- 레이지 로딩 없음 → 단순함
- 원격 git 저장소만 지원
- lock 파일로 버전 고정 (머신 간 재현 가능)
- `:restart` 명령어로 세션 유지하며 재시작

### 빌트인 LSP 완성

nvim-cmp + LuaSnip 제거 → 네이티브 완성으로:
```lua
vim.o.autocomplete = true

-- LspAttach 시 활성화
vim.lsp.completion.enable(true, client_id, args.buf, { autotrigger = true })
```

**모듈식 LSP 설정**: `lsp/` 폴더에 서버명으로 파일 생성 (예: `lsp/pylsp.lua`)

### ui2 — 새 UI 시스템

```lua
require('vim._core.ui2').enable({})
```
- "Press Enter" 중단 제거
- 입력 중 명령줄 강조 표시

## 병렬 설정 운영

`NVIM_APPNAME` 환경 변수로 구설정과 신설정 병행:
```bash
NVIM_APPNAME=nvim-next nvim
```

## 유지한 플러그인 목록

| 플러그인 | 용도 |
|---------|------|
| mason, mason-lspconfig | LSP 서버 관리 |
| nvim-treesitter | 문법 강조 |
| nord.nvim | 컬러스킴 |
| legendary.nvim | 키맵 관리 |
| fzf-lua | 빠른 파일/텍스트 검색 |
| lualine.nvim | 상태바 |
| which-key.nvim | 키맵 표시 |

## 관련 개념

- [[Neovim]]
- [[LSP (Language Server Protocol)]]
- [[Treesitter]]
