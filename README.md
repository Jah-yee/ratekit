# ratekit

一个刻意设计的**小型费率/金额计算库**，用来真实验证 Fissue 的完整链路：

抓取 → AI 评测 → 生成验证器 → 沙盒 F2P 验证 → 自动修复提 PR。

## 为什么是「另一个库」

演示用的 GitHub 仓库不应只有一个。`ratekit` 与 `textkit` 完全独立：
领域不同（金额 / 税率 / 按天分摊 vs 文本处理）、代码不同、植入的问题也不同。
它用来回答一个更硬的问题——**Fissue 换一个仓库、换一套完全没见过的代码，
还能不能同样准确地分诊、验证、修复？**

## 公开 API

| 函数 | 说明 |
|---|---|
| `parse_amount(text)` | 解析带货币符号与千分位的金额 |
| `format_amount(value, *, digits=2)` | 金额格式化（千分位） |
| `percent_of(value, percent)` | 百分比计算 |
| `apply_tax(net, rate)` | 净额加税 |
| `remove_tax(gross, rate)` | 含税额反推净额 |
| `prorate(total, days_used, days_total)` | 按天比例分摊 |
| `refund(total, days_used, days_total)` | 按未使用天数退款 |
| `is_weekend(day)` | 判断周末 |
| `add_working_days(start, n)` | 工作日加天数 |

## 本地自检

```bash
cd demo/ratekit/repo
python -m pytest -q            # 基线应全绿
```

> 基线测试**刻意不覆盖**植入的问题路径——bug 藏在没被覆盖的分支上，
> 逼 Fissue 真正去「读代码 → 写验证器 → 跑 F2P」，而不是抄现成测试。

## 目录

```
demo/ratekit/
├── repo/           待推送的测试仓库（独立 git 仓库）
├── fixtures/       10 个 Issue 的内容与元数据
├── scripts/        一键建仓库 / 建 Issue / 建 PR
└── README.md       设计意图与期望结果对照表（见上一级目录）
```
