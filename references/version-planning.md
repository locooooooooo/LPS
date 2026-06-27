# Version Planning

## 1. Daily version plan model

Each version plan should answer:
- what is in scope today
- what is explicitly not in scope
- which lanes are P0 / P1 / placeholder only
- which lane needs a long-worker owner
- which lanes can be short-worker only
- what counts as accepted

## 2. Large-system planning rule

When the user names a large system:
- create one module owner long-worker
- bind the module with a visible version, for example `核心模块@v1.0`
- define the owner boundary clearly
- decompose sub-lanes only after the owner exists

Examples:
- `system-integration@v1.0`
- `closure-flow@v0.9`
- `core-module@v1.0`

## 3. PM split rule

PM can split child work in two ways:

### Option A: long-worker-driven split
- PM creates the large-module owner
- long-worker reads the truth source
- long-worker proposes or dispatches short-worker lanes
- PM supervises and closes

### Option B: PM direct split
- PM reads the plan
- PM dispatches multiple short-workers directly
- use this when the module is already decomposed and context is cheap

Choose the path with lower context cost and lower coordination risk.

## 4. Placeholder rule

If a lane does not yet have enough truth source:
- keep it as placeholder
- do not dispatch implementation
- record the missing source explicitly

## 5. Acceptance rule

A version lane should be marked `verified` only when:
- acceptance is written clearly
- callback is collected
- runtime or artifact verification is complete if required

Otherwise keep it active or summarized with explicit follow-up.
