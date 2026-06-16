# Narrative Memory Agent · 黑客松看板

> **当前比赛：** Qwen Cloud Global Hackathon · Track 1: MemoryAgent
> Deadline: 2026/7/10 · 模型: qwen3.6-plus + text-embedding-v3
> 赛后本看板清空，转为黑客松筛选区。

---

## 整体进度

| 里程碑 | 状态 | 完成时间 |
|--------|------|---------|
| 方案定稿 + 架构图 | ✅ | W1 |
| Qwen API 验证 | ✅ | W1 |
| Circuit A + B 真实实现 | ✅ ahead | W1 (原计划W3) |
| 前端骨架 | ✅ | W1 |
| SleepCycle 三阶段巩固 | ✅ ahead | W1 (原计划W4) |
| 前后端对接 | ✅ ahead | W1 (原计划W2-3) |
| IngestionService | ✅ ahead | W2 (超前) |
| WorkingMemory 接入 /ask | ✅ | W2 (6/8 完成) |
| Validation 真实向量距离 | ✅ | W2 (6/8 完成) |
| Generation Bias 全链路 | ✅ | W3 (6/9 完成) |
| frontend 构建 + 单元测试 | ✅ feedback | W3 |
| OOC多因子 设计vs代码 trace | ✅ | W3 (6/12 审计) |
| SleepCycle REM阶段 方案对比 | ✅ | W3 (6/12 审计) |
| SleepCycle Phase 2 混合式升级 | ✅ | W3 (6/12 实现: LLM模式提取+向量剪枝+情感标签) |
| 三代记忆架构边界审计 | ✅ | W3 (6/12 审计 → 发现BUG并修复) |
| 端到端场景验证 | ✅ | W3 (6/16) |
| 测试覆盖 + 类型对齐 | ✅ | W3 (6/16) |
| 全面国际化 i18n | ✅ | W3 (6/16) |
| Demo切换：P&P角色 | ✅ | W3 (6/16) |
| 大模型对接验证 | ✅ | W3 (6/16) |
|| Session Resumption | 🆕 P2 | W4 |
| 架构图更新 | ❌ | W4 |
| 阿里云部署 | ❌ | W5 |
| Demo 视频 + README | ❌ | W5-6 |
| 提交 | ❌ | W6-7 |

---

## 已完成

### 基础架构（W1-W2）

- [x] **方案文档** — 双回路设计 + Generation Bias (§九)
- [x] **技术风险分析** — OOC 公式推导 + 多因子权重
- [x] **架构图** — SVG 中英文版本
- [x] **SQLite 数据库** — `database.py` + characters 表 + CRUD
- [x] **GenerationService (Circuit A)** — 调 Qwen 生成差异化选项
- [x] **ValidationService (Circuit B)** — T/B/D/C/P 评分 + OOC 公式
- [x] **`/ask` 端点** — Gen → Val 串联，已验证通过
- [x] **`/profile` 端点** — 数据库读取真实角色数据
- [x] **预置角色** — Caelan Ashmark（6 traits + 完整背景故事）
- [x] **前端骨架** — 5 个页面组件，暗色主题
- [x] **前端文案优化** — 发送按钮改为"如果是你，你会？"
- [x] **SleepCycle 三阶段巩固** — 冲突检测+加权→弧光演变+置信度调整→报告
- [x] **前后端对接** — API 适配层 + CORS + page.tsx 真实数据驱动 + SleepLogView 消费真实报告
- [x] **IngestionService** — LLM提取事件+角色 → 写入三层记忆 → 嵌入索引 (Caelvorn Ch.1验证通过)
- [x] **摄入前端** — 「📖 小说」标签页：粘贴文本 → 分析 → 结果展示，完成后自动刷新角色列表
- [x] **WorkingMemory 接入 `/ask`** — 全局 WorkingMemory + context_history 注入/记录，2026-06-08
- [x] **Validation 真实向量距离** — ChromaDB 语义距离替换 LLM 自估 D，2026-06-08

### Generation Bias 全链路（W3 — 6/9 完成）

