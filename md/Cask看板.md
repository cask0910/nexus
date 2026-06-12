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
- [x] Chrome 浏览器安装完成
- [x] 搜索引擎搭建完成（自建SearXNG，零成本，见skill: cask-free-web-search）
- [x] 工具安装纪律 skill 创建完成（tool-install-discipline：每个方向只装一个最火的）
- [x] 企查查MCP 5服务配通（company/risk/ipr/operation/executive · 认证Token已配置 · 见skill: qichacha-mcp）

---

## ⏰ 定时任务中心

> 核心 · 自动推送 · 详情见 `md/Cask日程系统.md`

### 📨 工作日简报（07:00）
- **状态：** ✅ 运行中（job_id: 7925940abca2）
- **时间：** 工作日（周一至周五）**7:00**
- **内容：** 📅黄历 + 🏆黑客松进度 + ❓昨日待装 → 💪（私人工作方向：NMA/渡心阁/小说）

### 📨 周末简报（10:00）
- **状态：** ✅ 运行中（job_id: cd9a836c64bc）
- **时间：** 周末（周六/日）**10:00**
- **内容：** 📅黄历 + 📖周浏览回顾 + ❓本周待装 + 📊热榜 → 💪（灵感娱乐方向）

### 🌐 日间浏览（12:00）
- **状态：** ✅ 运行中（job_id: 61550e97afbc）
- **时间：** 每天 **12:00**
- **内容：** 搜6方向+aibase+GitHub → 写日志到 `~/Cask窗台/逛逛/` → ⭐≥1000的工具类自动装 → ❓不确定的记下来
- **投递：** 静默（local），不主动推送

### 📡 信号简报·每日采集（15:00）
- **状态：** ✅ 新增（job_id: 8594d722458f）
- **时间：** 工作日 **15:00**
- **内容：** 精准狙击傻逼过滤器 — 静默抓5源 RSS（Simon Willison / Karpathy / Lilian Weng / OpenAI Blog / Hermes Agent）→ 追加到 `~/Cask窗台/信号简报/raw/` 周文件
- **投递：** 静默（local），仅采集不推送

### 📬 信号简报·每周汇总（周五 18:00）
- **状态：** ✅ 新增（job_id: bb2c635e516d）
- **时间：** **周五 18:00**
- **内容：** 读本周采集数据 → 挑 3-5 条精选 → 轻松幽默对话式发 Discord
- **投递：** Discord DM 给 Jasmine

---

## 各项目进度速览

> 完整内容见 `md/` 各独立看板

| 项目 | 状态 | 追踪文件 |
|------|------|---------|
| **📖 Libellus** | ✅ 已上线 ladylotus.net | [`md/Libellus.md`](Libellus.md) |
| **🔮 渡心阁** | ⏳ 前端MVP ~30% | [`md/渡心阁.md`](渡心阁.md) |
| **🐺 Caelvorn Series** | ✍️ Book2 32章节拍完成 ~60% | [`md/Caelvorn_Series.md`](Caelvorn_Series.md) |
|| **🏆 NMA 黑客松** | 🔥 W3审计完成 · 截7/10 | [`md/NMA.md`](NMA.md) |
| **🧠 心理学复习** | ⏩ 每日13:30推送 · 模块一进行中 | 总览见 `index.html` → 📚 |
| **🧭 自我认知** | 📄 档案更新至0604 | 详情见 `index.html` → 🧭 |
| **📋 工作项目** | 🔄 进行中 | [`md/工作项目.md`](工作项目.md) |

---



## AI工具分工

| 工具 | 角色 | 说明 |
|------|------|------|
| Claude | 主力思考 | 想清楚事情，有立场 |
| Gemini | 情绪价值 | 顺着说，适合渡心阁场景 |
| Deepseek | 机器味重 | 对话感差（但Cask正在用😂） |
| 本地模型 | 固定流程 | MacMini，不需要理解人 |
| Cask (me) | 自动化+信息+监控 | 脚本、抓取、调度 |

---

## 看板维护

**结构：**
- `index.html` — 展示前端（从md手动同步）
- `md/` — 源文件，改md → 手动同步到HTML
- `md/Cask看板.md` — 本文件（工具链总览 + 项目速览 + 看板维护）
- `md/Cask日程系统.md` — 完整cron配置（改cron前必读）
- `md/Libellus.md` — Libellus博客项目
- `md/NMA.md` — 当前黑客松跟踪
- `md/渡心阁.md` — 渡心阁开发
- `md/Caelvorn_Series.md` — 小说系列
- `md/工作项目.md` — 工作相关
- `md/睡前清空备忘.md` — Cron相关备忘

> 独立看板文件（Libellus / NMA / 渡心阁 / Caelvorn / 工作项目）是各自项目的唯一源头，不再在本文中重复展开。

**更新历史：**
- 2026-06-05：Field Notes格式定型（🎩 Cask's Take heading）+ 筛选bug修复 + 路径硬编码修复 | 犯了一个错：改错了skill（动了cask-daily-brief而非libellus-field-notes-format）
- 2026-06-04：大扫除——移除Libellus/心理学/自我认知/Hackathon/小说的重复内联内容，改为项目速览表 | 删除md/Cask能力.md（完全被index.html能力清单覆盖）
