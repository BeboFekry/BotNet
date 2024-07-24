import streamlit as st
import datetime

fname = "Abdallah"
lname = "Fekry"
email = "abdallahfekry95@gmail.com"
password = "admin"
date = datetime.datetime(2000,5,25).date()

st.write("---")
col1, col2 = st.columns([1,6])
with col1:
    st.image(r"images\boy (1).png")
with col2:
    st.write("  \n")
    st.subheader(f"{fname} {lname}")
st.write("---")

edit = st.Page(r"edit.py", title="Edit", icon=":material/timeline:")
# bt = st.columns(7)[6].button("edit")
# st.columns(7)[6].page_link(edit, label="Edit")
bt = st.columns(7)[6].button("Edit Info")
if bt:
    st.switch_page(edit)
# if bt:
#     edit.run()
# history = st.Page(r"diseasesHistory.py", title="Diseases History", icon=":material/timeline:")

st.info(f"**First Name:** {fname}")
st.info(f"**Last Name:** {lname}")
st.info(f"**Email:** {email}")
st.info(f"**Birth Date:** {date}")
# st.info("**View History:** ")

# st.page_link(history, label="Reports")
# bt2 = st.button("Reports")
# if bt2:
#     st.switch_page(history)