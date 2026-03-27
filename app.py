"""
Hydro Toolkit - 水利计算工具集

Water resource calculation toolkit for hydrology professionals.
Navigate to specific tools using the sidebar.
"""

import streamlit as st

st.set_page_config(
    page_title="Hydro Toolkit",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🌊 水利计算工具集 Hydro Toolkit")
st.caption("面向水利专业人员的在线计算平台")

st.markdown(
    '<div style="text-align:center;color:gray;font-size:13px;margin-bottom:1rem;">'
    '⭐ <a href="https://github.com/zengtianli/hydro-toolkit" target="_blank">Star on GitHub</a> · '
    '👤 <a href="https://github.com/zengtianli" target="_blank">Tianli Zeng</a> · '
    '📄 <a href="https://dockit.tianlizeng.cloud" target="_blank">DocKit — 文档工具箱</a>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown("""
### 工具总览

从 **左侧导航栏** 选择工具开始使用。每个工具均内置示例数据，打开即可体验。
""")

tools = [
    {
        "icon": "🌊",
        "name": "纳污能力计算",
        "name_en": "Pollution Capacity",
        "desc": "河道/水库纳污能力计算，支持支流分段和多方案",
        "input": "Excel (流量 + 功能区参数)",
        "output": "Excel (逐月纳污能力)",
    },
    {
        "icon": "⚡",
        "name": "水库群调度",
        "name_en": "Reservoir Scheduling",
        "desc": "梯级水库发电调度优化计算",
        "input": "Excel (来水 + 水库参数)",
        "output": "Excel (逐日调度过程)",
    },
    {
        "icon": "💧",
        "name": "水效评估",
        "name_en": "Water Efficiency",
        "desc": "工业集聚区水效评估 (AHP+CRITIC+TOPSIS)",
        "input": "Excel (三循环指标数据)",
        "output": "Excel (评分 + 企业排名)",
    },
    {
        "icon": "📊",
        "name": "水资源年报",
        "name_en": "Water Annual Report",
        "desc": "浙江省水资源年报数据查询与导出",
        "input": "内置 CSV 数据集",
        "output": "Excel/CSV 导出",
    },
    {
        "icon": "🌾",
        "name": "灌溉需水",
        "name_en": "Irrigation Demand",
        "desc": "水稻+旱地灌溉需水量水平衡计算",
        "input": "TXT (降雨 + 蒸发 + 灌区参数)",
        "output": "Excel (逐日需水量)",
    },
    {
        "icon": "🗺️",
        "name": "河区调度",
        "name_en": "District Scheduling",
        "desc": "19河区逐日水资源供需平衡调度",
        "input": "TXT (来水 + 需水 + 静态参数)",
        "output": "TXT/ZIP (调度结果)",
    },
]

cols = st.columns(3)
for i, tool in enumerate(tools):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="border:1px solid #e0e0e0; border-radius:10px; padding:16px; margin-bottom:12px; min-height:200px;">
            <h3>{tool['icon']} {tool['name']}</h3>
            <p style="color:gray; font-size:13px;">{tool['name_en']}</p>
            <p>{tool['desc']}</p>
            <p style="font-size:12px;">
                <b>输入：</b>{tool['input']}<br/>
                <b>输出：</b>{tool['output']}
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### 快速开始

1. 从左侧导航栏 **选择工具**
2. **上传数据** 或使用内置示例数据
3. **运行计算** 并下载结果

所有工具均内置示例数据，**打开即用，零门槛体验**。

""")

st.markdown("---")
st.markdown(
    '<div style="text-align:center;color:gray;font-size:13px;">'
    'Open Source · '
    '⭐ <a href="https://github.com/zengtianli/hydro-toolkit" target="_blank">Star on GitHub</a> · '
    'Built by <a href="https://github.com/zengtianli" target="_blank">Tianli Zeng</a>'
    '<br/>'
    'More tools: '
    '📄 <a href="https://dockit.tianlizeng.cloud" target="_blank">DocKit — 文档工具箱</a>'
    '</div>',
    unsafe_allow_html=True,
)
