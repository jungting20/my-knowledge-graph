#!/usr/bin/env python3
"""raw/ 파일 중 wiki/sources/ 에 반영되지 않은 파일을 출력한다."""

from pathlib import Path

ROOT = Path(__file__).parents[4]  # my-knowledge-graph/
RAW = ROOT / "raw"
SOURCES = ROOT / "wiki" / "sources"

IGNORE = {"assets"}

def main():
    raw_files = [
        f for f in RAW.iterdir()
        if f.is_file() and f.name not in IGNORE
    ]

    done, pending = [], []
    for f in raw_files:
        wiki_page = SOURCES / f"{f.stem}.md"
        if wiki_page.exists():
            done.append(f.name)
        else:
            pending.append(f.name)

    if pending:
        print("=== 미반영 소스 ===")
        for name in pending:
            print(f"  • {name}")
    else:
        print("모든 소스가 wiki에 반영되어 있습니다.")

    if done:
        print("\n=== 이미 반영된 소스 ===")
        for name in done:
            print(f"  ✓ {name}")

if __name__ == "__main__":
    main()
