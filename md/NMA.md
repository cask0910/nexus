# NMA 黑客松 · 已归档 🏆🎉

> **状态：已完成 · 2026年7月15日提交 · 结果：未获奖（2026-08-29 公布）**
> **代码路径：** `~/forge/narrative-memory-agent/`
> 项目：Narrative Memory Agent · Qwen Cloud Global AI Hackathon Track 1: MemoryAgent
> 仓库：`~/forge/narrative-memory-agent/`（GitHub 私有 `ladylotus/narrative-memory-agent` · 本地与远端同步）· 服务器：47.84.196.253（阿里云 ECS 新加坡 1C1G）**已随黑客松结束释放** → 服务器端每日 04:00 冷备 crontab 随之终止

### 赛后复盘（2026-08-29）
- 未获奖 → 五家记忆方向获奖项目全部开源，代码级深扒 → **研究文档转入 project-caelan**（`docs/RESEARCH_MEMORY_WINNERS_20260829.md`，含 R1-R6 落点）
- 收获：FAMA 成为记忆评测事实基准；行业共识 = 显式遗忘 + 可验证 + 可辩护；Reverie（人物记忆/证据门）与 Quên（世界记忆/验证闭环）互补，直接服务 Caelan 记忆架构

### 关键产出
- 三代记忆架构：WorkingMemory → Consolidation → SleepCycle（OOC五因子×心理学实验）
- 前端：四角色 P&P 场景演示（Lena/Caelan/Cedric/Mirabelle）
- 文档：Demo脚本 + 技术路径解析essay + Devpost描述

### 留存资产
- `~/forge/narrative-memory-agent/` — 完整代码仓库（GitHub 私有，含 `backend/app/seed.py` + `scripts/reseed_full.py`，演示库可重建）
- `~/forge/libellus/` — "That Doesn't Sound Like Them" 技术解析文章
- `~/forge/backups/nma-backups/` — 服务器释放后的**最后一份数据留存**：
  - `nma-production-snapshot-20260705-2041.tar.gz`（419KB）= `nma.db` 806KB（表 `events`/`event_archive`/`characters`/`session_state`，7 角色 / 44 events）+ 完整 chroma 向量库
  - `profile-baseline-20260705.json`（7 角色名单）
  - ⚠️ 这是**迁移重灌前**的 7 角色版，不是生产 4 角色（Lena/Caelan/Cedric/Mirabelle）版
- 经验（通用化后记入 Cask看板.md 工作哲学 + ref/ref-toolchain.md）
