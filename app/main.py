import streamlit as st
from utils import load_country_data, plot_boxplot, plot_ghi_ranking, get_summary_stats

# --- Page Config ---
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# --- Title ---
st.title("☀️ Solar Data Explorer")
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
    st.subheader(f"📊 Boxplot: {selected_metric} Comparison")
    plot_boxplot(data_dict, selected_metric)

    st.subheader("📋 Summary Statistics")
    summary_df = get_summary_stats(data_dict, selected_metric)
    st.dataframe(summary_df)

    st.subheader("🏆 Average GHI Ranking")
    plot_ghi_ranking(data_dict)
else:
    st.warning("Please select at least one country to view data.")
