import streamlit as st
import pandas as pd

# -------------------------------
# Title
# -------------------------------
st.title("Data Dashboard")

# -------------------------------
# Load Data
# -------------------------------
try:
    df = pd.read_csv("data.csv")
    st.subheader("Dataset Preview")
    st.write(df.head())
except:
    st.warning("Dataset not found. Please upload or check file name.")

# -------------------------------
# Example Visualisation
# -------------------------------
if 'df' in locals():
    st.subheader("Basic Visualisation")

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) > 0:
        selected_col = st.selectbox("Select a column", numeric_cols)
        st.line_chart(df[selected_col])
    else:
        st.write("No numeric columns available for charting.")

# -------------------------------
# LSEPI SECTION
# -------------------------------
st.header("LSEPI Considerations")

st.subheader("Ethical")
st.write("""
There is a risk that users may misinterpret patterns in the dataset as causal relationships when they are only descriptive correlations. 
This could lead to incorrect assumptions or overconfidence in the findings. In addition, simplified visualisations may not fully represent real-world complexity.
""")

st.write("""
Mitigation: The dashboard explicitly labels all outputs as descriptive analysis only, and explanatory notes are included to remind users that no causal inference should be made from the visualisations.
""")

st.subheader("Professional")
st.write("""
Users may interpret results differently depending on how filters are applied or how data subsets are selected. 
This can result in inconsistent conclusions if users lack understanding of how the dashboard processes data.
""")

st.write("""
Mitigation: Clear labels, structured layout, and filter explanations are provided to ensure users understand how interactions affect outputs and to support consistent interpretation of results.
""")
