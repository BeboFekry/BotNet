import streamlit as st
# st.columns([1,2,1])[1].image("images\logo.png")
# with st.columns(3)[1]:
#     st.title("I CARE")
st.columns([1,2,1])[1].image("images/logo.png")
st.info("Easy Build **Chatbots** for your business")
st.write("  \n")

st.title("Innovation Hub")
st.columns([1,4,1])[1].image("images/Chat bot.gif")
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
        st.info("دلوقتي تقدر تكوِّن الشات بوت بتاعك بنفسك بكل سهولة")
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Contact us-pana.png")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info("تقدر تودع خدمة العملاء وتوفر مرتبات ووقت ومجهود كتير")
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
        st.info("جه وقت انك ترقي البيزنس الخاص بيك لمستوي احترافي")
with tab5:
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/Cool robot.gif")
    with col2:
        st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n");st.write("  \n")
        st.info("!مستني ايه لحد دلوقتي جرب بنفسك وشوف الفرق")
st.write("---")

col1, col2 = st.columns([2,4])
with col1:
    st.image("images/Sign up-rafiki.png")
with col2:
    st.columns([1,1,1])[1].header("Sign up")
    st.info("Create account now and access all these features")
    signup = st.Page("signup.py")
    if st.button("Sign up", use_container_width=1):
        st.switch_page(signup)
st.write("---")

st.header("Social Media Variety")
st.info("تقدر تربطه علي كل منصات التواصل الاجتماعي")
st.columns([1,3,1])[1].image("images/Mobile Marketing-bro.png")
st.write("---")

st.header("Global Access")
st.info("تقدر تعدل وتضيف اسألة في اي وقت وفي كل مكان")
st.columns([1,3,1])[1].image("images/Online world-amico.png")
st.write("---")

st.header("ChatBot Types")
st.columns([3,3,4])[2].info("متاح كمان اكثر من نوع حسب احتياجاتك")

bot1 = st.Page("bot1.py", title="Chatbot 1", icon=":material/smart_toy:")
bot2 = st.Page("bot2.py", title="Chatbot 2", icon=":material/smart_toy:")
bot3 = st.Page("bot3.py", title="Chatbot 3", icon=":material/smart_toy:")

st.subheader("Type 1")
col1, col2 = st.columns([1,2])
with col1:
    st.image("images/Chat bot-pana.png")
with col2:
    st.write("  \n");st.write("  \n")
    st.info("دة النوع الابسط والاكثر استخداما والاقل تكلفة مناسب جدا لشغل الصفحات زي الفيسبوك والماسنجر  \nوهنا بتقدر تحط الاسئلة الاكثر شيوعا والاجابات بتاعتها والعميل بيبقي قدامه اختيارات يختار السؤال وبتظهرله الاجابة وطبعا احنا هنساعدك في اختيار الاسئلة")
    # if st.button("Type 1", use_container_width=1):
    #     st.switch_page(bot1)
st.caption("---")
st.subheader("Type 2")
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
    # if st.button("Type 2", use_container_width=1):
    #     st.switch_page(bot2)
st.caption("---")
st.subheader("Type 3")
col1, col2 = st.columns([1,2])
with col1:
    st.image("images/Artificial intelligence-amico.png")
with col2:
    st.write("  \n");st.write("  \n");st.write("  \n")
    st.info("النوع الثالث ودة الاذكي ويعتبر اكثر نوع يشبه الانسان باستخدام الذكاء الاصطناعي التوليدي بنجيب شات جي بي تي ونعيد تدريبه علي بياناتك عشان يكون مناسب اكثر للمهمة المحددة ليه ودة بيقدر يتكلم ويجري حوار مع العميل زي الانسان")
    st.columns([1,1,1,2,1,1,1])[3].image("images/artificial-intelligence.gif")
    # if st.button("Type 3", use_container_width=1):
    #     st.switch_page(bot3)
st.write("---")

# FAQ
st.header("FAQ")
st.columns([1,3,1])[1].image("images/Questions.gif")
st.columns([1,1])[1].info("يعني نختار ايه؟")
st.columns([1,1])[0].success("ببساطة لو شغلك عبارة عن صفحة علي الفيس بوك او الانستا وعايز رد آلي علي مجموعة من الاسئلة انت عارفهم بالفعل يبقي النوع الاول هو الانسب ليك")
st.columns([1,1])[1].info("طب وامتي اختار الحل الثاني؟")
st.columns([1,1])[0].success("لما يبقي عندك ")
st.columns([1,1])[1].info("طب لو ماعرفش العميل ممكن يسأل عن ايه وممكن يحتاج يسأل في تفاصيل كثير زي مساعدة في اختيار الطلب او شرح تفصيلي؟")
st.columns([1,1])[0].success("يبقي النوع الثالث انسب ليك")

st.write("---")

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