- [x] **FeedbackBar 改问动机** — 从"像Caelan吗？"改为四选项复选框（角色驱动/剧情驱动/实验心态/说不上来）
- [x] **onSubmit 连后端API** — page.tsx 调 /feedback 端点，真实发送数据
- [x] **generation.py preferred_profile 注入修正** — 按偏向中心做 nudging
- [x] **SettingsView 加"选择后询问原因"开关** — 自动 / 每次 / 从不 三档
- [x] **OOC 标签区分"背离" vs "惊喜"** — ooc_details 加 type 字段，🚫偏离角色 vs 🟠出乎意料
- [x] **EMA 计算逻辑** — preferred_profile = EMA(old, K_profile, alpha)，alpha 依标记类型（角色驱动0.3 / 说不上来0.1 / 默认自动0.15）
- [x] **/feedback API 端点** — 接收选项+标记 → 判断是否更新 → EMA 计算 → 写 preferred_profile
- [x] **全链路测试** — /ask OOC类型 ✅ /feedback EMA更新 ✅ /feedback 边界 ✅ 前端构建 ✅

### W3 审计与打磨（6/12）

- [x] **TODO.md 重建** — 6阶段倒计时排期 + 里程碑表 + 技术债务
- [x] **feedback 端点测试** — 6个测试用例全部通过（缺失参数/未知角色/全流程EMA/剧情驱动不更新/实验不更新/默认缓慢EMA）
- [x] **OOC多因子模型 设计vs代码审计** — 验证公式一致，补写权重值/violation分类/D计算细节到方案文档 §9.7
- [x] **SleepCycle REM阶段分析** — 确认Phase2纯规则实现，三子阶段缺失，写入 `internal/SleepCycle-实现方案对比.md`
- [x] **三代记忆架构审计** — 发现 sleep.py 因果维度BUG (`cause` vs `causality`) 并修复；确认 SemanticMemory 为死代码；数据流闭环缺口记录至 `internal/记忆架构审计-Zwaan索引与数据流闭环.md`
- [x] **SleepCycle Phase 2 混合式升级** — 按方案对比文档推荐，LLM模式提取(1次调用) + 向量冗余剪枝(ChromaDB L2<0.05) + LLM情感标签(1次调用)，保留弧光推进+置信度调整规则；所有6个sleep测试通过

### W3 深度打磨（6/16）
- [x] **测试覆盖** — 29个新测试（Validation 18 + Generation 11），全部通过
- [x] **前后端类型对齐** — 修3个真实BUG（选项卡片字段/profile arc_stage/ooc_summary）
- [x] **前端错误处理** — 4场景Toast提示（连不上/无档案/生成失败/巩固失败）
- [x] **全面国际化 i18n** — 7个前端组件 + seed数据 + 后端mark key + 风险标签 中文→英文
- [x] **Demo切换P&P** — Elizabeth Bennet + Fitzwilliam Darcy 双角色就位
- [x] **大模型对接验证** — /ask→/feedback→/profile→/sleep 全链路跑通

---

## 待做

### 🆕 P2 新文件（延后 — W4）

- [ ] **Session Resumption** — serialize/deserialize 工作记忆，切角色和重开都能续

### 🟢 W3 场景验证（6/15-6/21）

- [ ] Caelvorn 第一章+第二章数据端到端跑通
- [ ] 3-5个 Leo 场景 OOC 参数直觉校验
- [ ] 修 Bug、调 prompt、边界情况处理

### ⚪ W4 打磨（6/22-6/28）

- [ ] Session Resumption（降为P2，如果时间够）
- [ ] 架构图更新（补 Generation Bias 链路）
- [ ] README 精修（英文）

### W5-6 提交准备（6/29-7/10）

- [ ] 阿里云部署
- [ ] Demo 视频录制（重点展示：多轮对话一致性 + OOC守卫 + 摄入流水线 + 睡眠巩固报告 + GenBias偏好学习）
- [ ] Devpost 提交
- [ ] 仓库改 public + 敏感信息清理

---

## 📝 配套博客计划

> 赛博小家 Libellus 在黑客松期间持续输出技术拆解文章

### 策略
- 黑客松期间只写 NMA 相关技术文章到 Libellus
- 结束后切换回其他灵感，下一场黑客松再切回来
- 全部打 `hackathon` tag，方便评委搜索定位

