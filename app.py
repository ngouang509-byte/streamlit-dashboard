import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Business Dashboard Task 5", layout="wide")

st.title("📊 Business Dashboard (Task 5 - Descriptive Statistics)")

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
# FILTERS (so stats respond to filters - ADVANCED REQUIREMENT)
# -------------------------
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Category",
    df["Category"].unique(),
    default=list(df["Category"].unique())
)

region_filter = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=list(df["Region"].unique())
)

filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Region"].isin(region_filter))
]

# -------------------------
# BASIC DESCRIPTIVE STATISTICS
# -------------------------
st.header("📌 Summary Statistics")

st.write("### Sales Summary")
st.write(filtered_df["Sales"].describe())

st.write("### Profit Summary")
st.write(filtered_df["Profit"].describe())

# custom stats (mean, median, min, max, IQR)
q1 = filtered_df["Sales"].quantile(0.25)
q3 = filtered_df["Sales"].quantile(0.75)
iqr = q3 - q1

stats_df = pd.DataFrame({
    "Metric": ["Mean", "Median", "Min", "Max", "IQR"],
    "Sales": [
        filtered_df["Sales"].mean(),
        filtered_df["Sales"].median(),
        filtered_df["Sales"].min(),
        filtered_df["Sales"].max(),
        iqr
    ]
})

st.dataframe(stats_df)

st.divider()

# -------------------------
# GROUPED STATS (INTERMEDIATE)
# -------------------------
st.header("📊 Grouped Descriptive Statistics")

group_stats = filtered_df.groupby("Category")[["Sales", "Profit"]].agg([
    "mean", "median", "min", "max"
])

st.dataframe(group_stats)

st.divider()

# -------------------------
# DISTRIBUTION VIEWS (ADVANCED)
# -------------------------
st.header("📈 Distribution Analysis")

st.subheader("Sales Distribution (Histogram)")
st.bar_chart(filtered_df["Sales"].value_counts().sort_index())

st.subheader("Profit Distribution (Box View Approximation)")
st.bar_chart(filtered_df["Profit"].value_counts().sort_index())

st.divider()

# -------------------------
# KPI SUMMARY
# -------------------------
st.header("📌 KPI Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Sales", round(filtered_df["Sales"].mean(), 2))
col2.metric("Avg Profit", round(filtered_df["Profit"].mean(), 2))
col3.metric("Avg Margin %", round(filtered_df["Profit Margin %"].mean(), 2))

# -------------------------
# INTERPRETATION (ADVANCED REQUIREMENT)
# -------------------------
st.markdown("### 📌 Interpretation")

st.write("""
These statistics describe central tendency (mean, median), spread (range, IQR), and distribution patterns.

However:
- They do NOT explain causation.
- They are sensitive to outliers.
- They do not capture time-based or external factors affecting performance.

Grouped statistics help compare categories, but do not imply one category causes higher performance.
""")
