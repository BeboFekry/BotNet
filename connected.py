import streamlit as st

st.header("Your Connected Pages")
st.caption("---")

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