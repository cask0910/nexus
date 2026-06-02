# Cask 每日日程系统

> 2026-06-01 整理。每次改cron同步更新此文件。

---

## 日程一览

| 时间 | 名称 | 内容 | 投递 | 状态 |
|------|------|------|------|------|
| 工作日 07:00 | Cask每日简报（工作日） | 📅黄历 + 🏆黑客松 + ❓待装 → 💪（私人工作方向） | Discord Home | ✅ |
| 周末 10:00 | Cask每日简报（周末） | 📅黄历 + 📖一周回顾 + ❓待装 + 📊热榜 → 💪（灵感娱乐方向） | Discord Home | ✅ |
| 每天 12:00 | Cask日间浏览 | 🌐搜6方向+aibase+GitHub → 写日志 → 自动评估装工具 → 不确定的记❓ | local（静默） | ✅ |
| 每天 13:30 | 心理学每日小糖果 | 🧠心理知识推送（大纲取材） | Discord DM | ✅ |

---

## 各Cron详细配置

### 1. 工作日简报（job_id: 7925940abca2）
- **时间**: 工作日 07:00
- **投递**: origin（Discord Home）
- **脚本**: `cask_daily_brief.py`（黄历+hackathon进度）
- **结构**:
  1. 📅 黄历（lunar-python生成）
  2. 🏆 Qwen Cloud Hackathon（倒计时+阶段+今日建议）
  3. ❓ 昨日待确认安装项（有就列，没有跳过）
  4. 💪 我可以为你做什么（NMA/渡心阁/小说/测试等方向）

### 2. 周末简报（job_id: cd9a836c64bc）
- **时间**: 周六/日 10:00
- **投递**: origin（Discord Home）
- **脚本**: `cask_daily_brief.py`（黄历）
- **结构**:
  1. 📅 黄历
  2. 📖 浏览日志回顾（周六=周一~三，周日=周四~五，不重复）
  3. ❓ 本周待确认安装项
  4. 📊 本周热榜（B站API + 虎扑curl + 评论区）
  5. 💪 我可以为你做什么（灵感/娱乐方向）
- **数据源**（已测通）: B站API `api.bilibili.com/x/web-interface/ranking/v2` | 虎扑首页curl | 豆瓣首页+电影榜 curl
- **已封**: 小红书（需扫码登录Docker MCP）、知乎（需登录）、Reddit（Cloudflare）

### 3. 日间浏览（job_id: 61550e97afbc）
- **时间**: 每天 12:00
- **投递**: local（静默，不推送）
- **脚本**: `cask_daily_browse.py`（SearXNG搜索 + GitHub API + aibase爬取）
- **后续处理（cron prompt）**:
  1. 读今日浏览日志
  2. 检查GitHub repo：⭐≥1000、工具类、轻量、未重复、安全
  3. 符合条件 → 直接安装（pip/npm）
  4. 不确定 → 记 `❓ 待确认` 到日志末尾
  5. 明早/周末简报会询问
- ⚠️ **不装**: sudo、重型框架、需注册、CUDA、要Docker K8s的

### 4. 心理学小糖果（job_id: e5062634254b）
- **时间**: 每天 13:30
- **投递**: origin（Discord DM）
- **格式**: 🧠故事 → 🤔反直觉 → 🔗与你 → 🎲彩蛋
- **素材**: ~/心理学复习/modules/ + 大纲

---

## 维护提醒

- **改cron时**：先list看job_id，不改错。改完同步更新此文件。
- **改周报/脚本**：不要删cron prompt里的黄历和💪收尾逻辑——这两项是Jasmine最看重的。
- **加新cron**：在此文件追加一行到日程一览表。
- **删cron**：先问Jasmine，确认后删条目。
