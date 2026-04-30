---
title: "Ralph Loops: Teaching Claude Code to Work While You Sleep"
source: "https://medium.com/@davidroliver/ralph-loops-teaching-claude-code-to-work-while-you-sleep-aebb434b4432"
author:
  - "[[David R Oliver]]"
published: 2026-03-25
created: 2026-04-30
description: "More"
tags:
  - "clippings"
---
Automate Claude Code with bash loops, structured JSON output, and zero babysitting

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*4sFn1gOHOiGamNgu)

Photo by Simon Infanger on Unsplash

I have a book with 99 cognitive biases and an Obsidian vault that needed a structured note for each one. Each note needed YAML frontmatter with a dozen fields, a classification (bias, fallacy, heuristic, illusion, or effect), three domain-specific examples, counter-strategies, and academic references. Doing this interactively — one conversation per bias — would have meant 99 separate Claude Code sessions. That’s not a task. That’s a punishment!

So I built a loop. Then it broke. Then I built a better one. Then *that* broke. The third version processed 54 notes in 14 minutes without a single failure.

This is the story of what I learnt. If you’ve used Claude Code interactively but never automated it, this is your on-ramp.

## Act 1: The Machine

## What’s claude -p?

When you use Claude Code normally, you’re in an interactive session — typing prompts, reading responses, approving tool calls. But Claude Code has a headless mode: `claude -p`. You pipe in a prompt, it runs without interaction, and returns the output. No human in the loop.

```c
echo "Summarise this file" | claude -p --model sonnet
```

That’s the building block. One call, one task, one output.

## The Loop Pattern

A Ralph Loop takes `claude -p` and wraps it in a bash script that runs it repeatedly. The pattern has three parts:

1. **A tracker file** — a markdown checklist that records what’s done and what’s left. This survives across iterations. When the loop starts each cycle, it reads the tracker to find the next batch of unchecked items.
2. **A prompt file** — the instructions for each iteration. “Here are the next 9 biases. Create a Concept note for each one. Output them as JSON.”
3. **A bash wrapper** — the script that orchestrates everything. Read the tracker. Build the prompt. Call Claude. Process the output. Update the tracker. Commit. Loop.

Here’s the skeleton:

```c
while true; do
  # What's left to do?
  unchecked=$(grep '^\- \[ \]' tracker.md | head -n 9)
if [ -z "$unchecked" ]; then
    echo "Done!"
    break
  fi
  # Ask Claude to do it
  response=$(echo "$prompt" | claude -p --model sonnet ...)
  # Process the response, update tracker, commit
  # ...
done
```

The `--dangerously-skip-permissions` flag lets it run without asking for approval on each tool call. That sounds scary, but the safety model is different for loops: you review the plan and the prompt *before* launching. That's your approval gate. Once you've read what it's going to do and you're satisfied, you let it run.

## Version 1

My first Ralph Loop was ambitious. The prompt was 270 lines long. It instructed Claude to:

- Read the tracker file to find the next 3 unchecked biases
- Search the vault for existing notes that might need merging
- Web-search to verify Dobelli chapter numbers and academic citations
- Create three-tier notes (Quick Reference, Working Knowledge, Deep Dive)
- Update the tracker with progress
- Commit everything to git

I used Opus (the most capable model), gave it full tool access, and let it run. It worked beautifully. For about 45 minutes. Then it hit the usage limit. I waited for the limit to reset and ran it again. It processed another 30 biases and hit the limit again.

After two sessions and several hours of wall clock time, I had 45 of 99 biases completed. The loop *worked* — it just consumed tokens like a furnace.

## Act 2: The Mess

## Episode 1: Where did all the tokens go?

I started counting. Every time `claude -p` is called, even before your prompt is processed, it loads your entire Claude Code environment:

- **CLAUDE.md** — your project instructions
- `**.claude/rules/**` — all your rule files
- **MCP tool schemas** — every connected service (Notion, Atlassian, Hostinger — over 100 tool definitions in my case)
- **Auto-memory** — your MEMORY.md index

