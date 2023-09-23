import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    load_dotenv()
    # Load the OpenAI API KEY from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY not found")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(
        page_title='Private ChatGPT',
        page_icon="🤖",
    )



def main():
    init()
    
    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant."),           
        ]
    
    st.header("Private ChatGPT 🤖️")

    with st.sidebar:
        user_input = st.text_input("Type your message here:")
 
        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Waiting for response..."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))


    messages = st.session_state.messages if 'messages' in st.session_state else []
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i)+'_user')
        else:
            message(msg.content, is_user=False, key=str(i)+'_ai')


if __name__ == "__main__":
    main()