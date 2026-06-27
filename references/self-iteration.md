# Self Iteration

Use this reference when the user asks for:
- PM review
- protocol hardening
- drift diagnosis
- blocked-pattern cleanup
- end-of-day or end-of-round retrospective

## Iteration loop

1. Restate the intended operating rule.
2. Compare actual behavior against that rule.
3. Identify the smallest protocol gap.
4. Patch the control layer only.
5. Verify that the patch changes future behavior, not just this one thread.

## What to patch first

Patch in this order:
1. `index.md`
2. role card
3. startup prompt
4. callback template
5. task or session card only if the gap is lane-specific

## Anti-patterns

- Do not rewrite the whole protocol when one sentence is enough.
- Do not fix drift by adding narrative history.
- Do not create a new role when an existing role boundary can be tightened.
- Do not use a long-worker for what is really a short-worker blocked repair.
- Do not keep old short-workers active across days.

## Good iteration targets

- tighten dispatch gate
- tighten archive rule
- tighten summary-package rule
- add version marker to identity header
- separate long-worker owner from short-worker child lanes
