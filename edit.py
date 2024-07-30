import time

import streamlit as st
import datetime

st.header("Edit")
# fname = "Abdallah"
# lname = "Fekry"
# email = "abdallahfekry95@gmail.com"
# password = "admin"
# date = datetime.date(2000,5,25)
#
# edit_basic = st.Page("edit_basic_info.py")
# edit_pass = st.Page("edit_password.py")
#
# st.header("Edit information")
# bt = st.button("Edit Basic Information", use_container_width=1)
# st.info(f"Name: {fname} {lname}")
# st.info(f"Email: {email}")
# st.info(f"Birthday: {date}")
# st.write("  \n");st.write("  \n")
# bt2 = st.button("Change Password", use_container_width=1)
# if bt:
#     st.switch_page(edit_basic)
# if bt2:
#     st.switch_page(edit_pass)
#
# st.write("---")

tab1, tab2, tab3 = st.tabs(["Basic Info","Email address", "Change Password"])

with tab1:
    fname = "Abdallah"
    lname = "Fekry"
    email = "abdallahfekry95@gmail.com"
    password = "admin"
    date = datetime.date(2000, 5, 25)

    fname2 = st.text_input(label="First Name", max_chars=20, value=fname)
    lname2 = st.text_input(label="Last Name", max_chars=40, value=lname)
    date2 = st.date_input(label="Birthdate", value=date, min_value=datetime.date(1950,1,1))
    password2 = st.text_input(label="Password", max_chars=20, type='password', placeholder="Password")

    log = False
    change = False

    if password == password2 and password is not "":
        log = True
    if fname2 != fname and fname2 is not "":
        fname = fname2
        change = True
    if lname2 != lname and lname2 is not "":
        lname = lname2
        change = True
    if date2 != date and date2 is not "":
        date = date2
        change = True

    bt = st.button("Finish")
    if bt:
        if change == False:
            st.error("No changes in data!")
        else:
            if password2 is "":
                st.error("Error: please enter your password!")
            else:
                if log == True and change == True:
                    st.success("Success")
                    # time.sleep(1)
                    # st.rerun()
                elif change == True:
                    st.error("Wrong password!")


with tab2:
    email = "abdallahfekry95@gmail.com"
    password = "admin"
    email2 = st.text_input(label="Email", max_chars=50, value=email)
    password2 = st.text_input(label="Password ", max_chars=20, type='password', placeholder="Password")

    log = False
    change = False

    if password == password2 and password is not "":
        log = True
    if email2 != email and email2 is not "":
        email = email2
        change = True

    bt = st.button(" Finish")
    if bt:
        if change == False:
            st.error("No changes in data!")
        else:
            if password2 is "":
                st.error("Please enter your password!")
            else:
                if log == True and change == True:
                    st.success("Success")
                elif change == True:
                    st.error("Wrong password!")

with tab3:
    oldpass = "admin"
    log = False

    oldpass2 = st.text_input(label="Old Password", max_chars=20, type='password', placeholder="Old Password")
    password = st.text_input(label="New Password", max_chars=20, type='password', placeholder="New Password")
    password2 = st.text_input(label="Reenter Password", max_chars=20, type='password', placeholder="Re-enter New Password")

    bt = st.button("Finish ")
    if bt:
        if oldpass2 is "":
            st.error("Error: enter your old password!")
        else:
            if password is "" or password2 is "":
                st.error("Error: enter your new password!")
            if oldpass != oldpass2 and oldpass2 is not "":
                st.error("Error: Wrong password!")
            else:
                if password == password2 and password2 is not "":
                    oldpass = password
                    st.success("Success")
                elif password is not "" and password2 is not "":
                    st.error("Password not matched!")