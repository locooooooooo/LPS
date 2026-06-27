---
name: pm-orchestration-system
description: PM orchestration skill for multi-session planning, dispatch, acceptance, and iteration control. Use when Codex needs to run a structured PM system with roles such as PM, supervisor, long-worker, and short-worker; manage goal-mode execution; maintain version plans and day-close rules; enforce tag-based handoff; or package delivery as summary bundles instead of full git diff. Also use when a team wants optional modules such as git workflow, archive rules, or callback templates to be plugged in without changing the core protocol.
---

# PM Orchestration System

## Overview

Use this skill to run a reusable PM control system across threads, roles, and day-level loops.
Keep the core small: one truth source, one active goal, one dispatch surface, and explicit close-out rules.

## Core workflow

1. Restate the operating target.
- Identify whether the request is about PM dispatch, long-worker execution, short-worker closure, version planning, blocked repair, or end-of-day review.
- Do not mix multiple top-level goals unless the user explicitly asks for that.

2. Load only the active protocol surface.
- Read the relevant files from `references/` before writing new rules.
- Prefer the current truth source, role rules, task card, and session card over historical logs.
- Treat closed items as history, not live work.

3. Choose the execution role.
- `PM`: dispatch, acceptance, correction, and next-step control.
- `Supervisor`: inspect PM state, detect drift, and issue minimal corrections.
- `Long-worker`: own exactly one large module or cross-day lane when explicitly authorized.
- `Short-worker`: default worker for bounded delivery, blocked repair, verification, and day-close.

4. Choose the planning shape.
- For a large system, create one long-worker owner for one module, then split child work into short-worker lanes.
- For bounded repair or validation, dispatch a short-worker directly.
- Keep one lane per worker when possible.

5. Run with explicit closure.
- Every worker returns a summary package, not a full diff by default.
- Separate `loop state` from `dispatch state`.
- Close short-workers the same day. Re-open next day as a new short-worker if needed.

## Mandatory operating rules

- Use structured tags only in the form defined in [references/protocol-core.md](references/protocol-core.md).
- Use identity headers in the form `[role]#module@version`.
- Treat `@version` as a human-readable module or plan version, not as a tag.
- Default all new workers to short-worker unless the user explicitly authorizes a long-worker.
- A long-worker owns one large module only. Do not let a single long-worker spread across unrelated modules.
- A short-worker is day-close only. Do not let a short-worker continue across days without archive and re-open.
- Keep delivery in summary-package format unless review, merge, conflict, or explicit diff request requires a minimal patch.
- Do not let PM drift into implementation details when the task is orchestration only.

## Goal-mode usage

- Use goal mode for long-running PM or worker execution when the thread must continue until the target is actually closed.
- Define one concrete objective.
- Define the stop condition in terms of dispatch completed, callback collected, acceptance written, or archive updated.
- Prevent early stop by stating that the thread must not end at partial dispatch, partial callback, or partial summary.
- When blocked repair is needed, treat it as a short-worker lane unless the user explicitly says otherwise.

Read [references/goal-mode-prompts.md](references/goal-mode-prompts.md) when you need ready-to-send prompts for PM, long-worker, short-worker, or supervisor threads.

## Protocol surfaces

Read [references/protocol-core.md](references/protocol-core.md) for:
- tag contract
- identity header contract
- long-worker and short-worker rules
- callback pack
- summary package shape
- day-close and archive rules

Read [references/version-planning.md](references/version-planning.md) for:
- daily version plan structure
- how PM should open a new version lane
- how to map large systems to one long-worker owner
- how to split child lanes into short-workers

Read [references/repo-protocol-bootstrap.md](references/repo-protocol-bootstrap.md) when the user wants to materialize the protocol into repository files such as `docs/handoff/**`.

Read [references/self-iteration.md](references/self-iteration.md) when the user wants PM review, rule tightening, drift correction, or end-of-day protocol improvement.

## Optional modules

The core skill must work without optional modules.

Read [references/optional-modules.md](references/optional-modules.md) only when the user wants extra capabilities such as:
- git workflow hooks
- archive helpers
- stricter callback templates
- repository-specific handoff structure

If an optional module is not selected, keep it out of the operating context.

## Output shape

Default to compact PM output:
- changed control files
- dispatched or closed lanes
- callback status
- verification result
- risk or rollback note
- next action

Do not emit full `git diff` unless explicitly requested or required for review.
