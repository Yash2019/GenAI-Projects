import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

#page setup
st.set_page_config(
    page_title='Chatbot',
    page_icon='🤖',
    layout='centered'
)
st.title('Generative ChatBot')

#initialise Chat History
#session state = dictioary
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message['role']): #gives the role
        st.markdown(message['content']) #user query

#initialise the llm
llm = ChatGroq(
    model='llama-3.1-8b-instant',
    temperature=0
)

#input box
user_prompt=st.chat_input('Ask the chatbot')

#to display the user message at the top before answering
if user_prompt:
    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({'role': 'user', 'content': user_prompt})

    response = llm.invoke(
        input=[{'role': 'system', 'content': 'You are a helpful assistant'}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({'role': 'assistant', 'content': assistant_response})

    with st.chat_message('assistant'):
        st.markdown(assistant_response)