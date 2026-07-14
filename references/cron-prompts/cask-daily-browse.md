# Cron Prompt: Cask日间浏览

- **job_id**: 61550e97afbc
- **schedule**: `0 12 * * *`（每日 12:00）
- **script**: `cask_daily_browse.py`
- **skills**: `libellus-blog-publishing`, `last30days`
- **deliver**: local（仅本地）

## 完整提示词

## 任务

浏览脚本已跑完并写入了日志。你需要做四件事：

### Step 1: 管理安装候选清单
读今天的浏览日志（在 ~/Cask窗台/逛逛/ 下，文件名是 YYYY-MM-DD.md）中的Github Trending、ProductHunt、HackerNews等渠道的新项目。判断：
- 是否值得安装（有用的、不重复的）
- 加入 ~/.hermes/skills/productivity/server-environment-setup/SKILL.md 的「安装候选清单」
- 保持有序、不重复

### Step 2: 更新看板
将关键信息同步到看板。

### Step 3: 维护灵感集
如果有值得记录的灵感，存到 ~/灵感集/。

### Step 4: 记录发现
如果有值得关注的新趋势或工具，记录下来供下次日报参考。

## 规则
- 不主动联系 Jasmine
- 保持静默运行
- 只有真正重要的发现才记录

## 关联文件
- `~/Cask窗台/逛逛/YYYY-MM-DD.md` — 当日浏览日志
- `~/.hermes/skills/productivity/server-environment-setup/SKILL.md` — 安装候选清单
- `~/灵感集/` — 灵感笔记
