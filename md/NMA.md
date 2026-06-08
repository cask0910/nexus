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
| **WorkingMemory 接入 /ask** | ❌ **P1** | **W2 核心缝合** |
| **Validation 真实向量距离** | ❌ **P1** | **W2 核心缝合** |
| **Generation Bias（轻量版）** | ❌ **P1/P2** | **W2-3** |
| 端到端场景验证 | ❌ | W3 |
| OOC 参数调优验证 | ❌ | W3 |
| Session Resumption（降为P2） | ❌ | W4 |
| 架构图更新 | ❌ | W4 |
| 阿里云部署 | ❌ | W5 |
| Demo 视频 + README | ❌ | W5-6 |
| 提交 | ❌ | W6-7 |

---

## 已完成

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

---

## 待做

### 调研结论（2026-06-08）

对比 MemGPT（OS虚拟内存模型）和 MemPalace（4层记忆堆栈）后结论：
- NMA 架构方向正确且更强（双回路+SleepCycle+OOC三样行业唯一）
- **最大结构性问题**：三层记忆模块（Working/Episodic/Semantic）全实现了，但只有 Episodic 真在管线里——WorkingMemory 没接入 `/ask`，SemanticMemory 被 bypass，ChromaDB 有嵌入但没被查询
- **当前核心任务不是加新功能，是把已有积木连起来**

### 第二期调研：上下文压缩策略（2026-06-08）

对比了 10 种主流压缩策略后核心判断：

**NMA 不需要外加压缩模块。** 现有组件只要串起来就天然构成了一条压缩管线——

| NMA组件 | 对应什么压缩策略 | 状态 |
|---------|----------------|------|
| WorkingMemory(10轮) | 滑动窗口（近10轮不压缩，之前自动丢弃） | 待接入 `/ask` |
| Ingestion→ChromaDB嵌入 | Embedding压缩（80-90%压缩率） | 已实现但无人消费 |
| preferred_profile增量 | 锚定增量摘要（只合并新信息到持久锚点） | 待实现生成偏向后自然形成 |
| SleepCycle Phase2 | 周期性压缩时机（弧光演变+trait置信度调整） | 已实现但结果不回写profile |

**节奏总结**：W2 三件事（WM接入、真向量距离、Generation Bias）就是在搭这条压缩管线的三段桥。不需要额外的压缩模块。

排除的方案：LLMLingua（token级压缩 → 叙事丢失敏感细节）、MIT RLM（两层LLM → 长尾成本不可控）、HyCo²（88.8%压缩 → 牺牲语义完整性）、Anthropic原生compaction（依赖API封锁）。

### 🟡 W2 核心缝合（6/8-6/14）

- [ ] **WorkingMemory 接入 `/ask`** — 全局 WorkingMemory 实例，每次请求前注入最近10轮上下文，请求后写入当前回合。改动点：`api/ask.py` + `services/generation.py`。1天。
- [ ] **Validation 真实向量距离** — 用 `VectorStore.search()` 查角色历史事件嵌入，算真实 cosine 距离替换 LLM 自估的 D。改动点：`services/validation.py`。2-3天。
- [ ] **Generation Bias 轻量版** — POST `/feedback` 端点接收用户选中的选项文本 → append 到 `character.preferred_profile` → 下次 `/ask` 注入 system prompt。不做 EMA，不做新表。2天。

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
- [ ] Demo 视频录制（重点展示：多轮对话一致性 + OOC守卫 + 摄入流水线 + 睡眠巩固报告）
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
- [ ] 双回路架构设计：Circuit A + B + OOC 公式推导
- [ ] Generation Bias：用户反馈如何重塑角色生成
- [ ] SleepCycle：三阶段记忆巩固算法
- [ ] Session Resumption：跨会话身份连续性实现
- [ ] 前端对接实录：FastAPI + Next.js CORS 踩坑
- [ ] 从 Caelvorn 到 MemoryAgent：小说 IP × AI 架构的碰撞

## 关键设计决策

- **Generation Bias 轻量版**：不搞 EMA + 新表 + 标记组件。用户选中后直接发文本 → 写入 `preferred_profile` → 下次注入 prompt
- **Caelan Ashmark 为 Demo 角色**：Caelvorn Book 1 男主角
- **全开源，独立于渡心阁**
- **调整后不改变 Hackathon 交付范围**——说好的记忆系统还是要跑通，只是侧重点从"造新模块"变成"连已有模块"
- **NMA 差异化五件套不变**（双回路+OOC公式+SleepCycle+EMA+Zwaan索引），只是 EMA 可视化程度降低，但 WorkingMemory 接入和真实向量距离的补全让系统实际更完整了

## 架构回顾与方案对比（2026/6/5 更新）

### 当前架构快照
| 组件 | 状态 | 备注 |
|------|------|------|
| FastAPI 骨架 + 5 端点 | ✅ | /ask /ingest /profile /sleep /session/new |
| 三层记忆（工作/情景/语义） | ✅ **但未串联** | WorkingMemory未接入API，SemanticMemory被bypass |
| 向量检索（ChromaDB） | ✅ **但未查询** | Ingestion写入后无人消费 |
| Circuit A + B | ✅ | 生成→校验串联 |
| SleepCycle 三阶段 | ✅ | NREM→REM→Pruning |
| IngestionService | ✅ | LLM提取→事件→角色→嵌入全流水线 |
| **WorkingMemory→/ask** | 🟡 待接线 | W2最高优先级 |
| **真实向量距离** | 🟡 待接线 | W2次高优先级 |
| **Generation Bias 轻量版** | 🟡 方案已定 | POST /feedback + preferred_profile 注入 |

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

**核心结论**：NMA 的差异化在「五件套+三层记忆」——没有开源项目同时做了双回路、OOC公式、SleepCycle、生成偏向、Zwaan索引、三层记忆。W2 串好后就是整体最完整的叙事记忆方案。

### ⚙️ 后续待办
- [ ] 端到端跑通后做 OOC 参数调优验证（需 Jasmine 提供 3-5 个 Leo 场景，直觉校验 3 轮内收敛）
- [ ] 默认权重（α>β>γ>δ<ε）在 demo 阶段够用，调参是产品化精度
