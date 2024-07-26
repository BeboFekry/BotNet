import streamlit as st
import time
# import requests
# from flask import jsonify
url = "http://127.0.0.1:5000/login"

# app = st.Page("app.py")
log = False
signup = st.Page(r"signup.py", title="Signup", icon=":material/assignment:")
password2 = "admin"
email2 = "admin"
st.write("---")
col1, col2, col3 = st.columns([3,1,3])
with col1:
    st.write("  \n");st.write("  \n")
    st.image(r"images/Login.gif")
with col2:
    pass
with col3:
    st.title("Login")
    email = st.text_input(label="Email", max_chars=50)
    password = st.text_input(label="Password", max_chars=20, type='password')
    if email==email2 and password==password2 and password is not "" and email is not "":
        log = True
    bt = st.button("Login", use_container_width=1)
    if bt:
        if email is "" or password is "":
            st.error("Please enter your data!")
        if log==True:
            # st.write(st.version)
            st.success("Success")
            st.session_state.logged_in = True
            st.rerun()
            # st.balloons()
            # time.sleep(2)
            # body = jsonify({"email": email, "password": password})
            # response = requests.post(url, body)
            # if response.json()['message'] == 'success':
            #     st.session_state.key = response.json()['id']
            #     st.success("Success")
            #     st.session_state.logged_in = True
            #     st.rerun()
            # else:
            #     st.error(response.json()['message'])
        elif password is not "" and email is not "":
            st.error("Wrong email or password!")
    if log is not True:
        st.write("  \n")
        col11, col22 = st.columns([2,1])
        with col11:
            st.write("don't have an account?")
        with col22:
            signup = st.Page(r"signup.py", title="Signup", icon=":material/assignment:")
            bt = st.button("Signup")
            if bt:
                st.switch_page(signup)
            # st.page_link(signup)
st.write("---")

