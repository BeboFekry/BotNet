import streamlit as st
import time
import pandas as pd

st.header("Chatbot 1")

tab1, tab2, tab3 = st.tabs(["Questions", "Manage Questions", "Test"])

if "questions" not in st.session_state:
    st.session_state.questions = []

def add_question():
    question = st.text_input("Question", placeholder="اكتب هنا السؤال")
    answer = st.text_input("Answer", placeholder="اكتب هنا الاجابة")
    return question, answer

with tab1:
    st.subheader("Add Questions to your list")
    with st.form("test form"):
        question = st.text_input("Question", placeholder="اكتب هنا السؤال")
        answer = st.text_input("Answer", placeholder="اكتب هنا الاجابة")
        submitted = st.form_submit_button("Submit")
        if submitted:
            i = 1
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
    st.columns([5,1])[0].subheader("Manage Question")
    if len(st.session_state.questions) == 0:
        st.info("No questions have found!")
    else:
        i = 1
        choices = []
        questions = []
        for r in st.session_state.questions:
            if r["question"] != "":
                questions.append({"Number":f"Q {i}", "Question":r['question'], "Answer":r['answer'], "Select":False})
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
            if True not in edited["Select"].values:
                st.error("No chooses found!")
            else:
                i = 0
                for c in edited["Select"].values:
                    if c:
                        del st.session_state.questions[i]
                    i +=1
                st.session_state.sure = False
                st.success("Question Removed Successfully")
                time.sleep(1)
                st.rerun()
        if update:
            if True not in edited["Select"].values:
                st.error("No chooses found!")
            else:
                edit = False
                i = 0
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
                            else:
                                st.error(f"Question **:{edited.values[c][1]}:** is already exist!")
                                time.sleep(2)
                                st.rerun()
                        if df.values[c][2] != edited.values[c][2]:
                            st.session_state.questions[c]['answer'] = edited.values[c][2]
                            edit = True
                    i +=1
                if edit ==True:
                    st.session_state.sure = False
                    st.success("Question Updated Successfully")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("No changes found!")
with tab3:
    st.columns([1,2,1])[1].image("images/Chat bot-pana.png")
