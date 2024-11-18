import streamlit as st


st.title('_You should become a_')
st.title(f':blue[{st.session_state["prediction"].title()}]')

st.header("Suggestion")
for i in st.session_state['suggestions']:
    st.markdown(f"### {i}")


st.balloons()
