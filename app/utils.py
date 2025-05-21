import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Define consistent color palette
COLOR_PALETTE = ['#FFB366', '#66B2FF', '#66FFB2']  # Light Orange, Light Blue, Light Green

@st.cache_data
def load_country_data(countries):
    data = {}
    for country in countries:
        try:
            df = pd.read_csv(f"../data/{country.lower().replace(' ', '_')}_clean.csv")
            df["Country"] = country  # Add column for grouping
            data[country] = df
        except FileNotFoundError:
            st.error(f"Data for {country} not found.")
    return data

def get_summary_stats(data_dict, metric):
    rows = []
    for country, df in data_dict.items():
        rows.append({
            "Country": country,
            "Mean": round(df[metric].mean(), 2),
            "Median": round(df[metric].median(), 2),
            "Std Dev": round(df[metric].std(), 2)
        })
    df = pd.DataFrame(rows)
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df.columns),
            fill_color='#FFB366',  # Light Orange
            align='left'
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color=[[
                '#66B2FF', '#66FFB2', '#FFB366'  # Light Blue, Light Green, Light Orange
            ] * len(df) for _ in range(len(df.columns))],
            align='left'
        )
    )])
    fig.update_layout(title=f"{metric} Statistical Summary")
    st.plotly_chart(fig, use_container_width=True)
    return df

def plot_boxplot(data_dict, metric):
    df_all = pd.concat(data_dict.values(), ignore_index=True)
    fig = px.box(df_all, x="Country", y=metric, color="Country", 
                 title=f"{metric} Distribution",
                 color_discrete_sequence=COLOR_PALETTE)
    st.plotly_chart(fig, use_container_width=True)

def plot_ghi_ranking(data_dict):
    rows = [{"Country": c, "Average GHI": df["GHI"].mean()} for c, df in data_dict.items()]
    ranking_df = pd.DataFrame(rows).sort_values("Average GHI", ascending=False)
    fig = px.bar(ranking_df, x="Country", y="Average GHI", color="Country",
                 title="Average GHI by Country",
                 color_discrete_sequence=COLOR_PALETTE)
    st.plotly_chart(fig, use_container_width=True)

def plot_ghi_choropleth():
    data = {
        "Benin": 240.56,
        "Sierra Leone": 201.96,
        "Togo": 230.56,
    }
    iso = {
        "Benin": "BEN",
        "Sierra Leone": "SLE",
        "Togo": "TGO",
    }

    df = pd.DataFrame([{"Country": k, "GHI": v, "ISO": iso[k]} for k, v in data.items()])
    fig = px.choropleth(
        df,
        locations="ISO",
        color="GHI",
        hover_name="Country",
        color_continuous_scale=['#66B2FF', '#FFB366', '#66FFB2'],  # Light Blue, Light Orange, Light Green
        projection="natural earth",
        title="Average GHI by Country"
    )
    return fig
