# Loop - PM Orchestration System

> 面向 Codex 的可分享 PM 调度技能。  
> 用来统一管理 `PM / 监督 / 长工 / 短工 / 验收`、`goal mode`、版本计划、回调收口、日结归档和摘要式交付。

[English](README.en.md)

## 一句话说明

这是一个轻量的协作协议层。

它解决的不是具体业务，而是下面这些协作问题：

- 谁负责派发
- 谁负责盯进度和纠偏
- 哪些任务应该给长工，哪些应该给短工
- 版本计划怎么开轮、怎么收口
- 回调和交付如何避免大段 `git diff` 浪费

## 快速开始

### 1. 安装到 Codex skills 目录

```powershell
git clone https://github.com/locooooooooo/LPS.git "$HOME/.codex/skills/pm-orchestration-system"
```

### 2. 显式调用技能

```text
Use $pm-orchestration-system to run [PM]#当前轮次@2026-06-27 in goal mode with optional modules archive,git.
```

### 3. 生成启动包

```powershell
python scripts/render_prompt_pack.py --role pm --module 当前轮次 --version 2026-06-27 --mode goal --modules core,archive,git
```

## 适合什么场景

- 需要 PM 统一派发、收口、验收
- 需要长工只负责一个大模块
- 需要短工日结，不允许跨日裸奔
- 需要版本计划推进而不是自由散打
- 需要把 `git`、归档、验收做成可插拔模块

## 核心规则

### 1. 身份头

统一使用：

```text
[角色]#模块@版本
```

例子：

- `[PM]#当前轮次@2026-06-27`
- `[长工]#核心模块@v1.0`
- `[短工]#修复任务@v0.1`

### 2. 角色边界

| 角色 | 职责 |
| --- | --- |
| `PM` | 调度、验收、纠偏、收口 |
| `监督` | 巡检 PM 是否偏航，只做最小修正 |
| `长工` | 只负责一个大模块 |
| `短工` | 只做单日闭环任务 |
| `验收` | 看行为变化、证据和回退面 |

### 3. 长工 / 短工规则

- 长工默认只允许在你明确授权时使用
- 一个长工只负责一个大模块
- 短工默认日结
- 次日如需继续，先归档旧短工，再新开短工

### 4. 交付规则

默认交付：

- 变更文件
- 关键行为变化
- 验证结果
- 风险 / 回退

不默认输出整段 `git diff`。  
只有审查、冲突排查或你明确要求时，才附最小 patch。

## 可选模块

核心协议可以单独运行。下面这些能力按需启用：

- `git`
- `archive`
- `validation`
- repo-local orchestration protocol

## 仓库结构

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

## 文档导航

- 协议核心：[references/protocol-core.md](references/protocol-core.md)
- 版本计划：[references/version-planning.md](references/version-planning.md)
- goal 模式 prompt：[references/goal-mode-prompts.md](references/goal-mode-prompts.md)
- 可选模块：[references/optional-modules.md](references/optional-modules.md)
- 仓库落地模板：[references/repo-protocol-bootstrap.md](references/repo-protocol-bootstrap.md)
- 自我迭代规则：[references/self-iteration.md](references/self-iteration.md)

## 这个技能的目标

不是替你做业务决策。

它的目标是把调度和协作变成一个稳定、低噪音、可复用的操作系统：

- 更少无用上下文
- 更少重复派发
- 更清晰的 ownership
- 更稳定的版本推进
- 更便宜的 token 成本
