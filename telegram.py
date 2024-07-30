import streamlit as st
import time

col1, col2 = st.columns([1,8])
with col1:
    st.image("images/Picsart_24-07-27_21-40-00-090.png")
with col2:
    st.header("Telegram Channel Connection Tutorial")
st.info("Connect your bot to a **Telegram** channel chat")
st.caption("---")
st.write("Follow the video instructions")
st.columns([1,4,1])[1].video("Untitled video - Made with Clipchamp (1).mp4")
st.write("---")

if st.session_state.questions == 0:
    st.info("No bot have found!")
else:
    link = st.text_input("The Page Link")
    # bt = st.button("Connect")
    if st.button("Connect"):
        if link == "":
            st.error("Enter the link!")
        else:
            with st.spinner():
                time.sleep(5)
                st.session_state.connected.append({"type": "telegram", "link": link})
                st.success("Connected successfully")
