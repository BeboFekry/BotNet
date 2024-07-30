import streamlit as st
import time
import pandas as pd

st.header("Chatbot 1")

tab1, tab2, tab3 = st.tabs(["Questions", "Manage Questions", "Test"])

def add_question():
    question = st.text_input("Question", placeholder="اكتب هنا السؤال")
    answer = st.text_input("Answer", placeholder="اكتب هنا الاجابة")
    return question, answer

@st.dialog("Choose your social option to connect")
def social():
        # st.subheader("Choose a social to connect")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("images/Picsart_24-07-27_21-39-31-349.png")
            with col2:
                if st.button("Facebook"):
                    st.switch_page(facebook)
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("images/Picsart_24-07-27_21-40-50-295.png")
            with col2:
                if st.button("Instagram"):
                    st.switch_page(instagram)
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("images/Picsart_24-07-27_21-39-44-115.png")
            with col2:
                if st.button("WhatApp"):
                    st.switch_page(whatsapp)
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("images/Picsart_24-07-27_21-40-00-090.png")
            with col2:
                if st.button("Telegram"):
                    st.switch_page(telegram)

with tab1:
    st.subheader("Add Questions to your list")
    with st.form("test form"):
        question = st.text_input("Question", placeholder="اكتب هنا السؤال")
        answer = st.text_input("Answer", placeholder="اكتب هنا الاجابة")
        submitted = st.form_submit_button("Submit")
        # st.form("test form").clear
        if submitted:
            i = 1
            # del st.session_state.questions[-1]
            # question, answer, add = add_question2()
            # if st.button("Add", use_container_width=1):
            if question == "" or answer == "":
                st.error("Enter your data!")
            else:
                exist = False
                for i in st.session_state.questions:
                    if i['question'] == question:
                        st.error("Question already exist!")
                        exist = True
                        break
                if exist == False:
                    st.session_state.questions.append({"question": question, "answer": answer})
                    st.success("Success")
                    time.sleep(1)
                    st.rerun()
    # st.write("---")
    if len(st.session_state.questions) == 0:
        st.info("No questions found!")
    else:
        st.subheader("Test your bot")
        st.columns([1, 1, 1])[1].image("images/Chat bot-pana.png")
        l = []
        happened = 0
        for i in st.session_state.questions:
            l.append(st.button(i['question'], use_container_width=True))
            if True in l and happened == 0:
                for i in range(len(l)):
                    if l[i]:
                        st.info(f"{st.session_state.questions[i]['answer']}")
                        happened = 1
        st.write("---")
        if st.button("Finish", use_container_width=1):
            # st.success("success")
            facebook = st.Page("facebook.py")
            instagram = st.Page("instagram.py")
            whatsapp = st.Page("whatsapp.py")
            telegram = st.Page("telegram.py")
            if "questions" not in st.session_state or len(st.session_state.questions) == 0:
                st.info("No questions found!")
            else:
                social()



# st.subheader("Add Questions to your list")
    # # del st.session_state.questions[-1]
    # i = 1
    # # del st.session_state.questions[-1]
    # question, answer = add_question()
    # if st.button("Add", use_container_width=1):
    #     if question == "" or answer == "":
    #         st.error("Enter your data!")
    #     else:
    #         exist = False
    #         for i in st.session_state.questions:
    #             if i['question'] == question:
    #                 st.error("Question already exist!")
    #                 exist = True
    #                 break
    #         if exist == False:
    #             st.session_state.questions.append({"question": question, "answer": answer})
    #             st.success("Success")
    #             time.sleep(1)
    #             st.rerun()
    # st.write("---")
    # if len(st.session_state.questions) == 0:
    #     st.info("No questions found!")
    # else:
    #     st.subheader("Test your bot")
    #     st.columns([1, 1, 1])[1].image("images/Chat bot-pana.png")
    #     l = []
    #     happened = 0
    #     for i in st.session_state.questions:
    #         l.append(st.button(i['question'], use_container_width=True))
    #         if True in l and happened == 0:
    #             for i in range(len(l)):
    #                 if l[i]:
    #                     st.info(f"{st.session_state.questions[i]['answer']}")
    #                     happened = 1
    #     st.write("---")
    #     if st.button("Finish", use_container_width=1):
    #         st.success("success")

