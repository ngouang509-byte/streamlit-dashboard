import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Final Working Dashboard", layout="wide")

st.title("📊 Dashboard Working Again")

st.write("If you can see this, Streamlit is fully fixed.")

df = pd.DataFrame({
    "Category": ["Tech", "Furniture", "Office"],
    "Sales": [120, 250, 400],
    "Profit": [30, 80, 150]
})

st.dataframe(df)

st.markdown("---")

st.title("⚖️ LSEPI Considerations")

st.subheader("Ethical Consideration")
st.write(
    "This dashboard uses synthetic data for educational purposes. "
    "There is a risk users may treat outputs as real business results, so it is clearly labelled as simulated data."
)

st.subheader("Professional Consideration")
st.write(
    "Users may misinterpret charts or assume causation from correlation. "
    "The dashboard includes explanations and labels to reduce this risk."
)
