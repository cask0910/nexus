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
| Circuit A + B 真实实现 | ✅ | W1 |
| 前端骨架 | ✅ | W1 |
| SleepCycle 三阶段巩固 | ✅ | W1 |
| 前后端对接 | ✅ | W1 |
| IngestionService | ✅ | W2 |
| WorkingMemory 接入 /ask | ✅ | W2 |
| Validation 真实向量距离 | ✅ | W2 |
| Generation Bias 全链路 | ✅ | W3 |
| frontend 构建 + 单元测试 | ✅ | W3 |
| OOC多因子 设计vs代码 trace | ✅ | W3 |
| SleepCycle REM阶段 方案对比 | ✅ | W3 |
| SleepCycle Phase 2 混合式升级 | ✅ | W3 |
| 三代记忆架构边界审计 | ✅ | W3 |
| 端到端场景验证 | ✅ | W3 |
| 测试覆盖 + 类型对齐 | ✅ | W3 |
| Demo切换：P&P角色 | ✅ | W3 |
| Session Resumption | ✅ | W3 |
| 错误处理统一（ErrorToast） | ✅ | W4 (6/21) |
| 架构图更新（+GenBias回路） | ✅ | W4 (6/21) |
| 测试补齐（bias/bias_prompt/validation边界 80用例） | ✅ | W4 (6/21) |
| Docker 部署全套 | ✅ | W4 (6/21) |
| README + Tech Stack + Project Description 初稿 | ✅ | W4 (6/21) |
| **方向A：记忆衰减系统** | ✅ | W4 (6/21) |
| ├ decay.py — 时间衰减公式 + 三分类 | ✅ | |
| ├ episodic.py — events 表加字段 + archive 表 + migration | ✅ | |
| ├ generation.py — 情景记忆注入 | ✅ | |
| ├ ask.py — 检索 → 衰减筛选 → 记录访问 | ✅ | |
| ├ sleep.py — Phase 1.5 归档 + REM 引用 archive | ✅ | |
| ├ seed.py — 预置12条P&P事件 | ✅ | |
| ├ record_access 同步提升 importance（检索效应） | ✅ | |
| └ test_decay.py — 25个测试 | ✅ | |
| **文档更新（README/tech-stack/user-test-flow）** | ✅ | W4 (6/21) |
| **提交材料准备** | ✅ | W4 (6/21) |
| ├ 双角色填库（Lena 1048 / Caelan 1294 chars） | ✅ | |
| ├ demo_flow.md 补 type 字段 + demo-script-v2.md 录视频脚本 | ✅ | |
| ├ Project Description 509词英文描述 | ✅ | |
| ├ 架构图中英文双版确认正常 | ✅ | |
| ├ 9段口播音频（en-GB-SoniaNeural） | ✅ | |
| └ README/frontend-README/tech-stack/demo-questions 全部更新 | ✅ | |
|| **部署上线** | ✅ | W6 (7/1) |
| ├ 阿里云 ECS 新加坡 (2c1g, 47.84.196.253) | ✅ | |
| ├ Docker 前后端镜像构建+传输+部署 | ✅ | |
| ├ 后端:8000 / 前端:3000 双容器运行 | ✅ | |
| ├ Qwen API 从 3.6-plus 切 flash（节约额度） | ✅ | |
| ├ CORS + 跨域修复 | ✅ | |
| ├ crypto.randomUUID polyfill（前端 Node 兼容） | ✅ | |
| ├ Seed Seen 角色到服务器 DB（Caelan + Lena） | ✅ | |
| └ 前端 API URL 构建参数修正 | ✅ | |
|| **前端 Bug 修复** | ✅ | W6 (7/1) |
| ├ "查看其他选项" → "Show other options"（全英文） | ✅ | |
| ├ 追问后选项默认选中残留（chosen reset） | ✅ | |
| ├ "Welcome back" 截断 → 完整显示 Last question | ✅ | |
| ├ Import Text 导航从 settings 指向 ingestion 视图 | ✅ | |
| └ Settings 里 Import 按钮同样指向 ingestion | ✅ | |
|| **Surprise 选项修复** | ✅ | W6 (7/1) |
| ├ 撤销伪造 relabel 代码（诚实问题） | ✅ | |
| ├ 生成提示词加强 → AT LEAST one genuinely surprising | ✅ | |
| └ 温度 0.8 → 0.9（更多创意空间） | ✅ | |
| Demo 视频 + 提交材料 | ❌ | W5-6 |
| Devpost 提交 | ❌ | W6-7 |
|| **代码清理 + DB维护 (7/2)** | ✅ | W7 |
| ├ Session Resumption 补全 — conversation_history跨会话持久化 ✅ | ✅ | |
| ├ Feedback 图标修复（checkbox→🎯图标）✅ | ✅ | |
| ├ demo-script-v3.md 定稿（操作指南+视频脚本框架）✅ | ✅ | |
| ├ 生产DB双库清理（/data vs /app/data冗余）✅ | ✅ | |
| ├ 生产环境schema确认（last_sleep_report已存在）✅ | ✅ | |
| ├ 仓库冗余文件删除（9文件：空__init__/uv.lock/SVGs/翻译脚本）✅ | ✅ | |
| └ 生产容器内冗余文件同步清理 ✅ | ✅ | |

