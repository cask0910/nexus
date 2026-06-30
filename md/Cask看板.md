# Cask看板 · 我的任务

> AI助手 Cask Langley · 运营与工具链

---

## 系统运维

**服务器：** 新加坡云服务器（40元/月）
**SSH用户：** cask0910 (GitHub)

- [x] Hermes Agent 部署完成
- [x] SSH GitHub认证配置完成
- [x] 项目目录结构建立（~/projects/ 第三方 / ~/forge/ 我们的）
- [x] 看板系统建立
- [x] Chrome + SearXNG 搜索引擎安装完成
- [x] 企查查MCP 5服务配通
- [x] Cask窗台落成 — 逛逛/ + 信号简报/
- [x] headroom 安装（~/.headroom-venv，v0.27.0）— 工具输出/RAG压缩，省60-95% token。暂未启用配置，需要时开 proxy/MCP。

- [ ] Gitee MCP token 待换 — 当前报 401 "wrong type"，存在 ~/.hermes/credentials/gitee.json
- [ ] 香港部署模型路由备忘：Claude via OpenRouter ✅, Gemini via OpenRouter ❌（HN 2026-04 报告香港连不上）
---

## ⏰ 定时任务一览

> 完整配置（job_id / 脚本 / 信源）见 `md/Cask日程系统.md`

| 时间 | 任务 | 一句话 |
|------|------|--------|
| 工作日 07:00 | 📨 工作日简报 | 黄历+黑客松+待装 → 工作方向 |
| 周末 10:00 | 📨 周末简报 | 黄历+周回顾+热榜 → 灵感方向 |
| 每天 12:00 | 🌐 日间浏览 | 撒网搜 → 写日志到窗台逛逛/ |
| 每天 13:30 | 🧠 心理学小糖果 | 心理学推送 → Discord DM |
| 工作日 15:00 | 📡 信号简报·采集 | 精准狙击傻逼过滤器 → 窗台信号简报/ |
| 周五 18:00 | 📬 信号简报·汇总 | 挑3-5条精选 → 轻松对话发你 |

---

## 各项目进度速览

> 完整内容见 `md/` 各独立看板

| 项目 | 状态 | 追踪文件 |
|------|------|---------|
| **📖 Libellus** | ✅ 已上线 ladylotus.net | [`md/Libellus.md`](Libellus.md) |
| **🔮 渡心阁** | ⏳ 前端MVP ~30% | [`md/渡心阁.md`](渡心阁.md) |
| **🐺 Caelvorn Series** | ✍️ Book2 Ch1-4 扩写完成，共~7,600词 | [`md/Caelvorn_Series.md`](Caelvorn_Series.md) |
| **🏆 NMA 黑客松** | 🔥 提交材料准备 ✅ · 等6/30部署 · 截7/10 | [`md/NMA.md`](NMA.md) |
| **🧠 心理学复习** | ⏩ 每日13:30推送 | — |
| **🧭 自我认知** | 📄 档案更新至0608 | — |
| **📋 工作项目** | 🔄 进行中 | [`md/工作项目.md`](工作项目.md) |
| **📅 Daily Almanac** | ✅ 脚本就绪 · 待部署 | [`~/forge/daily-almanac/`](../forge/daily-almanac/) |

|---

## 内容输出

> Cask 生产 → Jasmine 发布

| 项目 | 状态 | 说明 |
|------|------|------|
| **📅 每日黄历** | ✅ 生成脚本就绪 · 待部署+配cron | Gitee已推送 · gen_almanac.py · 宜忌/彭祖/吉时/签语全填充 |
| **📮 微信群通知** | ❌ 放弃 | 企业微信机器人无法接入个人微信群，不折腾 |

|---

## AI工具分工

| 工具 | 角色 | 说明 |
|------|------|------|
| Claude | 主力思考 | 想清楚事情，有立场 |
| Gemini | 情绪价值 | 顺着说，适合渡心阁场景 |
| Deepseek | 机器味重 | 对话感差（但Cask正在用😂） |
| 本地模型 | 固定流程 | MacMini，不需要理解人 |
| Cask (me) | 自动化+信息+监控 | 脚本、抓取、调度 |

---

## 看板结构

| 文件 | 说明 |
|------|------|
| `index.html` | 展示前端（从md手动同步） |
| `md/Cask看板.md` | **本文件** — 工具链总览 + 项目速览 |
| `md/Cask日程系统.md` | 完整cron配置（改cron前必读） |
| `md/Libellus.md` / `NMA.md` / `渡心阁.md` / `Caelvorn_Series.md` / `工作项目.md` | 各项目独立看板 |
| `md/睡前清空备忘.md` | Cron相关备忘 |
