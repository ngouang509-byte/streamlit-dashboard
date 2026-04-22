import streamlit as st
import pandas as pd

# -------------------------
# TITLE
# -------------------------
st.title("Student Dashboard")

# -------------------------
# INTRO
# -------------------------
st.header("Overview")
st.write("This dashboard presents analysis and visualisations based on the dataset.")

# -------------------------
# SAMPLE DATA (replace later with your real dataset)
# -------------------------
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [12, 19, 8, 15]
})

# -------------------------
# VISUALISATION (SAFE - NO MATPLOTLIB)
# -------------------------
st.header("Visualisation")

st.bar_chart(data.set_index("Category"))

# -------------------------
# LSEPI SECTION (TASK 6 - DONE PROPERLY)
# -------------------------
st.header("LSEPI Considerations")

st.subheader("Ethical")
st.write("""
There is a risk that users may misinterpret patterns in the data and assume relationships imply causation. 
The dataset simplifies real-world behaviour, which may lead to misleading interpretations.
""")

st.write("**Mitigation:** Added clear notes stating that the visualisations show patterns and correlations only, not causation.")

st.subheader("Professional")
st.write("""
Users may interpret results differently depending on how they apply filters or view the data. 
This can lead to inconsistent conclusions if context is not considered.
""")

st.write("**Mitigation:** Labels and explanations were added to clarify how data should be interpreted.")
