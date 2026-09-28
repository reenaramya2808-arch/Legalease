import streamlit as st

st.title("Legalease")

st.write("AI-powered legal document generator")

user_input = st.text_area("Enter your legal document requirement:")

if st.button("Generate"):
    if user_input:
        st.write("Your legal document will be generated here.")
    else:
        st.warning("Please enter your requirement.")
