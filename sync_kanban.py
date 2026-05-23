#!/usr/bin/env python3
"""
sync_kanban.py — 轻量看板同步脚本
从 md 看板提取数据 → 安全更新 index.html

安全策略：只替换已知的、唯一的文本标记
No regex DOTALL, no multi-line wildcard matching.

用法：python3 ~/看板/sync_kanban.py
"""
import re
import os
from datetime import datetime

KANBAN_DIR = os.path.expanduser("~/看板")

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def replace_exact(html, old, new):
    """Safe exact string replacement. Warns if not found or not unique."""
    count = html.count(old)
    if count == 0:
        print(f"  ⚠️ 未找到替换目标: {old[:60]}...")
        return html
    if count > 1:
        print(f"  ⚠️ 目标出现{count}次，跳过: {old[:60]}...")
        return html
    return html.replace(old, new)


def main():
    print("🔄 同步看板数据...")

    # Read sources
    cask_md = read_file(os.path.join(KANBAN_DIR, "md", "Cask看板.md"))
    duxinge_md = read_file(os.path.join(KANBAN_DIR, "md", "渡心阁.md"))
    caelvorn_md = read_file(os.path.join(KANBAN_DIR, "md", "Caelvorn_Series.md"))
    html = read_file(os.path.join(KANBAN_DIR, "index.html"))

    now = datetime.now().strftime("%Y-%m-%d %H:%M CST")

    # === Extract progress ===

    # 渡心阁
    m = re.search(r'前端MVP[^~]*~(\d+)%', duxinge_md)
    duxinge_pct = m.group(1) if m else "30"

    # Caelvorn
    m = re.search(r'Book 2:.*?~(\d+)%', caelvorn_md)
    caelvorn_pct = m.group(1) if m else "60"

    # Psychology module progress
    psych_section = cask_md
    if "## 🧠 心理学复习计划" in cask_md:
        psych_section = cask_md.split("## 🧠 心理学复习计划")[1].split("## ")[0]

    modules = []
    for line in psych_section.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 3:
            icon, name, status_part = parts[0], parts[1], parts[2]
            if "📖" in icon or "🎯" in icon:
                status = "✅" if "✅" in status_part else "⬜"
                modules.append((icon, name, status))

    psych_done = sum(1 for _, _, s in modules if s == "✅")
    psych_total = len(modules)
    psych_pct = str(int(psych_done / psych_total * 100)) if psych_total > 0 else "0"

    print(f"  渡心阁: {duxinge_pct}%")
    print(f"  Caelvorn: {caelvorn_pct}%")
    print(f"  心理学: {psych_pct}% ({psych_done}/{psych_total})")

    # === Update HTML ===

    # 1. Timestamp — find whatever's currently there
    ts_match = re.search(r'上次同步：[\d\-: \w]+ CST', html)
    if ts_match:
        html = html.replace(ts_match.group(0), f'上次同步：{now}')
        print("  ✅ 时间戳已更新")
    else:
        print("  ⚠️ 未找到时间戳")

    # 2. Overview: 渡心阁 percentage
    html = replace_exact(html,
        '<span class="value" style="color:var(--teal);">30%</span>',
        f'<span class="value" style="color:var(--teal);">{duxinge_pct}%</span>')

    # 3. Overview: Caelvorn percentage
    html = replace_exact(html,
        '<span class="value" style="color:var(--purple);">60%</span>',
        f'<span class="value" style="color:var(--purple);">{caelvorn_pct}%</span>')

    # 4. Overview: Psychology percentage
    html = replace_exact(html,
        '<span class="value" style="color:var(--azure, #00b4ff);">0%</span>',
        f'<span class="value" style="color:var(--azure, #00b4ff);">{psych_pct}%</span>')

    # 5. Sidebar: Psychology badge
    html = replace_exact(html,
        '<span class="nav-badge" style="background:var(--azure-glow, rgba(0,180,255,0.2));color:var(--azure, #00b4ff);">0%</span>',
        f'<span class="nav-badge" style="background:var(--azure-glow, rgba(0,180,255,0.2));color:var(--azure, #00b4ff);">{psych_pct}%</span>')

    # 6. Sidebar: 渡心阁 badge
    html = replace_exact(html,
        '<span class="nav-badge" style="background:var(--teal-glow);color:var(--teal);">30%</span>',
        f'<span class="nav-badge" style="background:var(--teal-glow);color:var(--teal);">{duxinge_pct}%</span>')

    # 7. Sidebar: Caelvorn badge
    html = replace_exact(html,
        '<span class="nav-badge" style="background:var(--purple-glow);color:var(--purple);">60%</span>',
        f'<span class="nav-badge" style="background:var(--purple-glow);color:var(--purple);">{caelvorn_pct}%</span>')

    # 8. Psychology module items — rebuild the task-group block
    new_items = []
    for icon, name, status in modules:
        status_class = "status-progress" if status == "✅" else "status-pending"
        status_text = "学习中" if status == "✅" else "待开始"
        new_items.append(
            f'            <div class="task-item {status_class}">\n'
            f'              <div class="task-check"></div>\n'
            f'              <div class="task-body">\n'
            f'                <div class="task-title">{icon} {name}</div>\n'
            f'                <div class="task-meta"><span class="task-tag tag-study">{status_text}</span></div>\n'
            f'              </div>\n'
            f'            </div>'
        )
    new_block = "\n".join(new_items)

    # Find the old psych module block between the section-header and the closing </div></div>
    # We know the exact structure from the rebuilt HTML
    old_items_block = ""
    for icon, name, status in modules:
        status_class_old = "status-pending"  # all start as pending in clean HTML
        status_text_old = "待开始"
        old_items_block += (
            f'            <div class="task-item {status_class_old}">\n'
            f'              <div class="task-check"></div>\n'
            f'              <div class="task-body">\n'
            f'                <div class="task-title">{icon} {name}</div>\n'
            f'                <div class="task-meta"><span class="task-tag tag-study">{status_text_old}</span></div>\n'
            f'              </div>\n'
            f'            </div>\n'
        )
    old_items_block = old_items_block.rstrip("\n")

    if old_items_block in html:
        html = html.replace(old_items_block, new_block)
        print("  ✅ 心理学模块已同步")
    else:
        print("  ⚠️ 心理学模块块未匹配，跳过")

    write_file(os.path.join(KANBAN_DIR, "index.html"), html)
    print(f"✅ 看板同步完成！({now})")


if __name__ == "__main__":
    main()
