import streamlit as st
import time

tab1, tab2 = st.tabs(["Languages","Options"])
language = "English"
with tab1:
    # st.write("Languages")
    choice = st.radio("**Default Language**", ["English", "Arabic", "France", "Dutch"], index=0)
    if choice != language:
        with st.spinner(f"Waining while changing language to {choice}"):
            language = choice
            time.sleep(5)
            st.success(f"Language set to {choice}")
with tab2:
    pass