import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Business Dashboard Task 2", layout="wide")

st.title("📊 Business Dashboard (Task 2 - Preprocessing)")

df = pd.DataFrame({
    "Category": np.random.choice(["Tech", "Furniture", "Office", None], 300),
    "Region": np.random.choice(["London", "North", "South", None], 300),
    "Sales": np.append(np.random.randint(50, 1000, 295), [None]*5),
    "Profit": np.append(np.random.randint(10, 400, 295), [None]*5)
})

st.sidebar.header("Preprocessing Options")

include_missing = st.sidebar.checkbox("Include Missing Values", value=False)
remove_outliers = st.sidebar.checkbox("Remove Outliers", value=True)

if not include_missing:
    df = df.dropna()
else:
    df["Category"] = df["Category"].fillna("Unknown")
    df["Region"] = df["Region"].fillna("Unknown")
    df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
    df["Profit"] = df["Profit"].fillna(df["Profit"].mean())

df["Sales"] = df["Sales"].astype(float)
df["Profit"] = df["Profit"].astype(float)

df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

if remove_outliers:
    q_low = df["Sales"].quantile(0.05)
    q_high = df["Sales"].quantile(0.95)
    df = df[(df["Sales"] >= q_low) & (df["Sales"] <= q_high)]

st.header("Data Quality Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", len(df))
col2.metric("Missing Values", df.isnull().sum().sum())
col3.metric("Avg Profit Margin %", round(df["Profit Margin %"].mean(), 2))

st.bar_chart(df["Category"].value_counts())

st.divider()

st.header("Analysis")

st.bar_chart(df.groupby("Category")["Sales"].sum())
st.bar_chart(df.groupby("Region")["Profit"].sum())

st.dataframe(df)

st.write("Insight: Preprocessing affects KPIs and charts.")
