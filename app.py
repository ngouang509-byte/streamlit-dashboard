import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# TITLE
# -------------------------
st.title("Student Dashboard")

st.markdown("---")

# -------------------------
# SAMPLE SECTION (replace with your data)
# -------------------------
st.header("Main Analysis")

st.write("This is where your analysis and charts will go.")

# Example chart (replace with your own)
data = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
})

fig, ax = plt.subplots()
ax.bar(data["Category"], data["Values"])

st.pyplot(fig)

st.markdown("---")

# -------------------------
# LSEPI SECTION (TASK 6)
# -------------------------
st.markdown("### LSEPI Considerations")

st.markdown("""
**Ethical:**  
There is a risk that users may misinterpret trends and assume relationships imply causation. The dataset may oversimplify complex real-world behaviour.

**Mitigation:**  
Clear notes were added explaining that the visualisations show correlations only and should not be interpreted as causal relationships.

---

**Professional:**  
Users may misunderstand outputs due to limited context or incorrect use of filters, leading to inconsistent conclusions.

**Mitigation:**  
Labels and explanatory notes were included to explain how filters affect results and how to interpret the charts correctly.
""")
