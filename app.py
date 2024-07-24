import streamlit as st

# [theme]
# base="light"
# primaryColor="#4b84ff"

st.logo("images/logo.png")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def logoutt():
    st.session_state.logged_in = False
    st.rerun()

login = st.Page("login.py", title="Login", icon=":material/login:")
signup = st.Page(r"signup.py", title="Signup", icon=":material/assignment:")
intro = st.Page("intro.py", title="Home", icon=":material/home:")

home = st.Page("home.py", title="Home", icon=":material/home:", default=True)
profile = st.Page("profile.py", title="Profile", icon=":material/person:")
edit = st.Page(r"edit.py", title="Edit", icon=":material/edit:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
bot1 = st.Page("bot1.py", title="Chatbot 1", icon=":material/smart_toy:")
bot2 = st.Page("bot2.py", title="Chatbot 2", icon=":material/smart_toy:")
bot3 = st.Page("bot3.py", title="Chatbot 3", icon=":material/smart_toy:")
logout = st.Page(logoutt, title="Logout", icon=":material/logout:")


pages2 = {
    "":[login, signup, intro]
}

pages = {
    "": [profile, home],
    "Chatbots":[bot1, bot2, bot3],
    "Settings": [settings, edit, logout]
}


if st.session_state.logged_in == True:
    pg = st.navigation(pages)
    # st.sidebar.write("---")
    pg.run()
else:
    pg2 = st.navigation(pages2)
    pg2.run()
