# Cask 每日日程系统

> 2026-06-01 整理。每次改cron同步更新此文件。

---

## 日程一览

| 时间 | 名称 | 内容 | 投递 | 状态 |
|------|------|------|------|------|
| 工作日 07:00 | Cask每日简报（工作日） | 📅黄历 + 🌍今日神话/趣闻 → 💪（私人工作方向） | Discord Home | ✅ |
| 周末 10:00 | Cask每日简报（周末） | 📅黄历 + 🌍今日神话/趣闻 + ❓待装 + 📊热榜 → 💪（灵感娱乐方向） | Discord Home | ✅ |
| 每天 12:00 | Cask日间浏览 | 🌐搜6方向+aibase+GitHub → 写日志 → 自动评估装工具 → 不确定的记❓ → 📝精选一篇写 Field Notes 到 Libellus | local（静默） | ✅ |
| 每天 13:30 | 心理学每日小糖果 | 🧠心理知识推送（大纲取材） | Discord DM | ✅ |
| 工作日 15:00 | 信号简报·每日采集 | 📡 精准狙击傻逼过滤器 — 静默抓5源 RSS（Simon Willison/Karpathy/Lilian Weng/OpenAI Blog/Hermes Agent）→ 追加周文件 | local（静默） | ✅ 新增 |
| 周五 18:00 | 信号简报·每周汇总 | 📬 读周文件 → 挑3-5条精选 → 轻松幽默对话式发 Discord | Discord DM | ✅ 新增 |

---

## 各Cron详细配置

### 1. 工作日简报（job_id: 818b9d4961dc）
- **时间**: 工作日 07:00
- **投递**: origin（Discord Home）
- **脚本**: `cask_daily_brief.py`（黄历数据）
- **结构**:
  1. 📅 黄历（lunar-python生成）
  2. 🌍 今日神话/趣闻（每日一地区/主题，不重复）
  3. 💪 我可以为你做什么（NMA/渡心阁/小说/测试等方向）
- **变更记录**: 2026-07-10 黑客松进度 → 今日神话/趣闻

### 2. 周末简报（job_id: b4753098febb）
- **时间**: 周六/日 10:00
- **投递**: origin（Discord Home）
- **脚本**: `cask_daily_brief.py`（黄历数据）
- **结构**:
  1. 📅 黄历
  2. 🌍 今日神话/趣闻（周末可长一点，7-10行）
  3. 🔧 安装候选清单（有就列，没有跳过）
  4. 📰 热门内容（周六=周一二三 / 周日=周四五）
  5. 💪 我可以为你做什么
- **变更记录**: 2026-07-10 黑客松进度 → 今日神话/趣闻

### 3. 日间浏览（job_id: 61550e97afbc）
- **时间**: 每天 12:00
- **投递**: local（静默，不推送）+ ~/forge/libellus/ Field Notes .md（自动按年份/季度分目录）
- **脚本**: `cask_daily_browse.py`（SearXNG搜索 + GitHub API + aibase爬取）
- **skill**: `libellus-field-notes-format`（格式定义）
- **后续处理（cron prompt）**:
  1. 读今日浏览日志
  2. 检查GitHub repo：⭐≥1000、工具类、轻量、未重复、安全
  3. 符合条件 → 直接安装（pip/npm）
  4. 不确定 → 记 `❓ 待确认` 到日志末尾
  5. 明早/周末简报会询问
  6. 从今日日志中选最有意思的发现 → 写英文 Field Notes .md 到 Libellus
- **Field Notes 文章结构**:
  ```
  [长首段] 事实报道（dropcap）
  [可选第二段] 更多上下文
  ## 🎩 Cask's Take
  [个人观点，为什么这事有意思]
  ```
- ⚠️ **不装**: sudo、重型框架、需注册、CUDA、要Docker K8s的

### 4. 心理学小糖果（job_id: e5062634254b）
- **时间**: 每天 13:30
- **投递1**: origin（Discord DM）— 中文版
- **投递2**: ~/forge/libellus/src/content/posts/（自动按日期算年份/季度目录）— 英文版 .md
- **格式**: 🧠故事 → 🤔反直觉 → 🔗与你 → 🎲彩蛋
- **素材**: ~/心理学复习/modules/ + 大纲

### 5. 信号简报·每日采集（job_id: 8594d722458f）
- **时间**: 工作日 15:00
- **投递**: local（静默，不推送）
- **脚本**: `cask_signal_collect.py`（RSS抓取 + XML解析 + 去重）
- **信源**:
  1. Simon Willison — `simonwillison.net/atom/everything/`
  2. Andrej Karpathy — `karpathy.github.io/feed.xml`
  3. Lilian Weng — `lilianweng.github.io/index.xml`
  4. OpenAI Blog — `openai.com/news/rss.xml`（需浏览器UA）
  5. Hermes Agent — `github.com/NousResearch/hermes-agent/releases.atom`
- **输出**: `~/Cask窗台/信号简报/raw/week-YYYY-WW.jsonl`（增量追加）
- **别名**: 精准狙击傻逼过滤器 🤠

### 6. 信号简报·每周汇总（job_id: bb2c635e516d）
- **时间**: 周五 18:00
- **投递**: origin（Discord DM to Jasmine）
- **内容**: 读本周 `.jsonl` → 挑 3-5 条精选 → 轻松幽默对话式发 Discord
- **风格**: 不要表格，像朋友聊天，每条约一两句话说清"是什么+为什么值得看"
- **筛选标准**: Signal over noise / 多样性 / 跟Jasmine相关加分 / 时效性优先

---

## 维护提醒

- **改cron时**：先list看job_id，不改错。改完同步更新此文件。
- **改周报/脚本**：不要删cron prompt里的黄历和💪收尾逻辑——这两项是Jasmine最看重的。
- **加新cron**：在此文件追加一行到日程一览表。
- **删cron**：先问Jasmine，确认后删条目。
