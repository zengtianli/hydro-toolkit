# Hydro Toolkit

[English](README.md) | **中文**

水利计算工具集 — 水库调度、纳污能力、灌溉需水、水效评估等一站式计算平台。

[![在线演示](https://img.shields.io/badge/%E5%9C%A8%E7%BA%BF%E6%BC%94%E7%A4%BA-hydro.tianlizeng.cloud-brightgreen)](https://hydro.tianlizeng.cloud)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io)

---

### 立即体验 — 无需安装

**https://hydro.tianlizeng.cloud**

上传数据 → 选择工具 → 下载结果。所有工具内置示例数据，零门槛试用。

---

## 功能一览

| 工具 | 功能 | 输入 | 输出 |
|------|------|------|------|
| **纳污能力计算** | 河道/水库纳污能力计算，支持支流分段和多方案 | Excel (流量 + 功能区参数) | Excel (逐月纳污能力) |
| **水库群调度** | 梯级水库发电调度优化计算 | Excel (来水 + 水库参数) | Excel (逐日调度过程) |
| **水效评估** | 工业集聚区水效评估 (AHP+CRITIC+TOPSIS) | Excel (三循环指标数据) | Excel (评分 + 企业排名) |
| **水资源年报** | 浙江省水资源年报数据查询 (2019-2024) | 内置 CSV 数据集 | Excel/CSV 导出 |
| **灌溉需水** | 水稻+旱地灌溉需水量水平衡模拟 | TXT (降雨 + 蒸发) | Excel (逐日需水量) |
| **河区调度** | 19河区逐日水资源供需平衡调度 | TXT (来水 + 需水) | TXT/ZIP (调度结果) |

## 截图

> 即将添加

## 本地部署

### 快速启动

```bash
git clone https://github.com/zengtianli/hydro-toolkit.git
cd hydro-toolkit
pip install -r requirements.txt
streamlit run app.py
```

### Docker (即将支持)

```bash
docker run -p 8504:8504 zengtianli/hydro-toolkit
```

## 项目结构

```
hydro-toolkit/
├── app.py              # 首页 — 工具总览
├── pages/              # Streamlit 多页面应用
│   ├── 1_纳污能力计算.py
│   ├── 2_水库群调度.py
│   ├── 3_水效评估.py
│   ├── 4_水资源年报.py
│   ├── 5_灌溉需水.py
│   └── 6_河区调度.py
├── src/                # 计算引擎
│   ├── capacity/       # 纳污能力核心
│   ├── reservoir/      # 水库调度核心
│   ├── efficiency/     # AHP + CRITIC + TOPSIS
│   ├── annual/         # 年报数据加载器
│   ├── irrigation/     # 灌溉水平衡
│   ├── district/       # 19河区调度器
│   └── common/         # 共享 Streamlit 工具
├── data/               # 示例数据（内置演示）
├── templates/          # Excel 模板
├── requirements.txt
└── LICENSE             # MIT
```

## 技术栈

- **Python 3.9+** — 计算引擎
- **Streamlit** — Web 界面（多页面应用）
- **pandas / numpy / scipy** — 数据处理与数值计算
- **plotly** — 交互式图表
- **openpyxl** — Excel 读写

## 核心算法

| 工具 | 方法 |
|------|------|
| 纳污能力计算 | 一维稳态水质模型 + 支流混合: `W = 31.536 × b × (Cs - C0×e^(-KL/u)) × (QKL/u) / (1 - e^(-KL/u))` |
| 水库群调度 | 梯级水库联合调度 + 水位-库容插值 (scipy) |
| 水效评估 | AHP 主观赋权 + CRITIC 客观赋权，通过 α 滑块组合，TOPSIS 排名 |
| 灌溉需水 | 基于 Penman-Monteith ET₀ 的水稻/旱地水平衡逐日模拟 |
| 河区调度 | 19 河区逐日水平衡 + 动态平衡河区 + 分水枢纽递归分配 |

## 贡献

欢迎提 Issue 和 PR。请先开 Issue 讨论变更内容。

## 许可证

[MIT](LICENSE)
