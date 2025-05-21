import streamlit as st
from utils import (
    load_country_data,
    plot_boxplot,
    plot_ghi_ranking,
    get_summary_stats,
    plot_ghi_choropleth,
)

# --- Page Config ---
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# --- Inject CSS ---
st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlock"] > div:nth-child(2) {
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title("Solar Data Explorer")
st.markdown("Explore and compare solar potential across Benin, Sierra Leone, and Togo.")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Options")
selected_countries = st.sidebar.multiselect(
    "Select countries to compare:",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Togo"]
)

selected_metric = st.sidebar.selectbox(
    "Select metric to visualize:",
    ["GHI", "DNI", "DHI"]
)

# --- Load Data ---
data_dict = load_country_data(selected_countries)

# --- Display Visualizations ---
if data_dict:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribution Analysis")
        with st.container():
            plot_boxplot(data_dict, selected_metric)

    with col2:
        st.subheader("🗺️ Geographic Overview")
        with st.container():
            st.plotly_chart(plot_ghi_choropleth(), use_container_width=True)

    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("🏆 Performance Ranking")
        with st.container():
            plot_ghi_ranking(data_dict)

    with col4:
        st.subheader("📋 Statistical Summary")
        with st.container():
            get_summary_stats(data_dict, selected_metric)
else:
    st.warning("Please select at least one country to view data.")
