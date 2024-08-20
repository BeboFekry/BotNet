import streamlit as st

# st.set_page_config(layout='wide')

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/background.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.columns([1,2,1])[1].image("images/Picsart_24-08-15_01-45-01-740.png")
st.info("Easy Build **Chatbots** for your business")
st.write("  \n")

st.title("Innovation Hub")
st.columns([1,2,1])[1].image("images/Chat bot.gif")
st.write("  \n")
st.write("  \n")

st.toast("Rotate your mobile screen", icon=":material/sync:")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Deconstructed robot-pana.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info("دلوقـتي تـقـدر تكـوِّن الشات بوت بتاعـك بنـفسـك بكـل سـهـولـة")
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Contact us-pana.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info("تـقـدر تودع خدمة العملاء وتوفـر مرتـبات ووقـت ومجهود كتـير")
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Chat bot-pana.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info(" :rocket: الشات بوت هيوفرلك وقت كتير في الرد علي العملاء بسرعة الصاروخ")
with tab4:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Visionary technology-amico.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info("جـه وقت انـك ترقي البـيزنـس الخاص بـيك لمستـوي احتـرافـي")
with tab5:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Cool robot.gif")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info("!مسـتـنـي ايه لحـد دلوقـتـي جـرب بنـفسـك وشـوف الفـرق")
st.write("---")
# if st.button("Continue"):
#     st.session_state.tab = tab5
#     # (tab3)
# st.session_state
st.header("Social Media Variety")
st.info("تـقـدر تربـطـه علي كـل منـصات التواصل الاجـتماعي")
st.columns([1,2,1])[1].image("images/Mobile Marketing.gif")
st.write("---")

st.header("Global Access")
st.info("تـقـدر تـعـدل وتـضـيـف اسـألـة في اي وقـت وفي كـل مـكـان")
st.columns([1,3,1])[1].image("images/Online world-amico.png")
st.write("---")

st.header("ChatBot Types")
st.columns([3,3,4])[2].info("متـاح اكـثـر من نـوع حـسـب احتـياجاتـك")

bot1 = st.Page("bot1.py", title="Chatbot 1", icon=":material/smart_toy:")
bot2 = st.Page("bot2.py", title="Chatbot 2", icon=":material/smart_toy:")
bot3 = st.Page("bot3.py", title="Chatbot 3", icon=":material/smart_toy:")

col0, col1, col2, col3, col5 = st.columns([1,2,2,2,1])
# row = st.columns()
with col1.container(border=True):
    st.image("images/Chat bot-pana.png")
    # st.columns([1,1,1])[1].write("**Type 1**")
    if st.button("Type 1", use_container_width=1):
        st.switch_page(bot1)
with col2.container(border=True):
    st.image("images/Chat bot-rafiki.png")
    # st.columns([1, 1, 1])[1].write("**Type 2**")
    if st.button("Type 2", use_container_width=1):
        st.switch_page(bot2)
with col3.container(border=True):
    st.image("images/Artificial intelligence-amico.png")
    # st.columns([1, 1, 1])[1].write("**Type 3**")
    if st.button("Type 3", use_container_width=1):
        st.switch_page(bot3)
st.write("---")
st.subheader("Chatbot Type 1")
col1, col2 = st.columns([1,2])
with col1:
    st.image("images/Chat bot-pana.png")
with col2:
    st.write("  \n"); st.write("  \n"); st.write("  \n"); st.write("  \n"); st.write("  \n")
    st.info("دة النوع الابسط والاكثر استخداما والاقل تكلفة مناسب جدا لشغل الصفحات زي الفيسبوك والماسنجر  \nوهنا بتقدر تحط الاسئلة الاكثر شيوعا والاجابات بتاعتها والعميل بيبقي قدامه اختيارات يختار السؤال وبتظهرله الاجابة وطبعا احنا هنساعدك في اختيار الاسئلة")
    if st.button("Chatbot Type 1", use_container_width=1):
        st.switch_page(bot1)
st.caption("---")
st.subheader("Chatbot Type 2")
col1, col2 = st.columns([1,2])
with col1:
    st.image("images/Chat bot-rafiki.png")
