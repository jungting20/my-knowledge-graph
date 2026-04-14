---
title: "Claude Code /loop — Here Are 3 Autonomous Loops For My Daily Work!"
source: "https://medium.com/@alirezarezvani/claude-code-loop-here-are-3-autonomous-loops-for-my-daily-work-f571c61ff9b5"
author:
  - "[[Reza Rezvani]]"
published: 2026-03-09
created: 2026-04-13
description: "Claude Code /loop is not a cron job — it is an autonomous agent that works your second shift. Three workflows that survived two weeks of testing."
tags:
  - "clippings"
---
## I Ran Claude Code /loop for Days. Only 3 Workflows That Survived.

Most engineers hear *“scheduled tasks”* and think cron jobs. A time trigger, a script, a log file nobody checks. The Claude Code loop command is not that. It is closer to handing your night shift to a colleague who already knows your codebase, your conventions, and your PR review standards — then finding three pull requests waiting for you at breakfast.

Boris Cherny, the engineering lead behind Claude Code, runs five parallel Claude instances daily. Twenty to thirty PRs per day. His CLAUDE.md is a living document that evolves with every session. When Anthropic shipped `/loop`, they did not build a scheduler.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2LjA-eZMlZ7LUkWoSuoFAg.png)

Claude Code /loop Feature | Illustration Generated With Gemini 3 Pro ©

***Note:*** *AI tools assisted with researching this article. The setup, workflows, and production context described here are from our OpenClaw instance running daily across engineering, operations, and leadership functions.*

> They built the infrastructure for what Cherny calls *"your second shift."*

I spent the past two weeks testing this. Here is what actually works, what breaks, and why the 3-day expiry is smarter than it looks.

## What /loop Actually Does

The syntax is deceptively simple:

```c
claude /loop "check for failing tests and fix them" --every 2h --for 3d
```

That single line spins up a persistent agent session. Claude Code creates a git worktree *(an isolated copy of your repo)*, executes your instruction, waits for the interval you set, then does it again. Every iteration gets a fresh context pull from your repository state.

The agent reads your CLAUDE.md on each cycle, which means your instructions file becomes the control plane.

3 flags. That is the entire API surface.

## Quick Reference: /loop Command

![Quick Reference for Claude Code /loop command](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9LsZb_K8MfswhAyBOPT-UA.png)

Quick Reference for Claude Code /loop command | Image by Alireza Rezvani ©

**One distinction matters:** `/loop` is the CLI command for developers who live in the terminal. If you are using Claude Desktop's Cowork mode, you will find a similar capability through the scheduled tasks UI — but the mental model differs. Cowork schedules feel like calendar reminders. `/loop` feels like spawning a process.

