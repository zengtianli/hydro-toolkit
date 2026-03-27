# Hydro Toolkit

**English** | [中文](README_CN.md)

Water resource calculation toolkit — reservoir scheduling, pollution capacity, irrigation demand, water efficiency assessment, and more.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-hydro.tianlizeng.cloud-brightgreen)](https://hydro.tianlizeng.cloud)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io)

---

### Try it now — no install needed

**https://hydro.tianlizeng.cloud**

Upload your data, pick a tool, download the result. Zero setup. All tools include sample data for instant demo.

---

## What can Hydro Toolkit do?

| Tool | What it does | Input | Output |
|------|-------------|-------|--------|
| **Pollution Capacity** | Calculate river/reservoir pollution capacity with tributary segmentation | Excel (flow + zone params) | Excel (monthly capacity) |
| **Reservoir Scheduling** | Multi-reservoir cascaded hydropower dispatch optimization | Excel (inflow + reservoir params) | Excel (daily schedule) |
| **Water Efficiency** | AHP + CRITIC + TOPSIS assessment for industrial parks | Excel (3-cycle indicators) | Excel (scores + ranking) |
| **Water Annual Report** | Query Zhejiang province water resource annual data (2019-2024) | Built-in CSV dataset | Excel/CSV export |
| **Irrigation Demand** | Paddy + dryland irrigation water balance simulation | TXT (rainfall + evaporation) | Excel (daily demand) |
| **District Scheduling** | Regional water allocation for 19 districts with sluice cascade | TXT (inflow + demand) | TXT/ZIP (balance results) |

## Screenshots

### Homepage
![Homepage](docs/screenshots/homepage.png)

### Tools
| | |
|---|---|
| ![Pollution Capacity](docs/screenshots/capacity.png) | ![Reservoir Scheduling](docs/screenshots/reservoir.png) |
| ![Water Efficiency](docs/screenshots/efficiency.png) | ![Water Annual Report](docs/screenshots/annual.png) |
| ![Irrigation Demand](docs/screenshots/irrigation.png) | ![District Scheduling](docs/screenshots/district.png) |

## Self-host

### Quick start

```bash
git clone https://github.com/zengtianli/hydro-toolkit.git
cd hydro-toolkit
pip install -r requirements.txt
streamlit run app.py
```

### With Docker (coming soon)

```bash
docker run -p 8504:8504 zengtianli/hydro-toolkit
```

## Project structure

```
hydro-toolkit/
├── app.py              # Homepage — tool overview
├── pages/              # Streamlit multi-page apps
│   ├── 1_Pollution_Capacity.py
│   ├── 2_Reservoir_Scheduling.py
│   ├── 3_Water_Efficiency.py
│   ├── 4_Water_Annual_Report.py
│   ├── 5_Irrigation_Demand.py
│   └── 6_District_Scheduling.py
├── src/                # Calculation engines
│   ├── capacity/       # Pollution capacity core
│   ├── reservoir/      # Hydropower scheduling core
│   ├── efficiency/     # AHP + CRITIC + TOPSIS
│   ├── annual/         # Annual report data loader
│   ├── irrigation/     # Paddy/dryland water balance
│   ├── district/       # 19-district scheduler
│   └── common/         # Shared Streamlit utilities
├── data/               # Sample data (built-in demos)
├── templates/          # Excel templates
├── requirements.txt
└── LICENSE             # MIT
```

## Tech stack

- **Python 3.9+** — calculation engine
- **Streamlit** — web interface (multi-page app)
- **pandas / numpy / scipy** — data processing & numerical computation
- **plotly** — interactive charts
- **openpyxl** — Excel I/O

## Key algorithms

| Tool | Method |
|------|--------|
| Pollution Capacity | One-dimensional steady-state model with tributary mixing: `W = 31.536 × b × (Cs - C0×e^(-KL/u)) × (QKL/u) / (1 - e^(-KL/u))` |
| Reservoir Scheduling | Cascaded hydropower dispatch with water-level/storage interpolation (scipy) |
| Water Efficiency | AHP subjective + CRITIC objective weighting, combined via α slider, TOPSIS ranking |
| Irrigation Demand | Penman-Monteith ET₀ based paddy/dryland water balance with daily time step |
| District Scheduling | Daily water balance across 19 districts with dynamic equilibrium zones and sluice cascade |

## Contributing

Issues and PRs are welcome. Please open an issue first to discuss changes.

## License

[MIT](LICENSE)
