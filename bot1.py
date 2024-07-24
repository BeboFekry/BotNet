import streamlit as st
import time

st.header("Chatbot 1")

tab1, tab2, tab3 = st.tabs(["Questions", "Manage Questions", "Test"])

if "questions" not in st.session_state:
    st.session_state.questions = []

def add_question():
    question = st.text_input("Question", placeholder="اكتب هنا السؤال", value="")
    answer = st.text_input("Answer", placeholder="اكتب هنا الاجابة")
    return question, answer

with tab1:
    st.subheader("Add Questions to your list")
    # del st.session_state.questions[-1]
    i = 1
    # del st.session_state.questions[-1]
    question, answer = add_question()
    if st.button("Add", use_container_width=1):
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
    st.write("---")
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
            st.success("success")

with tab2:
    st.subheader("Manage Question")
    if len(st.session_state.questions) == 0:
        st.info("No questions have found!")
    else:
        i = 1
        choices = []
        for r in st.session_state.questions:
            if r["question"] != "":
                choices.append(st.checkbox(f"**Question no. {i}:**  \nQ: {r['question']}  \nA: {r['answer']}"))
                i += 1
        if st.button("Remove"):
            if True not in choices:
                st.error("No chooses found!")
            else:
                i = 0
                for c in choices:
                    if c:
                        del st.session_state.questions[i]
                    i +=1
                st.success("Question Removed")
                time.sleep(1)
                st.rerun()
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
    st.columns([1,2,1])[1].image("images/Chat bot-pana.png")
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
