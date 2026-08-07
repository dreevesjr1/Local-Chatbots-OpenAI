import os
import json
import uuid
import streamlit as st
from openai import OpenAI

CHAT_FILE = "chats.json"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_saved_chats():
    if not os.path.exists(CHAT_FILE):
        return {}

    with open(CHAT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_chats(chats):
    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        json.dump(chats, file, indent=4)


def create_new_chat():
    chat_id = str(uuid.uuid4())

    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": []
    }

    st.session_state.current_chat_id = chat_id
    save_chats(st.session_state.chats)


st.set_page_config(
    page_title="Chat Version 2.0",
    page_icon="💬",
    layout="wide"
)

if "chats" not in st.session_state:
    st.session_state.chats = load_saved_chats()

if "current_chat_id" not in st.session_state:
    if st.session_state.chats:
        st.session_state.current_chat_id = next(
            iter(st.session_state.chats)
        )
    else:
        create_new_chat()


# ---------------------------
# SIDEBAR
# ---------------------------

with st.sidebar:
    st.title("Chats")

    if st.button("➕ New Chat", use_container_width=True):
        create_new_chat()
        st.rerun()

    st.divider()

    for chat_id, chat in st.session_state.chats.items():

        if st.button(
            chat["title"],
            key=f"chat_{chat_id}",
            use_container_width=True
        ):
            st.session_state.current_chat_id = chat_id
            st.rerun()


# ---------------------------
# CURRENT CHAT
# ---------------------------

current_chat_id = st.session_state.current_chat_id

current_chat = st.session_state.chats[current_chat_id]

messages = current_chat["messages"]

st.title("Chat Version 2.0")


# Display previous messages

for message in messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# ---------------------------
# CHAT INPUT
# ---------------------------

prompt = st.chat_input("Ask me something...")


if prompt:

    messages.append({
        "role": "user",
        "content": prompt
    })

    # Use the first message as the chat title
    if current_chat["title"] == "New Chat":
        current_chat["title"] = prompt[:30]

    with st.chat_message("user"):
        st.write(prompt)


    response = client.responses.create(
        model="gpt-5-mini",
        input=messages
    )


    answer = response.output_text


    messages.append({
        "role": "assistant",
        "content": answer
    })


    with st.chat_message("assistant"):
        st.write(answer)


    save_chats(st.session_state.chats)

    st.rerun()