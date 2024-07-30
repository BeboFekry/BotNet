import streamlit as st
import datetime
import time
import requests
from flask import jsonify


@st.dialog("Terms of use:")
def TermsOfCondition():
    st.write("As a user in ChatHub you agree that the system will collect information about your customers orders to enhance your trial and give you a better targeting for customer")
    if st.checkbox("Accept"):
        st.success("Success")
        time.sleep(2)
        st.switch_page(login)

# خلي الباسوورد 8 حروف علي الاقل وفيه char كابيتاب وسمول وارقام وسبيشيال كاراكتار
addresses = ["@gmail.com", "@yahoo.com"]

url = "http://127.0.0.1:5000/signup"
log = False
# st.write("---")
login = st.Page(r"login.py", title="Login", icon=":material/login:")
# from app3 import log

col1, col2, col3 = st.columns([4,1,4])
with col1:
    st.write("  \n");st.write("  \n")
    st.write("  \n");st.write("  \n")
    st.write("  \n");st.write("  \n")
    st.write("  \n");st.write("  \n")
    st.write("  \n");st.write("  \n")
    st.image(r"images/Sign up.gif")
with col2:
    pass
with col3:
    st.title("Sign up")
    fname = st.text_input(label="First Name", max_chars=20)
    lname = st.text_input(label="Last Name", max_chars=40)
    date = st.date_input(label="Birth Date",  min_value=datetime.date(1950,1,1))
    email = st.text_input(label="Email", max_chars=50)
    password = st.text_input(label="Password", max_chars=20, type='password')
    password2 = st.text_input(label="Reenter password", max_chars=20, type='password')
    if password==password2 and password is not "":
        log = True
    bt = st.button("Sign up", use_container_width=1)
    if bt:
        if password is "":
            st.error("Enter your data!")
        if log==True:
            TermsOfCondition()

            # body = jsonify({"fname":fname,"lname":lname,"date":date,"email":email,"password":password})
            # response = requests.post(url, json=body)
            # if response.json()['message'] =="success":
            #     TermsOfCondition()
            # else:
            #     st.error(response.json()['message'])
        elif password is not "":
            st.error("Error: Password not matched!")
    st.write("  \n")
    col11, col22 = st.columns([3,1])
    with col11:
        st.write("have an account?")
    with col22:
        login = st.Page(r"login.py", title="Login", icon=":material/login:")
        bt = st.button("Login")
        if bt:
            st.switch_page(login)
st.write("---")