with tab2:
    st.columns([5,1])[0].subheader("Manage Question")

    # @st.dialog("Are you sure?")
    # def ReAccept(process):
    #     st.write(f"Are you sure about that?  \nYou will **{process}** the selected question forever!")
    #     if st.checkbox("Yes I am Sure"):
    #         if st.button("Continue"):
    #             st.session_state.sure = True
                # st.rerun()
    # if "sure" not in st.session_state:
    #     st.session_state.sure = False
    # st.columns([1,2,1])[1].image("images/Chat bot-pana.png")
    if len(st.session_state.questions) == 0:
        st.info("No questions have found!")
    else:
        i = 1
        choices = []
        questions = []
        for r in st.session_state.questions:
            if r["question"] != "":
                # choices.append(st.checkbox(f"**test Question no. {i}:**  \nQ: {r['question']}  \nA: {r['answer']}"))
                questions.append({"Number": f"Q {i}", "Question": r['question'], "Answer": r['answer'], "Select": False})
                i += 1
        df = pd.DataFrame(questions)
        edited = pd.DataFrame(st.data_editor(df, hide_index=True, use_container_width=1, disabled=("Number",)))
        col1, col2, col3 = st.columns([1,1,5])
        with col1:
            remove = st.button("Remove")
        with col2:
            update = st.button("Update")
        with col3:
            reset = st.button("Reset Changes")
        if reset:
            st.rerun()
        if remove:
            # st.write(edited["Select"].values)
            if True not in edited["Select"].values:
                st.error("No chooses found!")
            else:
                i = 0
                for c in edited["Select"].values:
                    if c:
                        del st.session_state.questions[i]
                        i -= 1
                    i += 1
                st.session_state.sure = False
                st.success("Question Removed Successfully")
                time.sleep(1)
                st.rerun()
        if update:
            # st.write(edited["Select"].values)
            if True not in edited["Select"].values:
                st.error("No chooses found!")
            else:
                edit = False
                i = 0
                # st.write(edited.values)
                for c in range(len(edited.values)):
                    if edited.values[c][3]:
                        if edited.values[c][1] == "":
                            st.error(f"Question is empty!")
                            time.sleep(2)
                            st.rerun()
                        if df.values[c][1] != edited.values[c][1]:
                            if edited.values[c][1] not in df["Question"].values:
                                st.session_state.questions[c]['question'] = edited.values[c][1]
                                edit = True
                            # ReAccept("update")
                            # if st.session_state.sure:
                            #     st.session_state.questions[c]['question'] = edited.values[c][1]
                            #     edit = True
                            else:
                                st.error(f"Question **:{edited.values[c][1]}:** is already exist!")
                                time.sleep(2)
                                st.rerun()
                        if df.values[c][2] != edited.values[c][2]:
                            st.session_state.questions[c]['answer'] = edited.values[c][2]
                            edit = True
                            # ReAccept("update")
                            # if st.session_state.sure:
                            #     st.session_state.questions[c]['answer'] = edited.values[c][2]
                            #     edit = True
                        # del st.session_state.questions[i]
                    i +=1
                if edit ==True:
                    st.session_state.sure = False
                    st.success("Question Updated Successfully")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("No changes found!")
    # if st.button("Reset"):
    #     # st.ca.che_data(func=data_editor)
    #     st.success("Reset")
    #     st.rerun()
    # st.subheader("Manage Question")
    # if len(st.session_state.questions) == 0:
    #     st.info("No questions have found!")
    # else:
    #     i = 1
    #     choices = []
    #     for r in st.session_state.questions:
    #         if r["question"] != "":
    #             choices.append(st.checkbox(f"**Question no. {i}:**  \nQ: {r['question']}  \nA: {r['answer']}"))
    #             i += 1
    #     if st.button("Remove"):
    #         if True not in choices:
    #             st.error("No chooses found!")
    #         else:
    #             i = 0
    #             for c in choices:
    #                 if c:
    #                     del st.session_state.questions[i]
    #                 i +=1
    #             st.success("Question Removed")
    #             time.sleep(1)
    #             st.rerun()
        # Edit
        # if "yes" not in st.session_state:
        #     st.session_state.yes = False
        # q = a = ""
        # if st.button("Edit", use_container_width=1):
        #     if True not in choices:
        #         st.error("No choices found!")
        #     else:
        #         st.session_state.yes = True
        #         i, j = 0, 0
        #         for c in choices:
        #             if c:
        #                 q = st.session_state.questions[i]['question']
        #                 a = st.session_state.questions[i]['answer']
        #                 j = i
        #             i += 1
        # if st.session_state.yes == True:
        #     question = st.text_input(f"Edit Question", value=q)
        #     answer = st.text_input(f"Edit Answer", value=a)
        #     if st.button("Finish"):
        #         st.session_state.questions[j] = {"question": question, "answer": answer}
        #         st.success("Question Edited")
        #         st.session_state.yes == False
        #         time.sleep(1)
        #         st.rerun()

