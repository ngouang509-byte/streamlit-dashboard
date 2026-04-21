
import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# PAGE SETUP
# -------------------------
st.set_page_config(page_title="Business Dashboard", layout="wide")

st.title("📊 Executive Summary & Drill-Down Dashboard")

# -------------------------
# SAMPLE DATA
# -------------------------
df = pd.DataFrame({
    "Category": np.random.choice(["Technology", "Furniture", "Office Supplies"], 300),
    "Region": np.random.choice(["London", "North", "South", "Midlands"], 300),
    "Sales": np.random.randint(50, 1000, 300),
    "Profit": np.random.randint(10, 400, 300)
})

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.header("Filters")

category = st.sidebar.selectbox("Select Category", ["All"] + list(df["Category"].unique()))
region = st.sidebar.selectbox("Select Region", ["All"] + list(df["Region"].unique()))

filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

# -------------------------
# EXECUTIVE SUMMARY
# -------------------------
st.header("Executive Summary")

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
avg_sales = filtered_df["Sales"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"£{total_sales:,.0f}")
col2.metric("Total Profit", f"£{total_profit:,.0f}")
col3.metric("Average Sales", f"£{avg_sales:,.0f}")

st.divider()

# -------------------------
# DRILL-DOWN ANALYSIS
# -------------------------
st.header("Drill-Down Analysis")

st.subheader("Sales by Category")
st.bar_chart(filtered_df.groupby("Category")["Sales"].sum())

st.subheader("Profit by Region")
st.bar_chart(filtered_df.groupby("Region")["Profit"].sum())

st.subheader("Data Table")
st.dataframe(filtered_df)

# -------------------------
# INSIGHT
# -------------------------
st.markdown("### 📌 Business Insight")
st.write(
    "Sales and profit vary across categories and regions, highlighting opportunities for targeted business strategies and performance improvement."
)