### 待写文章（灵感池）
- [x] 双回路架构设计：Circuit A + B + OOC 公式推导 ← 已发布为 《"That Doesn't Sound Like Them" — Five Gut Checks》
- [ ] Generation Bias：用户反馈如何重塑角色生成
- [ ] SleepCycle：三阶段记忆巩固算法
- [ ] Session Resumption：跨会话身份连续性实现
- [ ] 前端对接实录：FastAPI + Next.js CORS 踩坑
- [ ] 从 Caelvorn 到 MemoryAgent：小说 IP × AI 架构的碰撞

## 关键设计决策

- **Generation Bias 按方案文档 §九 完整实现**：四选项标记（角色驱动→EMA α=0.3 / 说不上来→α=0.1 / 默认自动→α=0.15）→ preferred_profile 存五维向量 → 下次生成以偏向中心做 nudging ✅ W3已实现并测试通过
- **惊奇度 UI 区分**："高风险"需分"背离角色"（T/B/C低）和"有惊喜"（P高且其他正常）两种 ✅
- **Settings 三档**：每次弹窗（默认）/ 仅高风险 / 不询问 ✅
- **Elizabeth Bennet + Fitzwilliam Darcy 为 Demo 角色**：Pride and Prejudice 全球知名度高，评审零学习成本；弧光变化丰富（偏见→觉醒、傲慢→谦卑），完美展示OOC检测+弧光感知
- **全开源，独立于渡心阁**

## 架构回顾与方案对比（2026/6/9 更新）

### 当前架构快照
| 组件 | 状态 | 备注 |
|------|------|------|
| FastAPI 骨架 + 6 端点 | ✅ | /ask /ingest /profile /sleep /feedback /session/new |
| 三层记忆（工作/情景/语义） | ✅ **但未串联** | WorkingMemory已接/ask，SemanticMemory被bypass |
| 向量检索（ChromaDB） | ✅ **但未查询** | Ingestion写入后无人消费 |
| Circuit A + B | ✅ | 生成→校验串联 |
| SleepCycle 三阶段 | ✅ | NREM→REM→Pruning |
| IngestionService | ✅ | LLM提取→事件→角色→嵌入全流水线 |
| **WorkingMemory→/ask** | ✅ | W2最高优先级 |
| **真实向量距离** | ✅ | W2次高优先级 |
| Generation Bias | ✅ W3闭环 | EMA五维 + 四标记 + Settings + OOC类型区分 |
| OOC 设计vs代码审计 | ✅ W3 | 确认公式一致，补方案文档 §9.7 |
| SleepCycle REM分析 | ✅ W3 | 三子阶段缺失，方案对比文档已产出 |
| 记忆架构审计 | ✅ W3 | 发现并修复因果维度BUG 🔧 |

### 方案对比（vs 主流记忆框架）
| 维度 | mem0 | MemGPT/Letta | MemPalace | NMA |
|------|------|-------------|--------|-----|
| 三层记忆 | ❌扁平 | ❌两层(存档+回溯) | ✅ 4层(L0-L3) | ✅ Baddeley+Zwaan+Asch |
| 双回路验证 | ❌ | ❌ | ❌ | ✅ Circuit A→B |
| OOC评分公式 | ❌ | ❌ | ❌ | ✅ T/B/D/C/P |
| 睡眠巩固 | ❌ | 虚拟上下文(paging) | ❌ | ✅ 三阶段(NREM→REM→Pruning) |
| 生成偏向学习 | ❌ | ❌ | ❌ | ✅ preferred_profile增量 |
| 角色一致性 | ❌ | prompt文字 | KG | ✅ 图式+OOC守卫 |
| 时间感知 | ❌ | ❌ | ✅ temporal KG | ✅ Zwaan时间索引 |
| token预算感知 | ❌ | ❌ | ✅ L0+L1低唤醒 | 可借鉴 |

**核心结论**：NMA 的差异化在「六件套+三层记忆」——双回路、OOC公式、SleepCycle、生成偏向、Settings可调、OOC类型分类。W3 全链路闭环完成。

### ⚙️ 后续待办
- [ ] 端到端跑通后做 OOC 参数调优验证（需 Jasmine 提供 3-5 个 Leo 场景，直觉校验 3 轮内收敛）
- [ ] 默认权重（α>β>γ>δ<ε）在 demo 阶段够用，调参是产品化精度
