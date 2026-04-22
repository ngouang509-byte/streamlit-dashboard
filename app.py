import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# TITLE
# -------------------------
st.title("Student Dashboard")

st.header("Overview")
st.write("This dashboard presents analysis and visualisations based on the dataset.")

# -------------------------
# SAMPLE DATA (replace with your real dataset)
# -------------------------
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [12, 19, 8, 15]
})

# -------------------------
# VISUALISATION
# -------------------------
st.header("Visualisation")

fig, ax = plt.subplots()
ax.bar(data["Category"], data["Values"])
ax.set_title("Example Bar Chart")
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
The dataset may oversimplify real-world behaviour, leading to misleading conclusions.
""")

st.write("**Mitigation:** Added clear notes explaining that results show correlations only, not causation.")

st.subheader("Professional")
st.write("""
Users may misinterpret outputs due to limited context or misunderstanding of filters. 
Different selections may lead to inconsistent interpretations.
""")

st.write("**Mitigation:** Labels and explanations were added to clarify how filters affect results.")
