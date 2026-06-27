# PM Orchestration System

这是一个可分享的 Codex 技能，用来统一管理 PM 调度、长工/短工、goal 模式、版本计划、回调收口和日结。

## 它是什么

这是一个轻量的协作协议层。
它强调三件事：

- 只有一个 truth source
- 只有一个 active goal
- 默认只交付摘要包，不默认输出整段 `git diff`

## 适合什么场景

- 需要 PM 派发和收口
- 需要长工只负责一个大模块
- 需要短工日结、次日归档后重开
- 需要版本计划推进
- 需要把 `git`、归档、验收做成可选模块

## 快速开始

1. 把仓库放进 Codex skills 目录。

```powershell
git clone https://github.com/locooooooooo/LPS.git "$HOME/.codex/skills/pm-orchestration-system"
```

2. 直接调用技能。

```text
Use $pm-orchestration-system to run [PM]#今日版本@2026-06-27 in goal mode with optional modules archive,git.
```

3. 生成一个启动包。

```powershell
python scripts/render_prompt_pack.py --role pm --module 今日版本 --version 2026-06-27 --mode goal --modules core,archive,git
```

## 角色

- `PM`：调度、验收、纠偏、收口
- `监督`：巡检 PM 是否偏航，必要时只做最小修正
- `长工`：只负责一个大模块
- `短工`：只做单日闭环任务
- `验收`：看结果、看证据、看是否可回退

## 身份格式

统一用：

```text
[角色]#模块@版本
```

例子：

- `[PM]#今日版本@2026-06-27`
- `[长工]#闯荡@v1.0`
- `[短工]#blocked修复@v0.1`

## 可选模块

按需启用，不默认强制：

- `git`
- `archive`
- `validation`
- 仓库内 handoff 协议

## 仓库文件

- `SKILL.md`
- `agents/openai.yaml`
- `references/protocol-core.md`
- `references/version-planning.md`
- `references/goal-mode-prompts.md`
- `references/optional-modules.md`
- `references/repo-protocol-bootstrap.md`
- `references/self-iteration.md`
- `scripts/render_prompt_pack.py`