If you have worked with [other Claude Code commands that automate repetitive work](https://alirezarezvani.medium.com/10-claude-code-commands-that-cut-my-dev-time-60-a-practical-guide-60036faed17f), `/loop` is the natural next step. Same philosophy — delegate the repeatable, keep the creative.

## The 3-Day Expiry Is the Feature, Not the Limitation

My first reaction to the 3-day maximum was frustration. Why cap it? I wanted a loop that monitors my staging environment indefinitely, catches regressions the moment they land, and opens fix PRs without me ever thinking about it.

Cherny’s explanation reframed everything: the expiry is garbage collection for forgotten autonomous agents.

Think about what happens without it. You set up a loop on Tuesday. By Friday, the codebase has shifted — new branches merged, dependencies updated, architectural decisions made in a team meeting you forgot to document. Your loop agent is still operating on Tuesday’s context.

It is not just stale. It is actively dangerous. An agent confidently patching code against outdated assumptions will create problems that take longer to debug than the original issue.

**The 3-day window forces a discipline:** scope your loops like sprint tasks, not like background daemons. If a task is worth running for more than 72 hours, it is worth re-evaluating every 72 hours. Restart the loop with fresh context. Update your CLAUDE.md. Adjust the instruction based on what you learned.

This is not a limitation. It is an opinionated design choice that prevents the most dangerous failure mode of autonomous agents: silent drift.

## Three Workflows That Actually Work

I tested a dozen configurations. Three survived contact with reality.

### Workflow 1: PR Babysitting

This was the first loop I got working reliably. The instruction:

```c
claude /loop "check open PRs on the current branch. If CI is failing,
read the error logs, fix the issue, and push. If CI passes and the PR
has no requested changes, post a comment saying 'Ready for human review.'
Summarize what you did in the PR description." --every 30m --for 2d
```

**What happens in practice:** Claude watches your CI pipeline, catches lint failures and type errors, pushes fixes, and pings you when the PR is actually ready.

I used this on a feature branch with a flaky integration test. Over 48 hours, Claude caught and fixed three legitimate issues *(a missing type import, a race condition in a test fixture, and a stale snapshot).*

It also correctly identified the flaky test as flaky — it added a comment noting the inconsistent failure pattern instead of trying to *“fix”* randomness.

**Where it struggled:** when a CI failure required understanding business logic that was not captured in CLAUDE.md or the codebase. It attempted a fix that was syntactically correct but semantically wrong. I caught it in review.

### Workflow 2: Dependency Monitoring

```c
claude /loop "run npm audit. If any high or critical vulnerabilities exist,
create a branch, update the affected packages, run the test suite, and
open a PR if tests pass. Include the vulnerability details in the PR body."
--every 4h --for 3d
```

This one is a quiet workhorse. Over three days, it caught two high-severity vulnerabilities in transitive dependencies, opened PRs with clean test runs, and included CVE references in the descriptions. The PRs merged without modification.

The key insight: dependency updates are the ideal `/loop` task because they are well-scoped, have clear success criteria (tests pass), and require minimal business context. The agent does not need to understand your product. It needs to understand your dependency graph.

## Workflow 3: Daily Standup Digest

**Cherny mentions running Slack MCP integrations for daily summaries. I replicated a simpler version:**

```c
claude /loop "summarize all commits merged to main in the last 24 hours.
Include: PR titles, authors, files changed count, and any test coverage
changes. Write the summary as a Markdown standup update and save it to
./reports/standup-$(date +%Y-%m-%d).md" --every 24h --for 3d
```

This replaced a manual process that nobody on my team actually did consistently. Three mornings in a row, I had a clean standup report ready before coffee. No Slack MCP required for the basic version — just file output.

**Fair disclosure:***I have not tested the Slack MCP integration that Cherny describes for* [*multi-agent setups*](https://alirezarezvani.medium.com/claude-code-v2-0-44-your-complete-guide-to-native-multi-agent-features-that-actually-work-207be12ed173)*. That is next on my list.*

## Setting Up Your First Loop

Prerequisites are minimal. You need Claude Code CLI installed, a git repository (loops create worktrees, so git is non-negotiable), and a CLAUDE.md file worth reading.

That last part matters more than you think. Without CLAUDE.md, your loop agent operates blind — it has no context about your conventions, your architecture decisions, or your testing philosophy. I wrote about [why context engineering is the foundation of production AI agents](https://alirezarezvani.medium.com/context-engineering-the-complete-guide-to-building-production-ready-ai-coding-agents-6e45ed51e05e) before, and `/loop` makes the argument concrete. Your CLAUDE.md is not documentation. It is the operating manual for your second shift.

### Step-by-step first loop:

1. Open terminal in your repo root
2. Verify Claude Code is installed: `claude --version`
3. Start simple: `claude /loop "run the test suite and report any failures" --every 1h --for 1d`
4. Check status: `claude /loop --status`
5. Stop early if needed: `claude /loop --stop`

**Common gotcha:** worktree permissions. If your repo has submodules or complex git configurations, the worktree creation can fail silently. Test with a simple instruction first before going elaborate.

## Where This Breaks

I would be cheerleading if I stopped at the success stories. Here is where `/loop` falls apart.

**Ambiguous tasks.** Any instruction that requires human judgment mid-execution — “refactor this module to be more maintainable” — produces inconsistent results across iterations. The agent interprets “maintainable” differently each cycle. Scope your instructions to specific, verifiable outcomes.

**Context drift.** Even within 3 days, a fast-moving codebase can shift enough to invalidate loop assumptions. If your team merges 15 PRs while your loop is running on a worktree branched from Monday morning, the fixes it proposes may conflict with work that landed Tuesday afternoon.

**Cost awareness.** Each loop iteration is an API call. A loop running every 30 minutes for 3 days is 144 iterations. If each iteration processes significant context, you are looking at meaningful API costs. I did not track exact numbers, but the bill was noticeable after running three concurrent loops for a week.

**The trust calibration problem.** The hardest part is not technical. It is deciding how much autonomy to grant. A loop that pushes directly to a feature branch? Reasonable. A loop that auto-merges its own PRs? That is a conversation your team needs to have before someone sets it up.

## The Bigger Question

Cherny describes `/loop` as building *"the colleague who works your second shift."* That framing is revealing. We are not building better cron jobs. We are building relationships with autonomous agents — relationships that require trust, boundaries, and periodic check-ins. The same dynamics that make human delegation hard apply here.

After two weeks of running loops, my honest assessment: `/loop` is genuinely powerful for well-scoped, repeatable tasks with clear success criteria. PR babysitting and dependency monitoring are the sweet spots. The 3-day expiry is wise. The worktree isolation prevents disasters.

But the temptation to over-delegate is real. I caught myself writing increasingly vague instructions, hoping Claude would figure it out. It did not.

> The best loops are the ones where I spent 10 minutes writing a precise instruction — the same way I would write a clear ticket for a junior engineer.

Maybe that is the real lesson. `/loop` does not replace thinking about what you want done. It replaces doing it yourself at 2 AM.

## Key Takeaways

- `**/loop**` **is an autonomous agent, not a cron job** — it creates isolated worktrees, reads your CLAUDE.md each cycle, and makes contextual decisions. Think sprint teammate, not background script.
- **The 3-day expiry prevents silent drift** — autonomous agents operating on stale context are more dangerous than no agent at all. The cap forces you to re-evaluate and restart with fresh context.
- **Start with well-scoped, verifiable tasks** — PR babysitting and dependency monitoring work because success criteria are clear. Vague instructions produce vague results.
- **Your CLAUDE.md is the control plane** — the quality of your loop output directly correlates with the quality of your context engineering. Invest in your instructions file before investing in loops.

**Check out my Open Source Claude Skills & Plugins Repository:**

## [GitHub - alirezarezvani/claude-skills: 169 production-ready skills & plugins for Claude Code…](https://github.com/alirezarezvani/claude-skills?source=post_page-----f571c61ff9b5---------------------------------------)

### 169 production-ready skills &amp; plugins for Claude Code, OpenAI Codex, and OpenClaw - engineering, marketing…

github.com

## Responses (4)

담심 (담심)

What are your thoughts?

  

```c
this sounds useful for throughput, but without hard data on defect density or post-merge rework it is basically anecdotal; at least compare loop-generated prs against human baselines like in the swan or code alpaca evals
```

6

```c
Thanks Reza for this blog. great insight and able to connect on similar grounds
```

3[Apoufortin](https://medium.com/@apoufortin?source=post_page---post_responses--f571c61ff9b5----2-----------------------------------)

[

Mar 11

](https://medium.com/@apoufortin/how-does-the-loop-agent-work-with-permissions-58aaea47bba1?source=post_page---post_responses--f571c61ff9b5----2-----------------------------------)

```c
How does the loop agent work with permissions? Does it depend on your project settings or does it auto grant everything?
```

3