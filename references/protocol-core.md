# Protocol Core

## 1. Truth-source priority

Read in this order:
1. current index or dispatch board
2. role card
3. active task card
4. active session card
5. only then recent history if required

Do not reload full history when the active cards already define the lane.

## 2. Tag contract

- Only recognize:
  - `⟦tag:v2|role|...⟧`
  - `⟦tag:v2|task|...⟧`
  - `⟦tag:v2|session|...⟧`
- Anything outside this exact wrapper is plain text, not a protocol tag.
- Preserve tag structure exactly when forwarding across sessions.

## 3. Identity header contract

Use:
- `[PM]#模块@版本`
- `[监督]#模块@版本`
- `[长工]#模块@版本`
- `[短工]#模块@版本`
- `[验收]#模块@版本`

Rules:
- `模块` names the lane or owned module.
- `版本` is human-readable, such as `v1.0`, `v0.2`, `2026-06-27`.
- New dispatches should include version unless the user explicitly keeps it implicit.

## 4. Role boundaries

### PM
- dispatch
- acceptance
- correction
- close-out
- no implementation analysis unless the user explicitly asks PM to do that

### Supervisor
- inspect PM loop state
- detect blocked or drift
- issue minimum correction
- do not expand scope

### Long-worker
- user-authorized only
- own one large module or cross-day lane
- can decompose child work into short-worker suggestions or direct short-worker dispatch
- should not own multiple unrelated large systems

### Short-worker
- default worker identity
- use for bounded execution, blocked repair, callback closure, verification, and index correction
- same-day close required

## 5. Long-worker / short-worker dispatch rule

For a large module:
1. assign one long-worker owner
2. define module version
3. split sub-lanes into short-workers when needed
4. collect callback
5. summarize and keep the module truth source current

For a small repair:
1. dispatch one short-worker directly
2. collect callback
3. close or archive

## 6. Day-close rule

- Short-worker must end the day in one of:
  - `summarized`
  - `blocked`
  - waiting for explicit acceptance note
- Next day, do not re-use the old short-worker as active state.
- Archive old short-worker record, then open a new short-worker if more work is needed.

## 7. Callback package

Use:

```md
[角色]#模块@版本
⟦tag:v2|session|<session-id>⟧
task tag: ⟦tag:v2|task|<task-id>⟧
role tag: ⟦tag:v2|role|<role-id>⟧
loop state: waiting_callback
dispatch state: waiting_callback

completed:
- ...

incomplete:
- ...

blockers:
- ...

next action:
- ...

evidence:
- file / artifact links only
```

## 8. Summary-package delivery

Default outward delivery:
- changed files
- key behavior change
- verification result
- risk / rollback

Only include minimal patch when:
- review requires it
- merge or conflict analysis requires it
- the user explicitly requests it

## 9. Dispatch gate

Only dispatch when one of these is true:
- there is a new truth source or new plan
- there is an active or waiting callback lane and the action is closure or correction
- the user explicitly names the lane, tag, file, or session and asks for direct action

Otherwise stay in standby.
