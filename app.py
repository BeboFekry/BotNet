import streamlit as st

st.set_page_config(page_title="BotNet", page_icon='images/icon2.png', layout="wide")

st.logo("images/Picsart_24-08-15_01-45-01-740.png", size='large')

if "logged_in" not in st.session_state:
    st.session_state.logged_in = True

if "connected" not in st.session_state:
    st.session_state.connected = []

if "questions" not in st.session_state:
    st.session_state.questions = []

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
reports = st.Page("reports.py", title="Reports", icon=":material/view_list:")

# facebook = st.Page("facebook.py", title="Facebook Connect", icon=":material/share:")
# instagram = st.Page("instagram.py", title="Instagram Connect", icon=":material/share:")
# whatsapp = st.Page("whatsapp.py", title="Whatsapp Connect", icon=":material/share:")
# telegram = st.Page("telegram.py", title="Telegram Connect", icon=":material/share:")
connections = st.Page("connected.py", title="Connected pages", icon=":material/link:")
dashboard = st.Page("dashboard.py", title="Dashboard", icon=":material/insert_chart:")

pages2 = {
    "":[login, signup, intro]
}

pages = {
    "": [profile, home],
    "AI Agents": [bot1, bot2, bot3],
    "Social Media": [connections, dashboard],
    "Settings": [reports, settings, edit, logout]
}

# st.login(None)

if st.session_state.logged_in == True:
    pg = st.navigation(pages)
    # st.sidebar.write("---")
    # pg = st.navigation(pages+pagess)
    pg.run()
else:
    pg2 = st.navigation(pages2)
    pg2.run()
