import streamlit as st

st.set_page_config(page_title="Clean Test App", layout="wide")

st.title("📊 App Working Test")

st.write("If you see this, Streamlit is working correctly.")

st.markdown("---")

st.title("⚖️ LSEPI Considerations")

st.subheader("Ethical Consideration")
st.write(
    "This dashboard uses synthetic data for educational purposes. "
    "There is a risk that users may interpret outputs as real-world results. "
    "To prevent this, the dataset is clearly labelled as simulated."
)

st.subheader("Professional Consideration")
st.write(
    "Users may misinterpret charts or assume causation from correlation. "
    "To reduce this risk, the dashboard includes explanations and limitations."
)
