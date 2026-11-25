# Agent Delivery Workflow

[English](README.md)

一套以完整业务结果为目标、**不绑定特定 Coding Agent 或模型**的轻量交付工作流。主 Agent 持续负责探索、必要设计、实现、集成和验证；只有独立上下文、真正可并行的工作、隔离实现或独立审查能带来收益时，才委派子 Agent 或外部 Worker 会话。

本版本完整替换早期 AgentTeam 实验：旧 skill、固定角色链、切片计划格式、格式门禁和重复模板已删除，不保留兼容别名或适配层。历史版本保留在 Git 中。采用 [MIT 许可证](LICENSE)。

## 选择入口

| Skill | 适用任务 |
| --- | --- |
| [software-delivery](.agents/skills/software-delivery/SKILL.md) | 实现或修复一项能力，贯通端到端验收；普通开发与可选多 Worktree 并行协同的默认入口。 |
| [requirements-design](.agents/skills/requirements-design/SKILL.md) | 仅设计任务、运行基线核查以及重要产品行为、架构或契约决策；复用已有合格文档。 |
| [release-readiness](.agents/skills/release-readiness/SKILL.md) | 评估明确的发布候选，分别记录仓库验证、部署前条件、实际部署和业务验收。 |

明确的小修复可直接实现和验证，无需新增计划文档或子 Agent。大型工作可以按可独立验收的结果列出简短计划，无需为每个内部步骤安排专门实现角色或单独提交。多特性并行或高风险交付时，可按需启用协调模式：编码前设计交叉评审 -> 冻结设计基线 -> 隔离 Worktree 与共享文件契约 -> 分级审查/返工 -> 主分支集成与清理。

## 在目标仓库使用

1. 先读取目标仓库自己的说明。将所需 skill 文件夹及其资源完整复制到目标 `.agents/skills/`；每个 skill 都可独立使用，且适用于不同 Coding Agent 与模型。
2. 需要独立审查时，可将 [delivery-reviewer.toml](.codex/agents/delivery-reviewer.toml) 复制到 `.codex/agents/`，也可使用内置或外部审查会话；本包不写死模型、Agent 工具、线程数、沙箱策略或 Goal 开关。
3. 从 [AGENTS.md](AGENTS.md) 中合并适用规则，保留目标仓库的架构、权限和发布约束。按任务需要查明真实路径与命令，不要求先完成全仓库配置表。
4. 给出结果与验收条件，例如：`使用 $software-delivery 修复保存流程，并验证相关成功与失败路径。`

模板只保留在所属 skill 的 `assets/` 中，按需使用，不为填模板而创建文档。角色中的只读指令属于行为约束，不提供独立沙箱隔离；支持时优先启用宿主强制的沙箱隔离。

## 交付原则

- 尽早贯通最小可运行链路，再补齐必要行为与有意义的失败验证；重要变更定稿前按相关性只读核查全局中间件、CI/发布白名单、配置/Schema 启动策略与目标环境路由认证基线。
- 按独立任务与能力视角委派，不按组织结构建立常驻 Agent。每个工作树保持单一写入者、协调共享运行状态，创建隔离 Worktree 前先确认基线提交与未提交依赖，并在并行 Worktree 分叉前约定共享热点文件契约。
- 提交归属按隔离边界划分：共享工作树内的委派写入者不得 stage 或 commit；独立 `git worktree` 特性分支内的实现者可在该特性分支提交内聚改动，目标集成分支的合并集成、冲突解决与验证后清理始终归协调者所有。
- 重要风险或明确要求时进行独立审查（多视角可用时可错峰分工），覆盖新增文件并区分原有改动；协调者先核实分级再仅对 `BLOCKING`/`MAJOR` 触发原会话返工（有轮次上限；达上限仍未解决的 `BLOCKING` 或 `MAJOR` 保持未验收并升级交人决策），第 2 轮起优先针对性增量复审。
- 诚实路由：若用户指定了具体 Coding Agent、模型或推理档位而宿主无法精确指定，必须预先如实说明限制，不得静默替换成其他 Agent 或模型。
- 相关代码或差异、配置、环境和数据假设未变化时复用证据。各 Worktree 负责单测/契约验证，合并回主分支后由协调者执行最终关键回归及可用的交互/UI 冒烟检查，无需每个角色重复执行全部测试。
- 仅在恢复或交接需要时维护简短检查点；有实质变化才更新，原始证据存入产物，常规状态随工作批量提交。
- 外部证据缺口只阻塞依赖它的工作或结论。部署和线上修改需要明确授权；本地测试不能证明生产验收通过。

## 验证资产包

需要 Python 3.11+ 及开发依赖。在仓库根目录运行：

```sh
python -m pip install -r requirements-dev.txt
python scripts/check_pack.py
python -m unittest discover -s tests -v
```

独立复制后的 skill 可用 `python scripts/check_pack.py --skill /path/to/software-delivery` 检查。

检查器只验证打包、元数据和本地资源链接，不判断设计语义、不授予操作权限，也不证明业务验收。[行为评估案例](tests/scenarios.md)覆盖任务分流、证据复用、外部阻塞和协调行为。本次重构的[需求](docs/requirements.md)与[设计](docs/design.md)分别记录变更依据。

后续应在相同条件下比较每个已验收结果的成本与时间、首次端到端通过时间，以及返工和回归。本版本不声称已经测得 token 节省或交付提速。