with col2:
    st.write("  \n");st.write("  \n");st.write("  \n")
    st.info("النوع الثاني ودة بيبقي اذكي باستخدام ادوات الذكاء الاصطناعي بيتم تدريبه علي البيانات الخاصة بيك وبيقدر ياخد كلام العميل ويفهمه ويستنتج هو بيسأل عن ايه وبيجاوبه باجابات بنحددها ليه")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.image("images/font (1).gif")
    with col2:
        st.image("images/fast-forward.gif")
    with col3:
        st.image("images/management.gif")
    with col4:
        st.image("images/fast-forward.gif")
    with col5:
        st.image("images/chatbot.gif")
    with col6:
        # pass
        st.image("images/analytics.gif")
    if st.button("Chatbot Type 2", use_container_width=1):
        st.switch_page(bot2)
st.caption("---")
st.subheader("Chatbot Type 3")
col1, col2 = st.columns([1,2])
with col1:
    st.image("images/Artificial intelligence.gif")
with col2:
    st.write("  \n");st.write("  \n");st.write("  \n")
    st.info("النوع الثالث ودة الاذكي ويعتبر اكثر نوع يشبه الانسان باستخدام الذكاء الاصطناعي التوليدي بنجيب شات جي بي تي ونعيد تدريبه علي بياناتك عشان يكون مناسب اكثر للمهمة المحددة ليه ودة بيقدر يتكلم ويجري حوار مع العميل زي الانسان")
    st.columns([1,1,1,2,1,1,1])[3].image("images/artificial-intelligence.gif")
    if st.button("Chatbot Type 3", use_container_width=1):
        st.switch_page(bot3)
st.write("---")

# FAQ
# st.header("FAQ")
st.columns([1,2,1])[1].image("images/Questions.gif")
col1, col2, col3, col4 = st.columns([1,2,2,1])
# with st.container(border=True):
st.columns([1,2,2,1])[2].info("يعني نختار ايه؟")
st.columns([1,2,2,1])[1].success("ببساطة لو شغلك عبارة عن صفحة علي الفيس بوك او الانستا وعايز رد آلي علي مجموعة من الاسئلة انت عارفهم بالفعل يبقي النوع الاول هو الانسب ليك")
st.columns([1,2,2,1])[2].info("طب وامتي اختار الحل الثاني؟")
st.columns([1,2,2,1])[1].success("لما يبقي عندك ")
st.columns([1,2,2,1])[2].info("طب لو ماعرفش العميل ممكن يسأل عن ايه وممكن يحتاج يسأل في تفاصيل كثير زي مساعدة في اختيار الطلب او شرح تفصيلي؟")
st.columns([1,2,2,1])[1].success("يبقي النوع الثالث انسب ليك")


st.write("---")

# st.info("خليك رقم 1 في السوق")
# st.columns([1,1,1])[1].image("images/number-one.gif")
# st.write("---")

st.info("احصل علي تقاريـر لنـشاطات شغلك مع اقـتراحات لاستهداف الفئة الافضل ليـك ولتطوير الية العمل الخاصة بـيك")
st.columns([1,3,1])[1].image("images/Data extraction-bro.png")
st.write("---")

st.info(" ChatHub زود مبيعاتك دلوقتي مع")
st.columns([1,1,1])[1].image("images/analytics.gif")
st.write("  \n"); st.write("  \n"); st.write("  \n")
# st.write("---")

# __________________________________________________________________________________________
# Footer
footer = st.container(border=True)
with footer:
    st.columns([3,1,3])[1].image("images/logo.png")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Services")
        st.caption("Web App")
        st.caption("Mobile App")
        st.write("Social")
        col11, col22, col33, col44, col5 = st.columns([1,1,1,1,5])
        with col11:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/702300.png)](http://www.linkedin.com/in/abdallah-fekry)")
        with col22:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/25231.png)](https://github.com/BeboFekry?tab=repositories)")
        with col33:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/4844503.png)](https://www.kaggle.com/bebofekry)")
        with col44:
            st.markdown("[![FB](https://raw.githubusercontent.com/BeboFekry/ChatHub/main/images/streamlit-mark-color.png)](https://abdalleh-fekry.streamlit.app/)")
    with col2:
        st.write("Contact")
        st.caption("Eng. Abdallah Fekry")
        st.caption("Egypt, Cairo")
        st.caption("+20 111 9499 384")
        st.caption("abdallahfekry95@gmail.com")
    with col3:
        st.write("About")
        st.caption("Smart Doctor")
        st.caption("Intelligent Comprehensive Medical System")
        st.caption("NLP + Computer Vision models that mimic a doctor")

    # st.caption("---")

col1, col2 = st.columns([1, 70])
with col2:
    st.caption("Copyright protected")