with tab3:
    # st.subheader("Manage Question")
    st.columns([1,2,1])[1].image("images/Chat bot-pana.png")

    # st.link_button("images/Picsart_24-07-27_21-39-31-349.png", "https://www.kaggle.com/bebofekry")



    # st.subheader("Add Questions to your list")
    # with st.form("test form"):
    #     question = st.text_input("Question", placeholder="اكتب هنا السؤال")
    #     answer = st.text_input("Answer", placeholder="اكتب هنا الاجابة")
    #     submitted = st.form_submit_button("Submit")
    #     # st.form("test form").clear
    #     if submitted:
    #         i = 1
    #         # del st.session_state.questions[-1]
    #         # question, answer, add = add_question2()
    #         # if st.button("Add", use_container_width=1):
    #         if question == "" or answer == "":
    #             st.error("Enter your data!")
    #         else:
    #             exist = False
    #             for i in st.session_state.questions:
    #                 if i['question'] == question:
    #                     st.error("Question already exist!")
    #                     exist = True
    #                     break
    #             if exist == False:
    #                 st.session_state.questions.append({"question": question, "answer": answer})
    #                 st.success("Success")
    #                 time.sleep(1)
    #                 st.rerun()
    # # st.write("---")
    # if len(st.session_state.questions) == 0:
    #     st.info("No questions found!")
    # else:
    #     st.subheader("Test your bot")
    #     st.columns([1, 1, 1])[1].image("images/Chat bot-pana.png")
    #     l = []
    #     happened = 0
    #     for i in st.session_state.questions:
    #         l.append(st.button(i['question'], use_container_width=True))
    #         if True in l and happened == 0:
    #             for i in range(len(l)):
    #                 if l[i]:
    #                     st.info(f"{st.session_state.questions[i]['answer']}")
    #                     happened = 1
    #     st.write("---")
    #     if st.button("Finish", use_container_width=1):
    #         st.success("success")

    # if len(st.session_state.questions) == 0:
    #     st.info("No questions have found!")
    # else:
    #     i = 1
    #     choices = []
    #     questions = []
    #     for r in st.session_state.questions:
    #         if r["question"] != "":
    #             # choices.append(st.checkbox(f"**test Question no. {i}:**  \nQ: {r['question']}  \nA: {r['answer']}"))
    #             questions.append({"Number":f"Q {i}", "Question":r['question'], "Answer":r['answer'], "Select":False})
    #             i += 1
    #     df = pd.DataFrame(questions)
    #     edited = pd.DataFrame(st.data_editor(df, hide_index=True))
    #     if st.button("Remove Question"):
    #         # st.write(edited["Select"].values)
    #         if True not in edited["Select"].values:
    #             st.error("No chooses found!")
    #         else:
    #             i = 0
    #             for c in edited["Select"].values:
    #                 if c:
    #                     del st.session_state.questions[i]
    #                 i +=1
    #             st.success("Question Removed")
    #             time.sleep(1)
    #             st.rerun()
    #     if st.button("Update Question"):
    #         # st.write(edited["Select"].values)
    #         if True not in edited["Select"].values:
    #             st.error("No chooses found!")
    #         else:
    #             edit = False
    #             i = 0
    #             # st.write(edited.values)
    #             for c in range(len(edited.values)):
    #                 if edited.values[c][3]:
    #                     if df.values[c][1] != edited.values[c][1]:
    #                         st.session_state.questions[c]['question'] = edited.values[c][1]
    #                         edit = True
    #                     elif df.values[c][2] != edited.values[c][2]:
    #                         st.session_state.questions[c]['answer'] = edited.values[c][2]
    #                         edit = True
    #                     # del st.session_state.questions[i]
    #                 i +=1
    #             if edit ==True:
    #                 st.success("Question Updates")
    #                 time.sleep(1)
    #                 st.rerun()
    #             else:
    #                 st.error("No change found!")
    # ______________________________________________________________________

    # st.subheader("Test your **bot**")
    # l = []
    # happened = 0
    # for i in st.session_state.questions:
    #     l.append(st.button(i['question'], use_container_width=True))
    #     if True in l and happened==0:
    #         for i in range(len(l)):
    #             if l[i]:
    #                 st.info(f"{st.session_state.questions[i]['answer']}")
    #                 happened = 1
    # for i in range(len(l)):
    #     if l[i]:
    #         st.info(f"{st.session_state.questions[i]['answer']}")
# if st.button("Add Quesion"):
#     add_question()