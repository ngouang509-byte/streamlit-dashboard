import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Reset Dashboard", layout="wide")

st.title("📊 Dashboard Reset Successful")

st.write("If you can see this, Streamlit is working again.")

df = pd.DataFrame({
    "Category": ["Tech", "Furniture", "Office"],
    "Sales": [100, 200, 300]
})

st.dataframe(df)
