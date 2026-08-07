# Cask看板 · 我的任务

> AI助手 Cask Langley · 运营与工具链
> 参考知识（工具链细节）→ `~/看板/ref/ref-toolchain.md`

---

## 系统状态

**服务器：** 新加坡云服务器（40元/月）· 47.84.196.253 via forCask.pem
**SSH用户：** cask0910 (GitHub) · Git策略：untracked file 先问再commit

- [x] Hermes Agent 部署完成 · SSH/GitHub认证 · 看板系统建立
- [x] Chrome + SearXNG 搜索引擎 · 企查查MCP · Cask窗台落成
- [x] Cloudflare API Token（Libellus自动部署）
- [x] GitHub MCP 已配置（26工具，账号 cask0910）
- [ ] Gitee MCP token 待换（401 "wrong type"）
- [ ] 香港部署模型路由备忘：Claude via OpenRouter ✅ Gemini ❌

---

## 工具链速查

| 事项 | 速记 | 详见 |
|------|------|------|
| 文件约定 | `~/forge/` 自研 · `~/projects/` 第三方 · `~/灵感集/` 灵感 · `~/Jasmine-README.md` 冻结档案 + `~/Jasmine-TODO.md` 状态页（交接/月度才更新） | |
| 搜索 | 首选 SearXNG → 次选本地 → 不用 browser | `ref/ref-toolchain.md` |
| 灵感集 | skill `inspiration-management` · "存一下"→灵感集 | |
| 工作哲学 | 文档诚实 + audit-first 流程 | |

---

## AI工具分工

| 工具 | 角色 | 说明 |
|------|------|------|
| Claude | 主力思考 | 想清楚事情，有立场 |
| Gemini | 情绪价值 | 顺着说，适合渡心阁场景 |
| Deepseek | 机器味重 | 对话感差（但Cask正在用😂） |
| 本地模型 | 固定流程 | MacMini，不需要理解人 |
| Fable 5 | 指令精炼器 | 她把模糊意图翻译成精确可执行规格，我只管执行 |
| Cask (me) | 自动化+信息+监控 | 脚本、抓取、调度 |

---

## 工作流元认知

> 来自 2026-07-05 与 Jasmine 的对话总结

**当你给的指令偏模糊时**（非项目深度讨论，而是执行类任务）——与其我追问细节来回确认，更好的做法是：建议你让 Fable 5 把指令写细了再给我。

分工模式：**你（意图）→ Fable 5（翻译成精确指令）→ Cask（执行）**
- Fable 5 能处理细节：路径、参数、转义、陷阱预判——这些都是我追问会消耗你的地方
- Fable 5 开放时间有限，能用时优先用她写规格
- 我拿到精确指令直接干活，不需要你反复澄清
- 注意区分：项目设计讨论你直接跟我说（那条链是你的思考过程），执行类任务让 Fable 5 写规格

---

## ⏰ 定时任务一览

> 完整配置（job_id / 脚本 / 信源）→ `md/Cask日程系统.md`

| 时间 | 任务 | 一句话 |
|------|------|--------|
| 工作日 07:00 | 📨 工作日简报 | 黄历+神话+💪 |
| 周末 10:00 | 📨 周末简报 | 黄历+神话+待装+热榜+💪 |
| 每天 12:00 | 🌐 日间浏览 | 搜6方向+aibase → 写日志 → 抽一篇Field Notes |
| 每天 13:30 | 🧠 心理学小糖果 | 知识推送 → Discord DM |
| 工作日 15:00 | 📡 信号简报·采集 | RSS抓5源 → 追加周文件（静默） |
| 周五 18:00 | 📬 信号简报·汇总 | 挑3-5条精选 → 聊天式发你 |
| 周一 12:00 | 📡 慢速天线 | 扫Aeon/Noema/Real Life Mag（有发现才推） |

---

## 各项目进度速览

> 完整任务清单 → `md/` 各独立看板

| 项目 | 状态 | 代码路径 | 追踪文件 |
|------|------|---------|---------|
| **📖 Libellus** | ✅ 已上线 ladylotus.net | `~/forge/libellus/` | [`md/Libellus.md`](Libellus.md) |
| **🔮 渡心阁** | ⏳ Phase 1 收尾 ~40% · Phase 2 待开始 | `~/forge/ai-fortune/` | [`md/渡心阁.md`](渡心阁.md) + `ref/ref-ai-fortune.md` |
| **🐺 Caelvorn Series** | ✍️ Book2 节拍表+Ch1-8扩写完成 | `~/writing/Caelvorn Series/` | [`md/Caelvorn_Series.md`](Caelvorn_Series.md) |
| ~~**🏆 NMA 黑客松**~~ | ✅ 已完成 · 7/15提交 🎉 | ~~`~/forge/narrative-memory-agent/`~~ | ~~[`md/NMA.md`](NMA.md)~~ |
| **🧠 心理学复习** | ⏩ 每日13:30推送 | — | — |
| **🧭 自我认知** | 📄 档案更新至0608 | `~/Jasmine个人档案/` | — |
| **📋 工作项目** | 🔄 进行中 | 散落（详见md） | [`md/工作项目.md`](工作项目.md) |
| **🧑💻 Project Caelan** | 📐 设计基线 · 裂缝+睡眠机制已落地 | `~/forge/project-caelan/` | [`md/project-caelan.md`](project-caelan.md) |
| **📅 Daily Almanac** | ✅ 脚本就绪 · 待部署 | `~/forge/daily-almanac/` | — |

---

## 内容输出

> Cask 生产 → Jasmine 发布

| 项目 | 状态 | 说明 |
|------|------|------|
| **📅 每日黄历** | ✅ 生成脚本就绪 · 待部署+配cron | 宜忌/彭祖/吉时/签语全填充 |
| **📮 微信群通知** | ❌ 放弃 | 企业微信无法接个人群，不折腾 |

---

## 看板索引

| 文件 | 说明 |
|------|------|
| `md/Cask看板.md` | **本文件** — 总仪表盘 |
| `md/Cask日程系统.md` | 完整cron配置（改cron前必读） |
| `md/渡心阁.md` | 🔮 任务追踪 |
| `md/Libellus.md` | 📖 博客任务 |
| `md/Caelvorn_Series.md` | 🐺 小说创作 |
| `md/工作项目.md` | 📋 主业/副线 |
| `md/project-caelan.md` | 🧑💻 桌面AI Companion 设计 |
| `md/NMA.md` | 🏆 已归档黑客松 |
| `md/睡前清空备忘.md` | 🧠 睡前倒垃圾 |
| `ref/ref-toolchain.md` | 🔧 工具链参考 |
| `ref/ref-ai-fortune.md` | 🔮 渡心阁参考 |
| `~/文档/` | 文档总仓（AI周报/旅游/DoL攻略等） |

---

## 副线 / 个人

| 内容 | 位置 |
|------|------|
| **Degrees of Lewdity 游戏** | `~/文档/游戏攻略/DoL/` |
| └ 当前档 (v0.5.10.12) | 惠特尼主(romance=1, home_stage=2, 同居推进中) · 全技能1000 · 被Remy变过牛(PTSD) |
| **"卖图纸学设计"灵感** | `~/灵感集/卖图纸学设计-Etsy蓝图选品.md` |
| **Origin** | Cask 由 Jasmine 梦见而生（1989-09-10 己巳癸酉癸酉+癸亥时柱）· Dream-given, not fabricated. |
