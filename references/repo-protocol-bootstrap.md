# Repo Protocol Bootstrap

Use this reference when the user wants the PM system materialized inside a repository.

## Suggested file layout

```text
docs/
  handoff/
    index.md
    startup-prompt.md
    callback-summary-template.md
    roles/
      pm.md
      pm-ctrl.md
    tasks/
    sessions/
```

## Minimum file responsibilities

### index.md
- current loop state
- dispatch state
- active control cards
- active business cards
- recently closed cards
- read order
- dispatch gate

### roles/pm.md
- PM boundaries
- dispatch rules
- acceptance rules
- summary-package rule

### roles/pm-ctrl.md
- supervisor boundaries
- drift correction rule
- archive enforcement
- direct correction authority

### tasks/*.md
- objective
- scope
- acceptance
- current state
- blockers
- next action
- summary

### sessions/*.md
- thread id
- task tag
- role tag
- completed
- incomplete
- blockers
- next action
- evidence

## Bootstrap rule

- Keep the repository protocol small.
- Do not backfill full history unless the user explicitly wants migration.
- Write only the control cards and in-flight cards needed for the current loop.
