# Cron Prompt: 信号简报·每周汇总

- **job_id**: bb2c635e516d
- **schedule**: `0 18 * * 5`（周五 18:00）
- **deliver**: origin（Discord，周报）
- **workdir**: `/home/ubuntu`

## 完整提示词

先跑 `date` 确认当前时间。

# 任务：生成本周信号简报

本周的原始采集数据在 ~/Cask窗台/信号简报/raw/ 下，文件名格式 week-YYYY-WW.jsonl。
打开当前周的文件，读取并分析采集到的信号。

## 输出格式
1. 本周信号总览（采集量、关键主题）
2. 重要信号详细说明（每条附来源和分析）
3. 趋势判断
4. 建议关注

## 规则
- 先跑 `date` 确认时间
- 发送到 Discord

## 关联文件
- `~/Cask窗台/信号简报/raw/week-YYYY-WW.jsonl` — 本周原始数据
- `~/Cask窗台/信号简报/` — 工具目录
