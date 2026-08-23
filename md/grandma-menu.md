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

## 方案：食材找菜（集成「来做菜」数据）

> 状态：**待确认** · 需求方：奶奶家（手头食材能做什么菜）· 数据源：YunYouJun/cook（MIT，599 道居家菜谱）

### 为什么这样接

「来做菜」是开源项目（MIT 可商用，标注来源即可），菜谱数据是一个 **44KB 的 recipe.csv** 躺在仓库里，599 道菜，每道含：菜名 / 食材（逗号分隔）/ B站视频号 / 难度 / 厨具 / 做法标签。食材分类也是现成的（素菜/荤菜/主食，带 emoji 和别名如 番茄=西红柿）。

数据这么轻，**不用部署他们的应用，直接把数据搬进来**，在我们自己的页面里做匹配——界面保持自家风格（老人用惯），菜谱用他们的。

### 数据层

- 新增 `public/recipes.json`：从 recipe.csv 转换（stuff/tools 解析成数组），一次导入
- 新增 `public/foods.json`：从 food.ts 提取食材分类 + 别名表
- 前端 fetch 这两个文件，**server.js 零改动**（静态文件直接读）
- 同步机制：手动脚本 `scripts/sync-recipes.py`（拉 GitHub raw → 重新生成 json），以后想更新跑一次即可；也可以挂 cron 每周自动拉
- 来源标注：页面底部「菜谱数据来自云游君 YunYouJun/cook（MIT）」

### 匹配逻辑（前端）

1. **自家菜库优先**：先把用户选的食材跟自家 42 道菜的 ings 匹配，命中就标「🏠 家里会做」排最前
2. **全库补充**：599 道里 stuff 包含所选食材的
3. **两种模式**（照抄他们的交互）：
   - 严格匹配：所选食材全部命中
   - 生存模式：命中任意 1 个就行，按命中数排序（食材快用完时好用）
4. **厨具过滤**：一口大锅（默认）/ 空气炸锅 / 烤箱 / 微波炉 / 电饭煲
5. 别名表兜底（番茄↔西红柿）

### UI（新增「食材找菜」tab，两家通用）

- 选食材：分组 emoji 大按钮（🥬素菜 🥩荤菜 🍚主食）
- 选厨具：一排图标
- 结果卡片：菜名 / 食材清单 / 难度 / 🎬 跳 B 站视频（BV 号拼 bilibili.com/video/BV...）
- 大字、图标化，符合老人使用习惯

### 工作量

| 步骤 | 内容 | 量 |
|---|---|---|
| 1 | 数据转换脚本 + 生成 recipes.json/foods.json | 小 |
| 2 | 「食材找菜」页 UI（选食材/厨具/模式切换） | 中 |
| 3 | 匹配逻辑（自家优先 + 全库 + 别名） | 中 |
| 4 | 测试（两家各自菜库优先）+ 上线 | 小 |

### 边界与风险

- 600 道是网友投稿居家菜谱，做法未必跟奶奶习惯一致 → 自家 42 道优先设计就是为了缓解这一点
- B站视频部分可能无版权/失效（BV 号是作者投稿的）→ 卡片上视频只是跳转，菜谱文字本身够用
- 数据不是实时更新的 → 手动/定时同步足够（菜谱变化很慢）
- 老人若用不惯全库，可只展示「🏠 家里会做」结果（设置里开关）

### 不做的事

- 不部署他们的应用（数据接入已足够）
- 不做「今天吃这个→加入今日点菜」联动（二期可加）
- 不接飞书表格实时拉取（CSV 同步够用）

---

## 运维备忘

- **启动/重启**：`sudo systemctl restart grandma-menu`（node）/ `sudo systemctl restart cloudflared`（tunnel）
- **日志**：`sudo journalctl -u grandma-menu -n 50` / `sudo journalctl -u cloudflared -n 50`
- **数据**：`data/state.json`（实时）+ `data/backups/YYYY-MM-DD.json`（每日）
- **改代码**：改 `public/` 下文件 → `git add -A && git commit`（node 服务读文件无需重启；改 server.js 需 `sudo systemctl restart grandma-menu`）
- **git**：`~/forge/grandma-menu/` 本地仓库（未推远程，暂不需要）

_最后更新：2026-08-23_