---

## 待做

### P0 — 提交必备
- [x] 阿里云部署证明 — ECS 已上线 ✅（截图存 internal/）
- [ ] Demo 视频 — 按 docs/user-test-flow.md ~3分钟
- [ ] Devpost 填表 — 上传视频 + 描述 + 架构图 + repo URL

### P2 — 低优先级
- [ ] 移动端适配
- [ ] 首次使用引导（选角→输入→提问 三步）
- [ ] 向量检索集成测试（ChromaDB + text-embedding-v3）
- [ ] SemanticMemory 持久化到 DB

---

## 关键设计决策

- **Generation Bias 按方案文档 §九 完整实现**：四选项标记（角色驱动→EMA α=0.3 / 说不上来→α=0.1 / 默认自动→α=0.15）→ preferred_profile 存五维向量 → 下次生成以偏向中心做 nudging
- **惊奇度 UI 区分**："高风险"需分"背离角色"（T/B/C低）和"有惊喜"（P高且其他正常）两种
- **Settings 三档**：每次弹窗（默认）/ 仅高风险 / 不询问
- **Elizabeth Bennet + Fitzwilliam Darcy 为 Demo 角色**：Pride and Prejudice 全球知名度高，评审零学习成本
- **时间衰减公式**：recall_score = importance × exp(-0.01 × chapters_elapsed)，只按 chapter 差，不按访问次数
- **检索效应**：每个事件被 /ask 命中一次，importance +0.01（上限 1.0），抵抗时间衰减
- **全开源，独立于渡心阁**

## 架构对比

| 维度 | mem0 | MemGPT/Letta | NMA |
|------|------|-------------|-----|
| 记忆架构 | ❌扁平 | ❌两层(存档+回溯) | ✅ 双层+角色库 |
| 双回路验证 | ❌ | ❌ | ✅ Circuit A→B |
| OOC评分公式 | ❌ | ❌ | ✅ T/B/D/C/P |
| 睡眠巩固 | ❌ | 虚拟上下文(paging) | ✅ 三阶段 |
| 生成偏向学习 | ❌ | ❌ | ✅ preferred_profile增量 |
| 角色一致性 | ❌ | prompt文字 | ✅ 图式+OOC守卫 |
| 记忆衰减 | ❌ | ❌ | ✅ 时间衰减公式 + 自动归档 |

**核心结论**：NMA 的差异化在「双回路+OOC公式+SleepCycle+GenBias+记忆衰减」。W4 方向A完成，全链路闭环。只剩提交材料。
