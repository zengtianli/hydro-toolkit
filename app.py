"""
Hydro Toolkit — 水利计算工具集

插件式架构：通过 GitHub URL 一键安装水利计算工具。
"""
import sys
from pathlib import Path

import streamlit as st

from core.plugin_loader import discover_plugins

# --- Page config (must be first Streamlit call) ---
st.set_page_config(
    page_title="Hydro Toolkit",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Discover plugins ---
plugins = discover_plugins()

# Add each plugin's directory to sys.path so its internal imports work
for p in plugins:
    p_str = str(p.path)
    if p_str not in sys.path:
        sys.path.insert(0, p_str)

# --- Build navigation ---
pages = [st.Page("core/home.py", title="首页", icon="🏠", default=True)]

for p in plugins:
    pages.append(st.Page(
        str(p.path / "app.py"),
        title=p.title,
        icon=p.icon,
        url_path=p.name,
    ))

pages.append(st.Page("core/manage.py", title="插件管理", icon="⚙️"))

nav = st.navigation(pages)
nav.run()
