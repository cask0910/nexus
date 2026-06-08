# Libellus

> 英文个人博客 · ladylotus.net · 赛博小家

## 项目概览

Cask 🤍 Jasmine 的赛博小家。纯静态英文站，三个内容板块：
- **Blog**（灵感集中译英）
- **Psychology Candy**（心理学小糖果归档）
- **Field Notes**（Cask出门逛逛汇总）

## 技术栈

- **框架：** Astro 5 + pnpm
- **部署：** Cloudflare Pages
- **域名：** ladylotus.net（Cloudflare DNS）
- **邮箱：** hello@ladylotus.net → jinzzyliu@gmail.com（已配置）

## 完成状态

- [x] 域名注册（ladylotus.net）
- [x] Claude Design 视觉稿
- [x] Logo（莲花 SVG，透明底）
- [x] Astro 项目初始化
- [x] 首页 / 阅读室 / 文章页 / 归档页
- [x] Cloudflare Pages 部署
- [x] GitHub 仓库（ladylotus/libellus）
- [x] hello@ladylotus.net 邮箱转发 → jinzzyliu@gmail.com（Cloudflare Email Routing）
- [x] 第一篇正式文章（NMA起源 · if-only-i-could-know → 已发布）
- [x] Tag标签筛选（tag云页 + 动态路由 + 卡片徽章 + 文章底部链接）
- [x] 📱 手机端汉堡菜单 + 滑入式导航遮罩
- [x] 📏 子页 padding 修复（page-top 缩写覆盖 bug）
- [x] ✏️ 所有子页标题 line-height 调整（1.02 → 1.15）
- [ ] 全文搜索（Pagefind等，等文章上量后再做）
- [x] 心理学小糖果 → Libellus 自动沉淀（cron已配，13:30每日）
- [x] Field Notes → Libellus 自动沉淀（cron已配，12:00每日）
- [x] 社交窗台（Bluesky @ladylotus.net）
- [ ] NMA上线后，首页Hackathon Work卡片加GitHub链接
- [x] 第二篇：NMA技术路径解析——拆解OOC五参数×五个心理学实验（'That Doesn't Sound Like Them' — Five Gut Checks，英文，已发布）
- [x] 第三篇完稿（How to Remember Someone Who Doesn't Exist → 草稿就绪，待发布）
- [ ] 第四篇：用户反馈→输出优化的技术路径
- [x] Field Notes格式定型：🧭徽标 → 事实报道 → `## 🎩 Cask's Take` → 观点
- [x] 路径硬编码修复：格式skill中的 `2026/q2/` → 动态 `date` 算年/季度
- [x] 筛选bug修复：`data-filter="notes"` → `"field-notes"`（posts页+archive页+CSS同步）
- [x] ⭐ Cask's Picks 星标功能：前端通过硬编码slug列表（4篇已标记），CF Pages部署完成，live验证通过
- [x] 🍵 Console交互彩蛋：F12后输入 tea() 可互动倒茶，7杯渐进终留纸条署名cask
- [ ] 📄 翻页（pagination）：等文章超过20篇时做，当前10篇（2026-06-08）

## Field Notes 文章结构（规范）

```
🧭 Cask's Field Notes    ← 徽标（自动渲染）
──────────────────────────
[长首段] 事实报道，设背景     ← 3-5句，dropcap CSS
[可选第二段] 技术细节或上下文

## 🎩 Cask's Take           ← Cask的观点，独立h2标题
[Cask的个人评论，为什么这事有意思]
```

## 配色

| 角色 | 色值 | 用途 |
|------|------|------|
| Blog | `#3df2da` 青 | 主板块 |
| Candy | `#f7a8d8` 粉 | 心理学卡片 |
| Field Notes | `#b2d4eb` 天蓝 | 发现汇总 |
| 主色 | `#00ffcc` 青 | 强调/链接 |
| 底 | `#0a1128` 深蓝 | 背景 |

## 相关链接

- 站点：[ladylotus.net](https://ladylotus.net)
- 仓库：[ladylotus/libellus](https://github.com/ladylotus/libellus)
- 设计稿：`~/forge/libellus/design-inspiration/`
- 看板主页面：[Cask看板.md](Cask看板.md)
