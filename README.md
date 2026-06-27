# PM Orchestration System

Shareable Codex skill for PM dispatch, long-worker and short-worker execution, goal-mode control, version planning, callback collection, and day-close closure.

## What it is

A compact operating layer for multi-thread PM work.
It keeps one truth source, one active goal, one module owner when needed, and one summary-package delivery style.

## Why use it

- Dispatch PM, supervisor, long-worker, short-worker, and acceptance threads with one protocol
- Keep long-worker ownership limited to one large module
- Keep short-worker lanes day-close only
- Keep `git`, archive, and validation behavior optional
- Keep delivery compact instead of defaulting to full `git diff`

## Quick start

1. Clone this repository into your Codex skills directory.

```powershell
git clone https://github.com/locooooooooo/LPS.git "$HOME/.codex/skills/pm-orchestration-system"
```

2. Call the skill explicitly.

```text
Use $pm-orchestration-system to run [PM]#today-plan@2026-06-27 in goal mode with optional modules archive,git.
```

3. Generate a starter prompt pack.

```powershell
python scripts/render_prompt_pack.py --role pm --module today-plan --version 2026-06-27 --mode goal --modules core,archive,git
```

## Roles

- `PM`: dispatch, acceptance, correction, close-out
- `Supervisor`: inspect drift and issue minimal corrections
- `Long-worker`: own one large module only
- `Short-worker`: bounded execution and day-close
- `Acceptance`: verify behavior and evidence

## Identity format

Use:

```text
[role]#module@version
```

Examples:

- `[PM]#today-plan@2026-06-27`
- `[Long-worker]#adventure@v1.0`
- `[Short-worker]#blocked-fix@v0.1`

## Optional modules

Activate only when needed:

- `git`
- `archive`
- `validation`
- repo-local handoff protocol

## Repository files

- `SKILL.md`
- `agents/openai.yaml`
- `references/protocol-core.md`
- `references/version-planning.md`
- `references/goal-mode-prompts.md`
- `references/optional-modules.md`
- `references/repo-protocol-bootstrap.md`
- `references/self-iteration.md`
- `scripts/render_prompt_pack.py`

## 中文说明

中文版见 [README.zh-CN.md](README.zh-CN.md).
