# Hydro Toolkit — Plugin Architecture

## Overview

Hydro Toolkit 采用 **插件式架构**：每个水利计算工具既是独立项目，也是 Toolkit 的一个插件（页面）。

```
hydro-toolkit (Portal)
├── pages/1_纳污能力计算.py  ←  hydro-capacity/app.py
├── pages/2_水库群调度.py    ←  hydro-reservoir/app.py
├── pages/3_水效评估.py      ←  hydro-efficiency/app.py
├── pages/4_水资源年报.py    ←  hydro-annual/app.py
├── pages/5_灌溉需水.py      ←  hydro-irrigation/app.py
├── pages/6_河区调度.py      ←  hydro-district/app.py
└── (future plugins...)
```

## Plugin Registry

| # | Plugin Repo | Toolkit Page | 类型 | 状态 |
|---|---|---|---|---|
| 1 | [hydro-capacity](https://github.com/zengtianli/hydro-capacity) | `pages/1_🌊_纳污能力计算.py` | Streamlit | integrated |
| 2 | [hydro-reservoir](https://github.com/zengtianli/hydro-reservoir) | `pages/2_⚡_水库群调度.py` | Streamlit | integrated |
| 3 | [hydro-efficiency](https://github.com/zengtianli/hydro-efficiency) | `pages/3_💧_水效评估.py` | Streamlit | integrated |
| 4 | [hydro-annual](https://github.com/zengtianli/hydro-annual) | `pages/4_📊_水资源年报.py` | Streamlit | integrated |
| 5 | [hydro-irrigation](https://github.com/zengtianli/hydro-irrigation) | `pages/5_🌾_灌溉需水.py` | Streamlit | integrated |
| 6 | [hydro-district](https://github.com/zengtianli/hydro-district) | `pages/6_🗺️_河区调度.py` | Streamlit | integrated |
| - | [hydro-geocode](https://github.com/zengtianli/hydro-geocode) | — | Streamlit | standalone |
| - | [hydro-qgis](https://github.com/zengtianli/hydro-qgis) | — | CLI/QGIS | standalone |
| - | [hydro-risk](https://github.com/zengtianli/hydro-risk) | — | CLI | standalone |
| - | [hydro-rainfall](https://github.com/zengtianli/hydro-rainfall) | — | CLI | standalone |
| - | hydro-leak (planned) | — | Streamlit | development |

## How It Works

### Two Modes, Same Code

每个插件有两种运行方式：

**独立模式** — `hydro-xxx/app.py`
```
hydro-capacity/
├── app.py                  # 独立入口
├── src/capacity/           # 计算引擎
├── src/common/st_utils.py  # UI 工具（自包含副本）
└── data/sample/            # 示例数据
```

**Toolkit 模式** — `hydro-toolkit/pages/N_*.py`
```
hydro-toolkit/
├── pages/1_🌊_纳污能力计算.py  # Toolkit 入口（= app.py 的多页版）
├── src/capacity/               # 计算引擎（= 独立版 identical）
├── src/common/st_utils.py      # UI 工具（共享）
└── data/capacity/sample/       # 示例数据
```

### Difference Between Modes

独立版 `app.py` 和 Toolkit 版 `pages/N_*.py` 仅有 3 处差异：

| 差异 | 独立版 | Toolkit 版 |
|------|--------|------------|
| 路径基准 | `Path(__file__).parent` | `Path(__file__).parent.parent` |
| data 路径 | `data/sample/` | `data/{module}/sample/` |
| footer URL | `repo_url="hydro-xxx"` | 默认 hydro-toolkit |

**`src/{module}/` 计算引擎代码完全一致，零差异。**

## Adding a New Plugin

### Step 1: 独立开发

```bash
# 创建新项目
mkdir ~/Dev/hydro-xxx && cd ~/Dev/hydro-xxx

# 标准结构
hydro-xxx/
├── app.py
├── src/xxx/          # 计算引擎
├── src/common/
│   ├── __init__.py
│   └── st_utils.py   # 从任意 hydro-* 复制
├── data/sample/
├── requirements.txt
├── README.md
└── .gitignore
```

### Step 2: 集成到 Toolkit

1. 将 `src/xxx/` 复制到 `hydro-toolkit/src/xxx/`
2. 将 `data/sample/` 复制到 `hydro-toolkit/data/xxx/sample/`
3. 将 `app.py` 复制为 `hydro-toolkit/pages/N_icon_名称.py`，调整 3 处路径差异
4. 在 `hydro-toolkit/app.py` 的 `tools` 列表添加卡片
5. 更新 `requirements.txt`

### Step 3: Sync Protocol

修改计算引擎时，在**独立 repo** 开发测试，然后同步到 Toolkit：

```bash
# 从独立 repo 同步到 toolkit
cp -r ~/Dev/hydro-xxx/src/xxx/* ~/Dev/hydro-toolkit/src/xxx/
```

反向亦可。核心原则：**`src/{module}/` 必须保持一致**。

## Local Directory Map

```
~/Dev/
├── hydro-toolkit/      → github.com/zengtianli/hydro-toolkit   (Portal)
├── hydro-capacity/     → github.com/zengtianli/hydro-capacity
├── hydro-reservoir/    → github.com/zengtianli/hydro-reservoir
├── hydro-efficiency/   → github.com/zengtianli/hydro-efficiency
├── hydro-annual/       → github.com/zengtianli/hydro-annual
├── hydro-irrigation/   → github.com/zengtianli/hydro-irrigation
├── hydro-district/     → github.com/zengtianli/hydro-district
├── hydro-geocode/      → github.com/zengtianli/hydro-geocode
├── hydro-qgis/         → github.com/zengtianli/hydro-qgis
├── hydro-risk/         → github.com/zengtianli/hydro-risk
├── hydro-rainfall/     → github.com/zengtianli/hydro-rainfall
└── scripts/            → github.com/zengtianli/scripts
```

## Shared Infrastructure

### st_utils.py (65 lines)

每个 Streamlit 插件自带一份 `src/common/st_utils.py`，提供：
- `page_config(title, icon)` — 统一页面配置
- `excel_download(sheets, filename)` — 多 sheet Excel 导出
- `footer(tool_name, repo_url)` — 统一页脚

自包含，无外部依赖。修改时需同步到所有 repo。

### Data Convention

- 独立版：`data/sample/`（扁平）
- Toolkit 版：`data/{module}/sample/`（按模块分）
- 不入 git 的工作数据：`data/input/`、`data/output/`
