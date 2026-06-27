# PM Orchestration System

> Shareable Codex skill for PM dispatch, long-worker and short-worker execution, goal-mode control, version planning, callback collection, archive flow, and summary-package delivery.

[中文](README.md)

## What it is

A compact operating layer for multi-thread PM work.

It solves coordination problems such as:

- who dispatches
- who supervises and corrects drift
- which work belongs to a long-worker vs a short-worker
- how to open and close a version plan
- how to avoid wasting tokens on full `git diff` by default

## Quick start

### 1. Install into your Codex skills directory

```powershell
git clone https://github.com/locooooooooo/LPS.git "$HOME/.codex/skills/pm-orchestration-system"
```

### 2. Invoke the skill explicitly

```text
Use $pm-orchestration-system to run [PM]#today-plan@2026-06-27 in goal mode with optional modules archive,git.
```

### 3. Generate a starter prompt pack

```powershell
python scripts/render_prompt_pack.py --role pm --module today-plan --version 2026-06-27 --mode goal --modules core,archive,git
```

## Where it fits

- PM dispatch and close-out
- one large-module owner per long-worker
- same-day closure for short-workers
- version-plan based execution
- optional `git`, archive, and validation modules

## Core rules

### Identity header

Use:

```text
[role]#module@version
```

Examples:

- `[PM]#today-plan@2026-06-27`
- `[Long-worker]#adventure@v1.0`
- `[Short-worker]#blocked-fix@v0.1`

### Role boundaries

| Role | Responsibility |
| --- | --- |
| `PM` | dispatch, acceptance, correction, close-out |
| `Supervisor` | inspect drift and issue minimal corrections |
| `Long-worker` | own one large module only |
| `Short-worker` | bounded execution and day-close |
| `Acceptance` | verify behavior, evidence, and rollback surface |

### Delivery rule

Default delivery is:

- changed files
- key behavior change
- verification result
- risk / rollback

Do not default to full `git diff`.  
Only expand to a minimal patch when review, conflict analysis, or explicit request requires it.

## Optional modules

Use only when needed:

- `git`
- `archive`
- `validation`
- repo-local handoff protocol

## Repository layout

```text
.
├── SKILL.md
├── README.md
├── README.en.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── protocol-core.md
│   ├── version-planning.md
│   ├── goal-mode-prompts.md
│   ├── optional-modules.md
│   ├── repo-protocol-bootstrap.md
│   └── self-iteration.md
└── scripts/
    └── render_prompt_pack.py
```
