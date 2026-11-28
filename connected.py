import streamlit as st

# st.divider()
st.header("Your Connected Pages")
# st.divider()

if len(st.session_state.connected) == 0:
    st.info("No connected pages found!")

else:
    i = 0
    # col1, col2 = st.columns([10, 1])
    # with col1:
    #     st.write("Your Pages")
    # with col2:
    #     st.caption("Number")
    #     st.caption("Remove")
    for c in st.session_state.connected:
        col1, col2 = st.columns([10,1])
        with col1:
            st.info(f"Type: {c['type']}  \nLink: {c['link']}")
        with col2:
            bt = st.button(f"{i+1}  \n:material/delete:")
            if bt:
                st.session_state.connected.remove(c)
                st.rerun()
        i += 1

st.divider()







# _______________________________________________________________________
st.header(":primary[:material/share:] Connect your social media accounts")

facebook, instagram, whatsapp, telegram, email = st.tabs(['Facebook', 'Instagram', 'Whatsapp', 'Telegram', 'Email'])
import time
with facebook:
    col1, col2 = st.columns([1,15])
    with col1:
        st.image("images/Picsart_24-07-27_21-39-31-349.png")
    with col2:
        st.subheader("Facebook Page Connection Tutorial")
    # st.info("Connect your bot to a **Facebook** page chat")
    # st.caption("---")
    st.markdown("Follow the video instructions", text_alignment='center')
    st.columns([1,4,1])[1].video("Untitled video - Made with Clipchamp (1).mp4", autoplay=False)
    st.divider()

    if st.session_state.questions == 0:
        st.info("No bot have found!")
    else:
        link = st.text_input("The Page Link", key='facebook')
        # bt = st.button("Connect")
        if st.button("Connect", key='facebookButton'):
            if link == "":
                st.error("Enter the link!")
            else:
                with st.spinner():
                    time.sleep(5)
                    st.session_state.connected.append({"type": "facebook", "link": link})
                    st.success("Connected successfully")

with instagram:
    col1, col2 = st.columns([1,15])
    with col1:
        st.image("images/Picsart_24-07-27_21-40-50-295.png")
    with col2:
        st.subheader("Instagram Page Connection Tutorial")
    # st.info("Connect your bot to an **Instagram** profile chat")
    # st.caption("---")
    st.markdown("Follow the video instructions", text_alignment='center')
    st.columns([1,4,1])[1].video("Untitled video - Made with Clipchamp (1).mp4")
    st.divider()

    if st.session_state.questions == 0:
        st.info("No bot have found!")
    else:
        link = st.text_input("The Page Link", key='instagram')
        # bt = st.button("Connect")
        if st.button("Connect", key='instagramButton'):
            if link == "":
                st.error("Enter the link!")
            else:
                with st.spinner():
                    time.sleep(5)
                    st.session_state.connected.append({"type": "instagram", "link": link})
                    st.success("Connected successfully")

with telegram:
    col1, col2 = st.columns([1,15])
    with col1:
        st.image("images/Picsart_24-07-27_21-40-00-090.png")
    with col2:
        st.subheader("Telegram Channel Connection Tutorial")
    # st.info("Connect your bot to a **Telegram** channel chat")
    # st.caption("---")
    st.markdown("Follow the video instructions", text_alignment='center')
    st.columns([1,4,1])[1].video("Untitled video - Made with Clipchamp (1).mp4")
    st.divider()

    if st.session_state.questions == 0:
        st.info("No bot have found!")
    else:
        link = st.text_input("The Page Link", key='telegram')
        # bt = st.button("Connect")
        if st.button("Connect", key='telegramButton'):
            if link == "":
                st.error("Enter the link!")
            else:
                with st.spinner():
                    time.sleep(5)
                    st.session_state.connected.append({"type": "telegram", "link": link})
                    st.success("Connected successfully")

with whatsapp:
    col1, col2 = st.columns([1,13])
    with col1:
        st.image("images/Picsart_24-07-27_21-39-44-115.png")
    with col2:
        st.subheader("Whatsapp Page Connection Tutorial")
    # st.info("Connect your bot to a **Whatsapp** page chat")
    # st.caption("---")
    st.markdown("Follow the video instructions", text_alignment='center')
    st.columns([1,4,1])[1].video("Untitled video - Made with Clipchamp (1).mp4")
    st.divider()

    if st.session_state.questions == 0:
        st.info("No bot have found!")
    else:
        link = st.text_input("The Page Link", key='whatsapp')
        # bt = st.button("Connect")
        if st.button("Connect", key='whatsappButton'):
            if link == "":
                st.error("Enter the link!")
            else:
                with st.spinner():
                    time.sleep(5)
                    st.session_state.connected.append({"type": "whatsapp", "link": link})
                    st.success("Connected successfully")

with email:
    col1, col2 = st.columns([1,15])
    with col1:
        st.image("images/Picsart_24-07-27_21-39-44-115.png")
    with col2:
        st.subheader("Email Page Connection Tutorial")
    # st.write("Connect your bot to a **Email** page chat")
    # st.divider()
    st.markdown("Follow the video instructions", text_alignment='center')
    st.columns([1,4,1])[1].video("Untitled video - Made with Clipchamp (1).mp4")
    st.divider()

    if st.session_state.questions == 0:
        st.info("No bot have found!")
    else:
        link = st.text_input("The Page Link", key='email')
        # bt = st.button("Connect")
        if st.button("Connect", key='emailButton'):
            if link == "":
                st.error("Enter the link!")
            else:
                with st.spinner():
                    time.sleep(5)
                    st.session_state.connected.append({"type": "whatsapp", "link": link})
                    st.success("Connected successfully")







