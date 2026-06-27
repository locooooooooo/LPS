# PM Orchestration System

Shareable Codex skill for PM dispatch, long-worker and short-worker execution, goal-mode control, version planning, callback collection, and end-of-day closure.

## What this skill does

- Runs a structured PM protocol across multiple threads
- Separates `PM`, `Supervisor`, `Long-worker`, `Short-worker`, and `Acceptance` roles
- Uses identity headers in the form `[role]#module@version`
- Uses tag-based handoff with `tag:v2`
- Defaults to summary-package delivery instead of full `git diff`
- Keeps `git`, archive, and validation behavior as optional modules

## Repository layout

```text
.
├── SKILL.md
├── README.md
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

## Install

Option 1: clone directly into your Codex skills directory.

```powershell
git clone https://github.com/locooooooooo/LPS.git "$HOME/.codex/skills/pm-orchestration-system"
```

Option 2: clone anywhere, then copy this folder into `~/.codex/skills/pm-orchestration-system`.

## Use

Call the skill explicitly:

```text
Use $pm-orchestration-system to run [PM]#today-plan@2026-06-27 in goal mode with optional modules archive,git.
```

Generate a starter prompt pack:

```powershell
python scripts/render_prompt_pack.py --role pm --module today-plan --version 2026-06-27 --mode goal --modules core,archive,git
```

## Optional modules

The core skill works by itself. Activate optional modules only when needed:

- `git`
- `archive`
- `validation`
- repo-local handoff protocol

## Notes

- `Long-worker` is for one large module only.
- `Short-worker` is day-close only.
- Full `git diff` is not the default delivery surface.
