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
| **前后端对接** | ✅ **ahead** | **W1 (原计划W2-3)** |
| Generation Bias (标记+EMA) | ❌ | W3 |
| 对话流串联 + 端到端 | ❌ | W2 |
| Session Resumption | ❌ | W2 |
| 架构图更新 | ❌ | W3 |
| 阿里云部署 | ❌ | W5 |
| Demo 视频 + README | ❌ | W5-6 |
| 提交 | ❌ | W6-7 |

---

## 已完成

- [x] **方案文档** — 双回路设计 + Generation Bias (§九)
- [x] **技术风险分析** — OOC 公式 推导 + 多因子权重
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

---

## 待做

### 🟡 P1
- [ ] **Generation Bias** — 标记组件 + EMA 回调 + 偏向生成
- [ ] **IngestionService** — 小说文本解析 + 角色提取
- [ ] **Session Resumption** — 重启时加载 SQLite 角色

### 🟢 P2
- [ ] **对话流串联** — 前端发消息 → /ask 显示回复 + OOC 标签
- [ ] **端到端衔接** — 摄入+对话+睡眠巩固完整流程
- [ ] **架构图更新** — 补上 Generation Bias 链路

### ⚪ P3
- [ ] README 精修
- [ ] Devpost 提交
- [ ] 阿里云部署

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

- **Generation Bias 标记组件**：用户选完后弹多选"这就是他会做的事 / 情节需要 / 想看看可能性 / 说不上来"，角色驱动才 EMA 更新 preferred_profile
- **Caelan Ashmark 为 Demo 角色**：Caelvorn Book 1 男主角
- **全开源，独立于渡心阁**
