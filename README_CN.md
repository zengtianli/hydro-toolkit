# 🌊 水利计算工具集 Hydro Toolkit

[English](README.md) | **中文**

[![GitHub stars](https://img.shields.io/github/stars/zengtianli/hydro-toolkit)](https://github.com/zengtianli/hydro-toolkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-FF4B4B.svg)](https://streamlit.io)

插件式水利计算工具集。粘贴 GitHub URL 即可安装工具，无需修改代码。

![screenshot](docs/screenshots/home.png)

## 架构

```
hydro-toolkit (Host)          插件 (git clone)
┌─────────────────┐     ┌──────────────────────┐
│  app.py         │     │  hydro-capacity/     │
│  core/          │────▶│  hydro-reservoir/    │
│  plugins/       │     │  hydro-efficiency/   │
│    hydro-xxx/   │     │  hydro-annual/       │
│    hydro-yyy/   │     │  hydro-irrigation/   │
└─────────────────┘     │  hydro-district/     │
                        └──────────────────────┘
```

Toolkit 是一个**纯 Host 壳**，零业务代码。每个工具是独立插件，通过 `plugin.yaml` 在运行时被发现。

## 已有插件

| # | 插件 | 说明 | 仓库 |
|---|------|------|------|
| 🌊 | 纳污能力计算 | 河道/水库纳污能力计算 | [hydro-capacity](https://github.com/zengtianli/hydro-capacity) |
| ⚡ | 水库群调度 | 梯级水电调度优化 | [hydro-reservoir](https://github.com/zengtianli/hydro-reservoir) |
| 💧 | 水效评估 | AHP+CRITIC+TOPSIS 综合评价 | [hydro-efficiency](https://github.com/zengtianli/hydro-efficiency) |
| 📊 | 水资源年报 | 浙江省数据查询（2019–2024） | [hydro-annual](https://github.com/zengtianli/hydro-annual) |
| 🌾 | 灌溉需水 | 水稻+旱地水量平衡模型 | [hydro-irrigation](https://github.com/zengtianli/hydro-irrigation) |
| 🗺️ | 河区调度 | 19河区逐日供需平衡 | [hydro-district](https://github.com/zengtianli/hydro-district) |

## 快速开始

```bash
git clone https://github.com/zengtianli/hydro-toolkit.git
cd hydro-toolkit
pip install -r requirements.txt
streamlit run app.py
```

然后在侧边栏点击 **插件管理**，粘贴插件仓库 URL 即可安装。

## 安装插件

1. 在浏览器中打开 Toolkit
2. 点击侧边栏的 **插件管理**（⚙️）
3. 粘贴 GitHub URL（如 `https://github.com/zengtianli/hydro-capacity`）
4. 点击 **安装** — 插件立即出现在侧边栏

## 开发自己的插件

创建以下结构的仓库：

```
hydro-my-tool/
├── plugin.yaml          # 必须 — 元数据
├── app.py               # 必须 — Streamlit 入口
├── src/my_tool/         # 计算逻辑
├── src/common/st_utils.py  # 共享 UI 工具
├── requirements.txt
└── README.md
```

**plugin.yaml**:
```yaml
name: my_tool
title: 我的工具
icon: "🔧"
order: 70
description: 一句话描述
version: 1.0.0
```

> **重要**: 不要包含 `src/__init__.py` — namespace package 要求必须缺失。

详见 [ARCHITECTURE.md](ARCHITECTURE.md)。

## 部署（VPS）

```bash
git clone https://github.com/zengtianli/hydro-toolkit.git
cd hydro-toolkit
pip install -r requirements.txt
# 安装插件
cd plugins && git clone https://github.com/zengtianli/hydro-capacity.git && cd ..
# 启动
nohup streamlit run app.py --server.port 8510 --server.headless true &
```

## 许可证

MIT
