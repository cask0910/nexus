# 🍲 嫁嫁菜单 · 全家点菜台

> 本地：`~/forge/grandma-menu/` · 单机原版 `grandma-menu.html` → 共享版 `public/index.html`
> 线上：`https://menu.ladylotus.net/jiajia/`（嫁嫁家点菜台）· `https://menu.ladylotus.net/nainai/`（奶奶家点菜台）· `/big` 结尾=大字页
> 部署：本机 Node + Cloudflare Tunnel · systemd 常驻（`grandma-menu.service` + `cloudflared.service`）
> 定位：全家共享实时点菜台——三个人（Jasmine/弟弟/妈妈）远程点菜实时同步，嫁嫁/奶奶只看大字页
> 双家分区：2026-08-21 上线 · 路径分区（子域名需 Cloudflare 面板操作，路径方案零操作）
> 双家主题：2026-08-21 · 嫁嫁家暖橙红 / 奶奶家青蓝（品牌名+静态title+canvas图+全部衍生色按家切换）
> 最后更新：2026-08-23（嫁嫁家菜库裁剪：29 内置 + 2 自定义）

---

## 项目背景

- **使用者**：点菜 = Jasmine / 弟弟 / 妈妈（分散各地，需远程）；看菜 = 嫁嫁（老年人，需要大字号，不点菜只接收）
- **嫁嫁流程**：三人点完生成今日菜单 → 嫁嫁打开 `/big` 大字页即可看到"今天吃什么 + 要备什么菜"，不用等发图
- **奶奶家**：未来可复用（点菜人不同，都是老人做饭），需数据隔离（新部署一套）
- 诞生：原单机版 localStorage（`grandma-menu.html`）→ 2026-08-21 改造为服务器共享版

---

## 架构

| 层 | 选型 |
|----|------|
| 前端 | 单文件 HTML 零依赖（`public/index.html` 点菜台 + `public/big.html` 大字页） |
| 后端 | Node 零依赖 HTTP 服务（`server.js`），端口 8080 |
| 存储 | `data/state-jiajia.json` + `data/state-nainai.json` 按家分区，原子写 + 每日备份保留 30 天（`data/backups/`） |
| 分区 | 路径分区：`/jiajia/*` 嫁嫁家 · `/nainai/*` 奶奶家 · `/` 302 → `/jiajia/`（旧链接不失效） |
| 主题 | 一份代码 CSS 双主题（`body.theme-nainai` 变量覆盖）：嫁嫁家暖橙红 / 奶奶家青蓝；品牌、静态 title、canvas 图、全部衍生色按家切换；中性面板用 `--soft-bg` 系列 |
| 同步 | 前端每 3 秒轮询 `<home>/api/state`；点菜/撤销走 `<home>/api/pick` 即时推送 |
| 暴露 | Cloudflare Tunnel（token 模式）→ `menu.ladylotus.net`，自动 HTTPS，无需开放入站端口 |
| 常驻 | systemd：`grandma-menu.service`（node）+ `cloudflared.service`（tunnel），开机自启 |

### API
- `GET /api/state` — 全量 {dishes, orders, settings, picked}
- `POST /api/state` — 增量更新（dishes/orders/settings 按 key）
- `POST /api/pick` — {id, diner} 点菜 / {id} 撤菜 / {clear:true} 清空

---

## 状态

- [x] 单机版完成（原 `grandma-menu.html`，36 道内置湖北菜）
- [x] 共享版改造（localStorage → 服务器同步，移除示例数据）
- [x] 嫁嫁大字页 `/big`（只读 · 超大字号 · 10 秒自动刷新 · 显示今日菜单+备菜+昨日未做）
- [x] systemd 常驻 + 开机自启
- [x] Cloudflare Tunnel 上线 `menu.ladylotus.net` ✅ 2026-08-21
- [x] 本地 git 管理（首次提交 78e1efd）
- [x] 双家分区：`/jiajia/` + `/nainai/`，数据按家隔离 ✅ 2026-08-21（commit 6d9fb46）
- [x] 双家主题区分：嫁嫁暖橙红 / 奶奶青蓝，品牌名+静态title+canvas图按家切换 ✅ 2026-08-21（commit 90a26dc）
- [x] 主题收尾：残留暖色全部变量化 + 修 server 静态替换多余 `>` + 中性面板 soft 变量 + 生成按钮/进度条渐变 gen 变量 ✅ 2026-08-21（7e5407b / 32e4617 / 3bb0773 / 34cf723）
- [x] 奶奶家已启用（Jasmine 自行配置点菜人：皇军/琦琦/净净，已开始使用）✅ 2026-08-21
- [x] 嫁嫁家菜库裁剪：删除 7 道嫁嫁不会做的菜（白灼虾/糍粑鱼/热干面/三鲜豆皮/葱油拌面/藕夹/清蒸武昌鱼），内置库 36→29；新增自定义菜：茶树菇炒肉、泡菜苕粉肉丝 ✅ 2026-08-23
- [x] 静态页加 `Cache-Control: no-cache, no-store` — 防旧缓存页 BUILTIN 合并把已删菜加回 ✅ 2026-08-23（commit 36398e4）
- [x] 默认菜库 +11 道（肉沫豆腐/蒸鸡蛋/干锅花菜/芹菜干子肉丝/苋菜/梅菜扣肉/鸡蛋饼/胡萝卜烧肉/玉米排骨汤/红烧冬瓜/胡萝卜丝炒肉丝）+ 茶树菇炒肉、泡菜苕粉肉丝转内置 — 内置 29→42，嫁嫁家 42 道 ✅ 2026-08-23
- [x] 每家隐藏列表（hidden）：修复"假删除"——删内置菜=进本家隐藏列表永久生效、不影响另一家；boot 合并跳过隐藏菜并清理残留；「恢复内置菜库」取消隐藏；导入过滤隐藏菜 ✅ 2026-08-23
- [ ] 验证：嫁嫁家家人实际使用反馈（三天试运行）

---

## 产品改造（点菜 / 做菜双角色）

- **状态**：讨论中 · 触发：奶奶家食材找菜需求 + 现有 UI 整体改造
- **方案全文**：`~/forge/grandma-menu/docs/产品改造方案.md`（双角色入口、做菜端 Duolingo 式一屏一步、视觉系统升级）
- **要点**：角色=点菜人/做菜人（不叫老人版）；做菜端含食材找菜向导 + 菜谱视频/步骤卡；数据接入 599 道 MIT 菜谱（细节见 docs/食材找菜集成方案.md）

---

## 运维备忘

- **启动/重启**：`sudo systemctl restart grandma-menu`（node）/ `sudo systemctl restart cloudflared`（tunnel）
- **日志**：`sudo journalctl -u grandma-menu -n 50` / `sudo journalctl -u cloudflared -n 50`
- **数据**：`data/state.json`（实时）+ `data/backups/YYYY-MM-DD.json`（每日）
- **改代码**：改 `public/` 下文件 → `git add -A && git commit`（node 服务读文件无需重启；改 server.js 需 `sudo systemctl restart grandma-menu`）
- **git**：`~/forge/grandma-menu/` 本地仓库（未推远程，暂不需要）

_最后更新：2026-08-23_