For my vault, that was roughly 50,000 tokens of context *before the prompt even arrived*. Multiply that by 15 iterations, and you’ve burnt 750,000 tokens just on boilerplate. Add the web searches (each spawning sub-agents), the three-tier note content, and the tool calls for file writing — and it’s obvious why two sessions weren’t enough.

**Lesson: know what’s in your context window.** The tokens you can see (your prompt) are often dwarfed by the tokens you can’t (your environment).

## Episode 2: The flag that broke everything

I researched optimisations and found two promising flags:

`**--bare**` — strips out CLAUDE.md, rules, MCP tools, hooks, and auto-memory. Everything. Just your prompt and the model. This would eliminate that 50,000-token overhead entirely.

I tried it. Silent failure. No error message, just: “Not logged in.”

It turns out `--bare` skips the keychain, which is how the Max subscription authenticates. It only works if you have an `ANTHROPIC_API_KEY` environment variable set. If you're on a subscription plan, `--bare` is a brick wall.

`**--json-schema**` — forces the model to output valid JSON matching a schema. Perfect for structured note generation. I wrote a schema file and pointed to it:

```c
claude -p --json-schema ./my-schema.json  # Hangs forever
```

It hung. No output, no error. I waited five minutes and killed it.

On a hunch, I tried the same schema as an inline string:

```c
claude -p --json-schema '{"type":"object",...}'  # Works instantly
```

Same schema, same content. File path hangs, inline works.

**Lesson: dry-run with a single item before launching a loop.** I found both of these bugs in two minutes with one test call. If I’d launched a full loop, I’d have waited for an hour of silence before realising something was wrong.

## Episode 3: Eighteen notes of silence

Emboldened by the working flags, I cranked the batch size from 3 to 18. Fewer iterations, fewer context reloads. Simple maths.

The call never returned. The model was trying to generate 18 complete markdown notes as a single JSON response — roughly 25,000 tokens of structured output. Too much.

I tested with 1. Worked. Tested with 3. Worked. Tested with 9. Worked. Tested with 18. Silence.

**Lesson: escalate batch size gradually.** 1 → 3 → 9 → target. Don’t guess. Test.

## Act 3: The Fix

## The key insight

Version 1 treated the LLM as a full-stack worker. It read files, searched the web, wrote files, updated progress, and committed to git. Every one of those actions used tools, and every tool call consumed tokens — both for the tool schemas in context and the back-and-forth of tool use.

The fix was obvious in hindsight: **make the script smarter so the LLM can be dumber.**

Version 3 split responsibilities cleanly:

**The bash script handles:**

- Reading the tracker to find unchecked biases
- Globbing the vault for existing notes (for cross-references)
- Building the prompt with all data pre-injected
- Calling `claude -p` with minimal flags
- Parsing the JSON response
- Writing each file to disk
- Ticking checkboxes in the tracker
- Updating progress counts
- Committing to git

**The LLM handles:**

- Generating note content

That’s it. One job. No tool calls, no file reads, no web searches, no git operations. The model receives a prompt with everything it needs and returns structured JSON. The script does the rest.

## The flags that made it work

