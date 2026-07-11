# CodexCodingAgentTeam

[English](README.md)

一个可复制到任意代码仓库中的 Codex 多 Agent 协作资产包。它提供通用交付机制，不携带任何特定仓库的产品、技术栈或目录假设。

核心模型很简单：根 Agent 负责协调；实现 Agent 完成一个边界明确的切片；验收 Agent 以只读方式独立审查完整差异；每个切片都以新的验证和独立提交收尾。

## 资产清单

| 资产 | 用途 |
| --- | --- |
| `.codex/agents/agentteam-evidence-explorer.toml` | 以只读方式梳理需求、代码、数据、行为、测试和验证证据。 |
| `.codex/agents/agentteam-slice-implementer.toml` | 在明确的路径边界内实现一个完整切片。 |
| `.codex/agents/agentteam-contract-reviewer.toml` | 对完整差异进行独立验收。 |
| `.agents/skills/agentteam-slice-delivery/` | 面向中大型需求的切片编排、验收门禁和计划校验器。 |
| `.agents/skills/agentteam-capability-delivery/` | 单个能力族从证据到交付的工作流。 |
| `.agents/skills/agentteam-requirements-design/` | 基于证据的需求澄清、可编码技术设计和就绪门禁。 |
| `.agents/skills/agentteam-release-readiness/` | 基于证据的发布就绪度评估，以及 UAT/生产闭环记录。 |

## 快速开始

### 给人类

1. 将 `.codex/agents`、`.agents/skills`、`templates` 和 [AGENTS.md](AGENTS.md) 中的协作规则复制或合并到目标仓库。不要覆盖目标仓库已有的专属说明。
2. 在 Codex 中打开目标仓库，并要求它遵循[引导提示词](templates/codex-bootstrap-prompt.md)。它会先梳理仓库、根据证据填写目标配置，并把未知项保留为 `TODO: <evidence needed>`。
3. 对中大型改动，在开始实现前审阅并确认分别产出的需求和技术设计；随后使用切片计划跟踪实现、独立验收、验证，以及每个已验收切片的一次提交。
4. 若需要发布决策，使用发布就绪度技能，并分别审阅仓库、UAT 和生产证据。部署仍必须获得明确授权。

### 给 Codex Agent

1. 先读取目标仓库的 `AGENTS.md`，再读取本资产包的 [AGENTS.md](AGENTS.md)；始终以目标仓库规则为准。
2. 编辑前先建立仓库事实：只能依据当前证据填写目标配置；未知项保留为 `TODO: <evidence needed>`；不要推断环境权限。
3. 当需求或设计不完整时，使用 `$agentteam-requirements-design`。只要存在未解决的关键决策、契约或证据缺口，就不能开始实现或切片规划。
4. 仅对已批准且可直接编码的设计使用 `$agentteam-slice-delivery`：实现一个边界明确的切片，取得独立的只读验收，重新执行关键验证，然后由根 Agent 暂存并提交。
5. 对一个边界清晰的能力族使用 `$agentteam-capability-delivery`；使用 `$agentteam-release-readiness` 形成 go/no-go 决策记录。没有明确授权，绝不部署、发布或修改外部系统。

## 详细工作流

1. 复制或合并 `.codex/agents` 和 `.agents/skills` 到目标仓库。
2. 将 [AGENTS.md](AGENTS.md) 中的协作规则合并到目标仓库，并用真实的仓库路径、命令、边界、环境权限以及发布/回滚入口填写其 `Target Project Configuration` 占位符。目标仓库自己的架构、权限、发布和验证规则始终优先。
3. 当需求或设计不完整时，先使用 `$agentteam-requirements-design`；它会生成 `$agentteam-slice-delivery` 所需的已批准基线。
4. 对已批准的中大型需求使用 `$agentteam-slice-delivery`；对一个边界清晰的能力族实现使用 `$agentteam-capability-delivery`。
5. 在委派实现与独立验收前，创建并校验切片计划。只有获得 `ACCEPTED` 结论的切片，根 Agent 才能暂存和提交。
6. 对最终就绪度决策使用 `$agentteam-release-readiness`。它会区分仓库就绪、UAT 就绪和生产就绪；实际发布操作仍需单独授权。

## 使用 Codex 引导

让 Codex 读取 [templates/codex-bootstrap-prompt.md](templates/codex-bootstrap-prompt.md)，并在目标仓库中执行其中的提示词。该提示词会引导 Codex 完成基于证据的需求澄清、技术设计、就绪门禁，并且只有在此之后才进入切片规划。

资产包内的占位符格式为 `{{UPPER_SNAKE_CASE}}`。Codex 只能用仓库证据替换它们；否则必须保留 `TODO: <evidence needed>`，并报告阻塞问题或闭环事项。

```powershell
pwsh .agents/skills/agentteam-requirements-design/scripts/validate-design-readiness.ps1 -RequirementsPath docs/requirements/my-capability.md -DesignPath docs/design/my-capability.md
pwsh .agents/skills/agentteam-slice-delivery/scripts/validate-slice-plan.ps1 -Path docs/plans/my-slice-plan.md
```

这是工作流资产包，不是项目模板或发布工具。它不能替代目标仓库的 `AGENTS.md`，也不会授予部署、发布、修改数据库或写入外部系统的权限。
