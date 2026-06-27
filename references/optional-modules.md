# Optional Modules

Keep these modules out of the active context unless the user selects them.

## 1. Git module

Use when the user wants:
- branch discipline
- staged delivery
- commit / PR packaging
- minimal patch review

Recommended rules:
- do not default to full git diff in delivery
- prefer summary package + changed files
- only expand to patch when review or conflict requires it

## 2. Archive module

Use when the user wants:
- daily short-worker archive flow
- closed-lane cleanup
- historical thread rollup

## 3. Repo protocol module

Use when the user wants:
- a repo-local `docs/orchestration/**` system
- standardized role cards, task cards, session cards
- startup prompt templates inside the repository

## 4. Validation module

Use when the user wants:
- stricter callback schema
- acceptance checklist
- runtime verification checklist

## Selection rule

At start, state which optional modules are active.

Example:
- active optional modules: `git`, `archive`
- inactive optional modules: `repo-protocol`, `validation`
