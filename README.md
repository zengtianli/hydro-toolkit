# 🌊 Hydro Toolkit

**English** | [中文](README_CN.md)

[![GitHub stars](https://img.shields.io/github/stars/zengtianli/hydro-toolkit)](https://github.com/zengtianli/hydro-toolkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-FF4B4B.svg)](https://streamlit.io)

Plugin-based water resource calculation toolkit. Install tools by pasting a GitHub URL — zero code changes required.

![screenshot](docs/screenshots/home.png)

## Architecture

```
hydro-toolkit (Host)          Plugins (git clone)
┌─────────────────┐     ┌──────────────────────┐
│  app.py         │     │  hydro-capacity/     │
│  core/          │────▶│  hydro-reservoir/    │
│  plugins/       │     │  hydro-efficiency/   │
│    hydro-xxx/   │     │  hydro-annual/       │
│    hydro-yyy/   │     │  hydro-irrigation/   │
└─────────────────┘     │  hydro-district/     │
                        └──────────────────────┘
```

The Toolkit is a **host shell** with zero business logic. Each tool is an independent plugin discovered at runtime via `plugin.yaml`.

## Available Plugins

| # | Plugin | Description | Repo |
|---|--------|-------------|------|
| 🌊 | Pollution Capacity | River/reservoir pollution capacity calculator | [hydro-capacity](https://github.com/zengtianli/hydro-capacity) |
| ⚡ | Reservoir Scheduling | Cascade hydropower scheduling optimizer | [hydro-reservoir](https://github.com/zengtianli/hydro-reservoir) |
| 💧 | Water Efficiency | AHP+CRITIC+TOPSIS assessment | [hydro-efficiency](https://github.com/zengtianli/hydro-efficiency) |
| 📊 | Water Annual Report | Zhejiang Province data query (2019–2024) | [hydro-annual](https://github.com/zengtianli/hydro-annual) |
| 🌾 | Irrigation Demand | Paddy + dryland water balance model | [hydro-irrigation](https://github.com/zengtianli/hydro-irrigation) |
| 🗺️ | District Scheduling | 19-district daily supply-demand balance | [hydro-district](https://github.com/zengtianli/hydro-district) |

## Quick Start

```bash
git clone https://github.com/zengtianli/hydro-toolkit.git
cd hydro-toolkit
pip install -r requirements.txt
streamlit run app.py
```

Then go to **Plugin Manager** in the sidebar and paste any plugin repo URL to install it.

## Install a Plugin

1. Open the Toolkit in your browser
2. Click **Plugin Manager** (⚙️) in the sidebar
3. Paste a GitHub URL (e.g. `https://github.com/zengtianli/hydro-capacity`)
4. Click **Install** — the plugin appears in the sidebar immediately

## Develop Your Own Plugin

Create a repo with this structure:

```
hydro-my-tool/
├── plugin.yaml          # Required — metadata
├── app.py               # Required — Streamlit entry point
├── src/my_tool/         # Business logic
├── src/common/st_utils.py  # Shared UI utilities
├── requirements.txt
└── README.md
```

**plugin.yaml**:
```yaml
name: my_tool
title: My Tool Name
icon: "🔧"
order: 70
description: One-line description
version: 1.0.0
```

> **Important**: Do NOT include `src/__init__.py` — it must be absent for namespace package resolution.

See [ARCHITECTURE.md](ARCHITECTURE.md) for full details.

## Deploy (VPS)

```bash
git clone https://github.com/zengtianli/hydro-toolkit.git
cd hydro-toolkit
pip install -r requirements.txt
# Install plugins
cd plugins && git clone https://github.com/zengtianli/hydro-capacity.git && cd ..
# Start
nohup streamlit run app.py --server.port 8510 --server.headless true &
```

## License

MIT