```c
claude -p - \
  --model sonnet \
  --output-format json \
  --json-schema '{"type":"object","properties":{"files":{"type":"array",...}}}' \
  --tools "" \
  --dangerously-skip-permissions
```
![](https://miro.medium.com/v2/resize:fit:1384/format:webp/1*G41UyS_lx_LDafAxRz3qcQ.png)

The script extracts the files array from the response and writes each one:

```c
response=$(echo "$prompt" | claude -p - --model sonnet ...)

file_count=$(echo "$response" | jq '.structured_output.files | length')

for i in $(seq 0 $((file_count - 1))); do
  fname=$(echo "$response" | jq -r ".structured_output.files[$i].file_name")
  fcontent=$(echo "$response" | jq -r ".structured_output.files[$i].content")
  echo "$fcontent" > "$fname"
done
```

## The numbers

![](https://miro.medium.com/v2/resize:fit:1140/format:webp/1*NjYyo65L8wrdAg4tDCdCKA.png)

That’s roughly a 95% reduction in token consumption.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pCE7AktEc8bLiGRab47naw.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pip1K0YTmNlVgmHXnV41SQ.png)

## What about monitoring?

We built a status file that the script updates at each phase transition — a markdown file with a progress bar, current phase, elapsed time, and ETA. You watch it in a terminal:

```c
while true; do clear; cat .claude/tmp/status.md; sleep 2; done
```

Honest assessment: it’s limited. The status updates between phases (starting → generating → writing → committing), but during the Sonnet call itself — which takes 2–3 minutes per batch and is most of the wall-clock time — the dashboard is frozen. It’s checkpoint-based, not streaming. You see it jump in bursts.

For a future version, this needs work. Possibly tailing the Claude process output, or using a webhook pattern. For now, `tail -f` on a log file is the more honest alternative.

## The Template

Here’s a generic Ralph Loop you can adapt for any batch task. It’s not the full 99-bias script — it’s the reusable skeleton.

## Script

```c
#!/bin/bash
set -euo pipefail
TRACKER="tracker.md"
BATCH_SIZE=9
SCHEMA='{"type":"object","properties":{"files":{"type":"array","items":{"type":"object","required":["name","content"],"properties":{"name":{"type":"string"},"content":{"type":"string"}}}}},"required":["files"]}'
while true; do
  # 1. Read tracker
  unchecked=$(grep '^\- \[ \]' "$TRACKER" | head -n "$BATCH_SIZE")
  count=$(echo "$unchecked" | grep -c '.' || true)
  [ "$count" -eq 0 ] && echo "Done!" && break
  # 2. Build prompt (inject data the LLM needs)
  prompt="Your instructions here.
Items to process:
$unchecked"
  # 3. Call Claude
  response=$(echo "$prompt" | claude -p - \
    --model sonnet \
    --output-format json \
    --json-schema "$SCHEMA" \
    --tools "" \
    --dangerously-skip-permissions)
  # 4. Write files from JSON
  file_count=$(echo "$response" | jq '.structured_output.files | length')
  for i in $(seq 0 $((file_count - 1))); do
    name=$(echo "$response" | jq -r ".structured_output.files[$i].name")
    content=$(echo "$response" | jq -r ".structured_output.files[$i].content")
    echo "$content" > "$name"
  done
  # 5. Tick tracker and commit
  # (your sed/awk logic here)
  git add -A && git commit -m "Processed batch of $count"
done
```

## Flag Cheatsheet

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LFQhSsrqDie2UoOqtBjuCA.png)

## The Five Gotchas

1. `**--bare**` **needs an API key.** If you're on a Pro or Max subscription, it `--bare` silently fails to authenticate. You need `ANTHROPIC_API_KEY` set as an environment variable.
2. `**--json-schema**` **needs inline JSON.** Passing a file path (`--json-schema schema.json`) hangs indefinitely. Pass the schema as a string instead.
3. **Dry-run with one item first.** Before launching a loop, run the exact `claude -p` command with a single item. Verify auth works, output parses, and content is acceptable.
4. **Escalate batch size gradually.** Test at 1, then 3, then your target. Large structured JSON responses can stall if they exceed the model’s output token budget.
5. **Monitoring is checkpoint-based.** Status files only update between phases. During generation, the dashboard is frozen. For now, accept this limitation or use `tail -f` on a log file.

## What I’d Do Differently Next Time

- **Error recovery.** If a Sonnet call fails, the script currently crashes. A retry with a smaller batch would be more resilient.
- **Parallel batches.** Nothing stops you from running two loops on different ranges simultaneously, as long as they write to different files.
- **Streaming monitoring.** Hook into the Claude process output rather than relying on phase-transition checkpoints.
- **Validation pass.** After the loop completes, run a separate verification loop that spot-checks the generated content against a quality rubric.