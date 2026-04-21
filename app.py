# -------------------------
# LSEPI FOOTER (Task 6)
# -------------------------

st.divider()

st.markdown("## ⚖️ LSEPI Considerations")

st.markdown("### 📘 Ethical Consideration")
st.write("""
This dashboard uses randomly generated business data to demonstrate analysis techniques. 
A key ethical risk is that users may assume the results represent real business performance, which could lead to incorrect decisions. 
To mitigate this, the dashboard clearly states that the dataset is synthetic and for educational purposes only.
""")

st.markdown("### 📘 Professional Consideration")
st.write("""
The interpretation of KPIs and statistical outputs may vary depending on user understanding. 
There is a risk that users misinterpret correlations as causation or overlook the impact of filters on results. 
To reduce this, the dashboard includes clear labels, filtering controls, and an interpretation section explaining limitations.
""")
