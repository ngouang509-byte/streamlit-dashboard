import streamlit as st
import pandas as pd
import numpy as np
import re

st.set_page_config(page_title="Business Dashboard Task 4", layout="wide")

st.title("📊 Business Dashboard (Task 4 - Regex Feature Engineering)")

# -------------------------
# DATA
# -------------------------
df = pd.DataFrame({
    "Category": np.random.choice(["Tech-Gadgets", "Tech-Software", "Furniture-Chairs", "Furniture-Tables", "Office-Paper", "Office-Staples"], 400),
    "Region": np.random.choice(["London", "North", "South", "Midlands"], 400),
    "Sales": np.random.randint(50, 1000, 400),
    "Profit": np.random.randint(10, 400, 400)
})

df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

# -------------------------
# REGEX FEATURE ENGINEERING (BASIC REQUIREMENT)
# -------------------------
def map_category(cat):
    if re.search(r"Tech", str(cat)):
        return "Technology"
    elif re.search(r"Furniture", str(cat)):
        return "Furniture"
    elif re.search(r"Office", str(cat)):
        return "Office Supplies"
    else:
        return "Other"

df["Category_Group"] = df["Category"].apply(map_category)

# -------------------------
# INTERMEDIATE: MAPPING TABLE
# -------------------------
st.header("📌 Regex Mapping Example")

mapping_df = df[["Category", "Category_Group"]].drop_duplicates()

st.write("Original → Transformed Mapping")
st.dataframe(mapping_df)

# frequency validation
st.write("### Category Group Distribution")
st.bar_chart(df["Category_Group"].value_counts())

st.divider()

# -------------------------
# FILTER (ADVANCED REQUIREMENT)
# -------------------------
st.sidebar.header("Regex Feature Filter")

group_filter = st.sidebar.multiselect(
    "Select Category Group",
    df["Category_Group"].unique(),
    default=list(df["Category_Group"].unique())
)

filtered_df = df[df["Category_Group"].isin(group_filter)]

# -------------------------
# KPIs (USES REGEX FEATURE)
# -------------------------
st.header("📊 KPIs (Regex-based Analysis)")

col1, col2, col3 = st.columns(3)

col1.metric("Sales", f"£{filtered_df['Sales'].sum():,.0f}")
col2.metric("Profit", f"£{filtered_df['Profit'].sum():,.0f}")
col3.metric("Avg Margin %", round(filtered_df["Profit Margin %"].mean(), 2))

st.divider()

# -------------------------
# CHARTS (USES REGEX FEATURE)
# -------------------------
st.header("📊 Analysis Using Regex Feature")

st.subheader("Sales by Category Group")
st.bar_chart(filtered_df.groupby("Category_Group")["Sales"].sum())

st.subheader("Profit by Category Group")
st.bar_chart(filtered_df.groupby("Category_Group")["Profit"].sum())

st.subheader("Full Dataset")
st.dataframe(filtered_df)

# -------------------------
# INSIGHT
# -------------------------
st.markdown("### 📌 Insight")
st.write(
    "Regex was used to group detailed product categories into broader business segments. "
    "This transformation improves analysis clarity and enables grouped filtering, KPI calculation, and comparative insights."
)
