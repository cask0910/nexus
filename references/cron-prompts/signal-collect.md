# Cron Prompt: 信号简报·每日采集

- **job_id**: 8594d722458f
- **schedule**: `0 15 * * 1-5`（工作日 15:00）
- **script**: `cask_signal_collect.py`
- **deliver**: local（仅本地）

## 完整提示词

运行采集脚本 cask_signal_collect.py，静默完成即可。无需输出到任何平台。

## 规则
- 静默运行，不输出到 Discord 或其他平台
- 出错时记录日志但不打扰 Jasmine
- 采集结果供日报和汇总使用

## 关联文件
- `~/Cask窗台/信号简报/raw/` — 原始采集数据（JSONL格式）
- `~/Cask窗台/信号简报/cask_signal_collect.py` — 采集脚本
