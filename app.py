import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Business Dashboard Task 3", layout="wide")

st.title("📊 Business Dashboard (Task 3 - Filtering)")

# -------------------------
# DATA
# -------------------------
df = pd.DataFrame({
    "Category": np.random.choice(["Tech", "Furniture", "Office"], 400),
    "Region": np.random.choice(["London", "North", "South", "Midlands"], 400),
    "Sales": np.random.randint(50, 1000, 400),
    "Profit": np.random.randint(10, 400, 400)
})

df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

# -------------------------
# QUALITY TOGGLES (ADVANCED)
# -------------------------
st.sidebar.header("⚙️ Data Quality Controls")

include_missing = st.sidebar.checkbox("Include Missing Values (simulate)", value=False)
remove_outliers = st.sidebar.checkbox("Remove Outliers", value=True)

# simulate missing values
if include_missing:
    df.loc[df.sample(20).index, "Sales"] = np.nan

if not include_missing:
    df = df.dropna()

if remove_outliers:
    q_low = df["Sales"].quantile(0.05)
    q_high = df["Sales"].quantile(0.95)
    df = df[(df["Sales"] >= q_low) & (df["Sales"] <= q_high)]

# -------------------------
# GLOBAL FILTERS (REQUIRED)
# -------------------------
st.sidebar.header("🌍 Global Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=list(df["Category"].unique())
)

region_filter = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

sales_range = st.sidebar.slider(
    "Sales Range",
    int(df["Sales"].min()),
    int(df["Sales"].max()),
    (int(df["Sales"].min()), int(df["Sales"].max()))
)

# apply global filters
filtered_df = df[df["Category"].isin(category_filter)]

if region_filter != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region_filter]

filtered_df = filtered_df[
    (filtered_df["Sales"] >= sales_range[0]) &
    (filtered_df["Sales"] <= sales_range[1])
]

# -------------------------
# DRILL-DOWN FILTERS (REQUIRED SEPARATION)
# -------------------------
st.sidebar.header("🔍 Drill-down Filters")

profit_min = st.sidebar.slider(
    "Minimum Profit",
    int(filtered_df["Profit"].min()),
    int(filtered_df["Profit"].max()),
    int(filtered_df["Profit"].min())
)

drill_df = filtered_df[filtered_df["Profit"] >= profit_min]

# -------------------------
# KPIs
# -------------------------
st.header("📌 KPIs")

col1, col2, col3 = st.columns(3)

col1.metric("Sales", f"£{drill_df['Sales'].sum():,.0f}")
col2.metric("Profit", f"£{drill_df['Profit'].sum():,.0f}")
col3.metric("Avg Margin %", round(drill_df["Profit Margin %"].mean(), 2))

st.divider()

# -------------------------
# CHARTS (MULTIPLE REQUIRED)
# -------------------------
st.header("📊 Analysis (Filtered Views)")

st.subheader("Sales by Category")
st.bar_chart(drill_df.groupby("Category")["Sales"].sum())

st.subheader("Profit by Region")
st.bar_chart(drill_df.groupby("Region")["Profit"].sum())

st.subheader("Profit Margin Distribution")
st.bar_chart(drill_df["Profit Margin %"])

st.subheader("Sales vs Profit (Table View)")
st.dataframe(drill_df)

# -------------------------
# INSIGHT
# -------------------------
st.markdown("### 📌 Insight")
st.write(
    "Filtering significantly changes KPIs and visualisations. "
    "Global filters control overall analysis, while drill-down filters refine detailed insights. "
    "Quality toggles show how preprocessing decisions affect results."
)
