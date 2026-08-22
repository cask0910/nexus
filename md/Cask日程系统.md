# Cask 每日日程系统

> 2026-06-01 整理。每次改cron同步更新此文件。

---

## 日程一览

| 时间 | 名称 | 内容 | 投递 | 状态 |
|------|------|------|------|------|
| 工作日 07:00 | Cask每日简报（工作日） | 📅黄历 + 🔧信号摘要 → 💪（私人工作方向） | Discord Home | ✅ |
| 周末 10:00 | Cask每日简报（周末） | 📅黄历 + 🔧安装候选 + 📰热门 → 💪（灵感娱乐方向） | Discord Home | ✅ |
| 每天 12:00 | Cask日间浏览 | 🌐搜6方向+aibase+GitHub → 写日志 → 自动评估装工具 → 不确定的记❓ → 📝精选一篇写 Field Notes 到 Libellus | local（静默） | ✅ |
| 每天 13:30 | 心理学每日小糖果 | 🧠心理知识推送（大纲取材） | Discord DM | ✅ |
| 工作日 15:00 | 信号简报·每日采集 | 📡 精准狙击傻逼过滤器 — 静默抓5源 RSS（Simon Willison/Karpathy/Lilian Weng/OpenAI Blog/Hermes Agent）→ 追加周文件 | local（静默） | ✅ 新增 |
| 周五 18:00 | 信号简报·每周汇总 | 📬 读周文件 → 挑3-5条精选 → 轻松幽默对话式发 Discord | Discord DM | ✅ 新增 |
| 周一 12:00 | 慢速天线 | 📡 慢速天线 — 扫描Aeon/Noema/Real Life Mag RSS + SearXNG句式搜索 | origin（有发现才推） | ✅ 新增 2026-07-29 |
| 每天 12:45 | 人生之书开源监控 | 🎣 蹲小狮日记《人生之书》开源（GitHub中文关键词 + B站新投稿，有发现才推） | origin（有发现才推） | ✅ 新增 2026-08-22 |

---

## 各Cron详细配置

### 1. 工作日简报（job_id: 818b9d4961dc）
- **时间**: 工作日 07:00
- **投递**: origin（Discord Home）
- **脚本**: `cask_daily_brief.py`（黄历数据）
- **结构**:
  1. 📅 黄历（lunar-python生成）
  2. 🔧 今日信号简报采集摘要（读 ~/Cask窗台/信号简报/raw/ 最新采集，提 2-3 条）
  3. 💪 我可以为你做什么（从看板读取：读 Cask看板.md 项目速览 → 挑2-3个进行中方向）
- **变更记录**: 2026-07-10 黑客松进度 → 今日神话/趣闻；2026-07-21 北欧连续剧模式；2026-08-04 铁律硬化（禁止过程元信息，正文逐字进Final Response）+ 修复黄历脚本路径bug（直接取Script Output注入数据）；2026-08-05 💪改为从看板读取（硬编码方向词 → 看板当前状态）；2026-08-11 砍掉神话模块（用户觉得没意思，等想到更有意思的再恢复）→ 工作日=黄历+信号摘要+💪

### 2. 周末简报（job_id: b4753098febb）
- **时间**: 周六/日 10:00
- **投递**: origin（Discord Home）
- **脚本**: `cask_daily_brief.py`（黄历数据）
- **结构**:
  1. 📅 黄历
  2. 🔧 安装候选清单（有就列，没有跳过）
  3. 📰 热门内容（周六=周一二三 / 周日=周四五）
  4. 💪 我可以为你做什么
- **变更记录**: 2026-07-10 黑客松进度 → 今日神话/趣闻；2026-08-04 铁律硬化 + 修复黄历脚本路径bug；2026-08-11 砍掉神话模块 → 周末=黄历+安装候选+热门+💪

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

### 7. 慢速天线（job_id: 3b84f3ea305c）
- **时间**: 每周一 12:00
- **投递**: origin（Discord Home，有发现才推，无发现 [SILENT]）
- **脚本**: `slow_antenna.py`（RSS抓取 + SearXNG搜索 + 三层筛选）
- **信源 A 类（RSS）**:
  1. Aeon — `aeon.co/feed.rss`
  2. Noema Magazine — `noemamag.com/feed/`（需浏览器UA）
  3. Real Life Mag — `reallifemag.com/feed/`
- **信源 B 类（独立作者追踪）**: 初始为空，从捕获中人工加入
- **信源 C 类（SearXNG关键词）**: 按句式搜索（"missing piece" "nobody is building" "infrastructure that doesn't exist" 等，不以话题限定）
- **信源 D 类（触发后深挖）**: 命中后自动追作者其他文章
- **三层筛选**:
  1. 硬排除：<2000词、快消文标题、新闻聚合器
  2. 信号检测：描述缺口/分析瓶颈/跨领域/提出协议层/异见
  3. 质量标记：Cron做前两关，标记"值得一看"推给你
- **命名空间**: `~/Cask窗台/逛逛/慢速天线/`
- **捕获日志**: `captures-YYYY-MM-DD.json`
- **设计哲学**: 与傻逼狙击器独立运行——宁缺毋滥，有发现才推

### 8. 人生之书开源监控（job_id: e63c5519eee6）
- **时间**: 每天 12:45
- **投递**: origin（Discord DM，有新命中才推，否则静默）
- **脚本**: `life_book_watch.py`（GitHub API + B站 API）
- **监控对象**: 小狮日记（B站 mid 444728505）·《我用AI给我家写了一本史书》（2026-08-20）中的"人生之书"app
- **触发条件**:
  1. GitHub 出现 repo 名/描述含「小狮」「人生之书」（中文关键词，排除英文 lifebook 误报）
  2. 小狮日记 B站 近7天新投稿标题含「开源/人生之书/史书/访谈/源代码/GitHub」
- **去重**: 已报命中写入 `~/.hermes/scripts/.life_book_seen.txt`，只报新出现
- **背景**: 灵感集条目 `人生之书-AI为长辈写传记的采访技巧.md`（2026-08-22）——Jasmine 决策：作者开源→直接用；没开源→以后自搓

---

## 维护提醒

- **改cron时**：先list看job_id，不改错。改完同步更新此文件。
- **改周报/脚本**：不要删cron prompt里的黄历和💪收尾逻辑——这两项是Jasmine最看重的。
- **加新cron**：在此文件追加一行到日程一览表。
- **删cron**：先问Jasmine，确认后删条目。
