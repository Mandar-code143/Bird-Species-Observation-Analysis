import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.markdown("""
### Bird Species Observation Analysis

This dashboard analyzes bird observations across
Forest and Grassland habitats to identify biodiversity
patterns, conservation priorities, and environmental influences.
""")

st.download_button(
    "Download Cleaned Dataset",
    data=open("Cleaned_Bird_Data.csv","rb"),
    file_name="Cleaned_Bird_Data.csv",
    mime="text/csv"
)


# ----------------------------
# LOAD DATA
# ----------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("Cleaned_Bird_Data.csv")
    return df

df = load_data()

# ----------------------------
# TITLE
# ----------------------------

st.title("🐦 Bird Species Observation Analysis Dashboard")

st.markdown("---")

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------

st.sidebar.header("Filters")

habitat_filter = st.sidebar.multiselect(
    "Select Habitat",
    options=df["Habitat"].dropna().unique(),
    default=df["Habitat"].dropna().unique()
)

season_filter = st.sidebar.multiselect(
    "Select Season",
    options=df["Season"].dropna().unique(),
    default=df["Season"].dropna().unique()
)

filtered_df = df[
    (df["Habitat"].isin(habitat_filter))
    &
    (df["Season"].isin(season_filter))
]

species = st.selectbox(
    "Search Species",
    sorted(filtered_df["Common_Name"].dropna().unique())
)

species_data = filtered_df[
    filtered_df["Common_Name"] == species
]

st.write(species_data.head())

st.set_page_config(
    page_title="Bird Species Observation Analysis",
    page_icon="🐦",
    layout="wide"
)
# ----------------------------
# KPI SECTION
# ----------------------------

total_obs = len(filtered_df)

total_species = filtered_df["Scientific_Name"].nunique()

forest_records = len(
    filtered_df[filtered_df["Habitat"] == "Forest"]
)

grass_records = len(
    filtered_df[filtered_df["Habitat"] == "Grassland"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Observations", total_obs)

col2.metric("Unique Species", total_species)

col3.metric("Forest Records", forest_records)

col4.metric("Grassland Records", grass_records)

st.markdown("---")

# ----------------------------
# TOP SPECIES
# ----------------------------

st.subheader("Top 10 Most Observed Bird Species")

top_species = (
    filtered_df["Common_Name"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_species.columns = ["Species", "Count"]

fig_species = px.bar(
    top_species,
    x="Species",
    y="Count",
    title="Top 10 Species"
)

st.plotly_chart(
    fig_species,
    use_container_width=True
)

# ----------------------------
# HABITAT ANALYSIS
# ----------------------------

st.subheader("Habitat Analysis")

habitat_count = (
    filtered_df["Habitat"]
    .value_counts()
    .reset_index()
)

habitat_count.columns = ["Habitat", "Count"]

fig_habitat = px.pie(
    habitat_count,
    names="Habitat",
    values="Count",
    title="Forest vs Grassland Observations"
)

st.plotly_chart(
    fig_habitat,
    use_container_width=True
)

# ----------------------------
# SEASON ANALYSIS
# ----------------------------

st.subheader("Seasonal Trends")

season_data = (
    filtered_df.groupby("Season")
    .size()
    .reset_index(name="Observations")
)

fig_season = px.bar(
    season_data,
    x="Season",
    y="Observations",
    title="Bird Observations by Season"
)

st.plotly_chart(
    fig_season,
    use_container_width=True
)

# ----------------------------
# TEMPERATURE ANALYSIS
# ----------------------------

st.subheader("Temperature Analysis")

temp_data = filtered_df.dropna(
    subset=["Temperature"]
)

fig_temp = px.histogram(
    temp_data,
    x="Temperature",
    nbins=30,
    title="Temperature Distribution"
)

st.plotly_chart(
    fig_temp,
    use_container_width=True
)

# ----------------------------
# HUMIDITY ANALYSIS
# ----------------------------

st.subheader("Humidity Analysis")

humidity_data = filtered_df.dropna(
    subset=["Humidity"]
)

fig_humidity = px.histogram(
    humidity_data,
    x="Humidity",
    nbins=30,
    title="Humidity Distribution"
)

st.plotly_chart(
    fig_humidity,
    use_container_width=True
)

# ----------------------------
# SKY CONDITIONS
# ----------------------------

st.subheader("Sky Conditions")

sky_data = (
    filtered_df["Sky"]
    .value_counts()
    .reset_index()
)

sky_data.columns = ["Sky", "Count"]

fig_sky = px.bar(
    sky_data,
    x="Sky",
    y="Count",
    title="Sky Condition Analysis"
)

st.plotly_chart(
    fig_sky,
    use_container_width=True
)

# ----------------------------
# WIND CONDITIONS
# ----------------------------

st.subheader("Wind Conditions")

wind_data = (
    filtered_df["Wind"]
    .value_counts()
    .head(10)
    .reset_index()
)

wind_data.columns = ["Wind", "Count"]

fig_wind = px.bar(
    wind_data,
    x="Wind",
    y="Count",
    title="Wind Condition Analysis"
)

st.plotly_chart(
    fig_wind,
    use_container_width=True
)

# ----------------------------
# CONSERVATION DASHBOARD
# ----------------------------

st.subheader("Conservation Insights")

watchlist_species = filtered_df[
    filtered_df["PIF_Watchlist_Status"] == True
]["Scientific_Name"].nunique()

stewardship_species = filtered_df[
    filtered_df["Regional_Stewardship_Status"] == True
]["Scientific_Name"].nunique()

c1, c2 = st.columns(2)

c1.metric(
    "Watchlist Species",
    watchlist_species
)

c2.metric(
    "Stewardship Species",
    stewardship_species
)

# ----------------------------
# BIODIVERSITY HOTSPOTS
# ----------------------------

st.subheader("Biodiversity Hotspots")

hotspots = (
    filtered_df.groupby("Admin_Unit_Code")
    ["Scientific_Name"]
    .nunique()
    .reset_index()
)

hotspots.columns = [
    "Park",
    "Species_Count"
]

hotspots = hotspots.sort_values(
    by="Species_Count",
    ascending=False
)

fig_hotspot = px.bar(
    hotspots,
    x="Park",
    y="Species_Count",
    title="Species Diversity by Park"
)

st.plotly_chart(
    fig_hotspot,
    use_container_width=True
)

st.markdown("---")

st.success(
    "Dashboard Loaded Successfully"
)