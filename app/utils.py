import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

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
            "Mean": df[metric].mean(),
            "Median": df[metric].median(),
            "Std Dev": df[metric].std()
        })
    return pd.DataFrame(rows)

def plot_boxplot(data_dict, metric):
    df_all = pd.concat(data_dict.values(), ignore_index=True)
    fig = px.box(df_all, x="Country", y=metric, color="Country", title=f"{metric} Distribution")
    st.plotly_chart(fig, use_container_width=True)

def plot_ghi_ranking(data_dict):
    rows = [{"Country": c, "Average GHI": df["GHI"].mean()} for c, df in data_dict.items()]
    ranking_df = pd.DataFrame(rows).sort_values("Average GHI", ascending=False)
    fig = px.bar(ranking_df, x="Country", y="Average GHI", color="Country", title="Average GHI by Country")
    st.plotly_chart(fig, use_container_width=True)
    
def plot_country_map():
    data = pd.DataFrame({
        'Country': ['Benin', 'Sierra Leone', 'Togo'],
        'Avg_GHI': [240.56, 201.96, 230.56],
        'Latitude': [9.3077, 8.4606, 8.6195],
        'Longitude': [2.3158, -11.7799, 0.8248]
    })

    fig = px.scatter_geo(
        data,
        lat='Latitude',
        lon='Longitude',
        text='Country',
        size='Avg_GHI',
        color='Avg_GHI',
        color_continuous_scale='YlOrRd',
        projection='natural earth',
        title='Average GHI by Country',
        hover_name='Country'
    )

    return fig