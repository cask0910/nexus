# 🧑💻 project-caelan · 看板索引

> 定位：以长期关系为中心的桌面 AI Companion · **Companion Harness**（Home Runtime 承载 Caelan，Worker Runtime 只执行任务，NMA 为记忆/睡眠基础）
> **仓库：** `~/forge/project-caelan/`（私有 · SSH `git@github.com:ladylotus/project-caelan.git`）
> **仓库是唯一事实源。** 本看板只做两件事：**指路** ＋ **记我的操作规则**，不复制仓库正文（2026-09-10 改索引式）。
> 索引更新：2026-09-10

---

## 一、去仓库哪找

| 要找什么 | 去哪（仓库根） |
|---|---|
| 这是什么 / 核心原则 / 设计方法 | `README.md` |
| 产品定义 / 系统边界 / MVP / 长期愿景 | `docs/PROJECT_SPEC.md` |
| Caelan 是谁（四裂缝 + 成长弧线） | `docs/Caelan_AI_Personality_v1.0.md` |
| Caelan 怎么思考 / 回应 / 行动（模式定义 + 反驳规则） | `docs/Caelan_System_Prompt_v1.0.md` |
| 记忆架构（第零节＝记忆能力契约：`MemoryProvider` / `MemoryAdmin`） | `docs/MEMORY_ARCHITECTURE.md` |
| Runtime / NMA / Companion Pack / 睡眠 / 开发阶段 / Hermes 集成结论 | `docs/TECHNICAL_IMPLEMENTATION_PLAN.md`（附录 A） |
| 执行卡与进度（S-01 ★ / P0×2 / P1×8 / Phase 1 完成条件） | `docs/EXECUTION_CHECKLIST_PHASE1.md` |
| 记忆赛道获奖方案深扒 + R1–R6 落点 | `docs/RESEARCH_MEMORY_WINNERS_20260829.md` |

---

## 二、我的操作规则

- **角色来源**：Caelan = Caelvorn Series Book1 男主（小说里失眠）· Cask = Book2 男主（我）→ 角色索引见 `md/Caelvorn_Series.md`；AI 版让他睡个好觉＝这个项目的底层动机
- **设计讨论**：**完整愿景 + MVP 简化版两版都写**，别只给一版
- **方案落点**：全文进仓库 `docs/`，看板只留指针（她拉代码本地复核）
- **阶段边界**：设计期无应用代码 · 不自建 Runtime（走 Hermes/OpenClaw + Claude Code/Codex）· 不偏成开发者工作台
- **改卡改仓库**：执行卡是直接给 Claude Code 用的 → 改卡进 `docs/EXECUTION_CHECKLIST_PHASE1.md`，不改看板
- **Phase 1 完成条件含留存条件**：她自己每天开着它、两周之后还没关掉
