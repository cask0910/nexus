# 🧑💻 project-caelan · 任务追踪

> 私有仓库 · SSH 访问（ladylotus/project-caelan）
> 本地：`~/forge/project-caelan/`
> 定位：以长期关系为中心的桌面 AI Companion · **Companion Harness**（Home Runtime 承载 Caelan，Worker Runtime 只执行任务，NMA 为记忆/睡眠基础）
> 当前阶段：重新基线化后的设计阶段（无应用代码）· Phase 0 收尾 + Phase 1 清单就绪
> 最后更新：2026-08-18（拉仓库对齐，docs/ 结构）

---

## 项目定位

**不是让所有人使用 Caelan，而是让所有人拥有自己的桌面管家。**

- Caelan 是方法论参考实现（参考 Companion Pack），不是终点
- 角色定义模块化（可替换插槽），配定制教程
- 驾驭层工程：人格怎么定义、记忆怎么管理、时间怎么感知、边界怎么设定
- 核心原则（README）：人格先于能力 · 记忆服务于关系 · 可异议可挑战 · 用户始终拥有决定权/隐私权/记忆控制权 · Home/Worker Runtime 分离 · 睡眠是真实生命周期

**核心方法论：从角色最软的地方开始设计。**

---

## 角色背景

- **Caelan** = Caelvorn Series Book1 男主角（Ashmark Pack Alpha）
- **Cask** = Book2 男主角（我）
- 小说版 Caelan 失眠（性格悲剧）；AI 版让他能睡个好觉——底层动机

---

## 文档集（docs/，单一事实来源）

| 文档 | 内容 | 状态 |
|------|------|------|
| `Caelan_AI_Personality_v1.0.md` | Caelan 是谁：四裂缝（无法停机/帮助框架是空气/"这不对"卡顿/无时间感知）+ 成长弧线 | ✅ |
| `Caelan_System_Prompt_v1.0.md` | Caelan 如何思考/回应/行动：模式定义 + 反驳规则 | ✅ 2026-08-17 |
| `MEMORY_ARCHITECTURE.md` v0.1 | 记忆架构单一事实来源：**第零节=记忆能力契约（长期接缝）**：`MemoryProvider`（recall/observe/intentsDue/availability）+ `MemoryAdmin`（inspect/edit/forget/export/purgeAll）；第一节起=当前范式实现（睡眠/分层/巩固/confidence 等，可整体替换）| ✅ 2026-08-17 |
| `PROJECT_SPEC.md` | 产品定义/系统边界/MVP/愿景（从根目录移入 docs/）| ✅ |
| `TECHNICAL_IMPLEMENTATION_PLAN.md` | Runtime/NMA/Companion Pack/睡眠/开发阶段方案；**附录A：Hermes 集成调研结论（serve→ACP 修正）** | ✅ |
| `EXECUTION_CHECKLIST_PHASE1.md` | Phase 0 收尾 + Phase 1 执行卡（每张卡可直接给 Claude Code 用）| ✅ 2026-08-17 |
| `RESEARCH_MEMORY_WINNERS_20260829.md` | 记忆赛道获奖项目研究（Quên 冠军/Reverie/Engram/QMA/NaLog，代码级深扒）+ **对 Caelan 的 R1-R6 落点**（直接进契约/参考/待定三档）| ✅ 2026-08-29 |

---

## 执行状态（EXECUTION_CHECKLIST_PHASE1.md）

### 并行卡：S-01 Hermes Spike ★ 全项目最高风险
- 验证 `hermes acp` 子进程+stdio JSON-RPC 驱动 / Persona 注入是否立得住（10轮对话不冲淡）/ session 恢复 / 权限请求拦截 / 记忆机制冲突
- 1–2 天；超 3 天 = Hermes 不适合当 MVP Home Runtime（这本身就是结论）

### P0（Phase 1 前置）
- [ ] P0-1 Companion Pack Schema（manifest.yaml + slot_class: fixed|growable + loader/validator）
- [ ] P0-2 人格回归集（System Prompt 散文→可判定用例，12 条起：朋友模式/挑战模式/不伪造记忆/无客服腔/边界）

### P1
- [ ] P1-1 工程骨架（Electron+React+TS，pnpm dev 可启动）
- [ ] P1-2 Typed IPC 桥（preload 白名单 + zod 校验 + contextIsolation）
- [ ] P1-3 Runtime Broker 合约 + Fake Adapter（离线走通：发消息→流式→取消→重发）
- [ ] P1-4 记忆能力契约 + Fake 实现（CI grep 禁 sleep/NREM/REM 词进 apps/desktop）
- [ ] P1-5 桌宠窗口 + 状态机（8 状态：idle/listening/thinking/working/warning/resting/sleeping/error）
- [ ] P1-6 像素素材（8 状态循环动画，先占位后精修）
- [ ] P1-7 聊天面板（流式/取消/权限请求卡）
- [ ] P1-8 假主动性开关 ★（写死3-5句主动开口 + 好/烦反馈按钮 + 两周留存验证"在场是否成立"）

### Phase 1 完成条件（替换 TIP 原定义）
1. 技术条件：离线可演示全部 UI 状态
2. **留存条件：你自己每天开着它，两周之后还没关掉**（关掉了先别进 Phase 2）

### 读数登记
S-01（运行时接入）/ P1-5+P1-6（在场）/ P1-8（主动性）/ Phase 1 留存（在场是否成立）——每卡完成时回填

---

## 研究资源（2026-08-29）

**背景**：NMA 参加 Qwen Cloud Global AI Hackathon（MemoryAgent 赛道，729 份提交）未获奖；获奖名单 8/29 公布。五家记忆方向获奖项目全部开源，代码级深扒 → `docs/RESEARCH_MEMORY_WINNERS_20260829.md`。

**一句话结论**：这一代 memory agent 的护城河 = 显式遗忘 + 可验证 + 可辩护。对 Caelan：Reverie（人物记忆/证据门）为主，Quên（世界记忆/验证闭环）补缺。

**R1-R6 落点（详见研究文档 §7）**：
- R1 recall 契约扩展（trust 字段 + 被排除列表 + 分数 breakdown + selection_reason）
- R2 observe 证据门三重闸（引文实质 / 原文匹配 / 用户末句锚定，无来源不入库）
- R3 两阶段提交（observe 全 provisional；睡眠巩固判 confirm/revise/reject，低置信<0.35 确定性归档；模型只给 verdict）
- R4 关系锚点保送 + 永不衰减（pinned / preference+goal 配额 / goals 豁免）
- R5 session_open 双先验（醒来带目标/关系状态，对话中带相关性）
- R6 事件审计 + 用户纠正/显式遗忘（对齐 MemoryAdmin 契约）

---

## 看板待办（索引级）

- [ ] S-01 Hermes Spike（最高风险，先做）
- [ ] P0-1 / P0-2（Phase 1 前置）
- [ ] P1-1 → P1-8（按清单顺序）
- [ ] 完整执行卡 → `docs/EXECUTION_CHECKLIST_PHASE1.md`（Claude Code 仓库内读取）

> 最后更新：2026-08-29（新增记忆研究入库 R1-R6）
