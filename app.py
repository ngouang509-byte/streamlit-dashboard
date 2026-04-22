import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
# SAMPLE DATA + CHART
# (Replace this with your real dataset)
# -------------------------
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [12, 19, 8, 15]
})

st.header("Visualisation")

fig, ax = plt.subplots()
ax.bar(data["Category"], data["Values"])
ax.set_title("Sample Bar Chart")
ax.set_xlabel("Category")
ax.set_ylabel("Values")

st.pyplot(fig)

# -------------------------
# LSEPI SECTION (TASK 6)
# -------------------------
st.header("LSEPI Considerations")

st.subheader("Ethical")
st.write("""
There is a risk that users may misinterpret trends and assume relationships imply causation. 
The dataset may oversimplify complex real-world behaviour, leading to misleading conclusions.
""")

st.write("**Mitigation:** Clear notes were added stating that the visualisations show correlations only, not causation.")

st.subheader("Professional")
st.write("""
Users may misinterpret outputs due to limited context or misunderstanding of filter effects. 
Different selections can lead to inconsistent interpretations across users.
""")

st.write("**Mitigation:** Labels and explanatory notes were included to explain how filters affect results and interpretation.")
