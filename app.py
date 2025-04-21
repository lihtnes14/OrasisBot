import streamlit as st
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated
import os
from dotenv import load_dotenv

load_dotenv()

# Set API keys in the environment (or manually input if using secrets)

# Initialize LLM
llm = ChatGroq(
    model_name="gemma2-9b-it"
)

# Define State for LangGraph
class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# Node logic
def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

# Streamlit UI
st.set_page_config(page_title="OrasisBot", layout="centered")
st.title("💬 OrasisBot")

# Set light mode background color and text
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;  /* Light background color */
        color: #343a40;  /* Dark text for better readability */
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 32px;
        color: #343a40;
        padding-top: 20px;
        font-weight: bold;
    }
    .user-message {
        text-align: right;
        background: linear-gradient(135deg, #a2d2ff, #4c9dff);
        color: #ffffff;  /* White text color for better contrast */
        border-radius: 25px;
        padding: 10px 20px;
        max-width: 70%;
        margin: 5px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        opacity: 1;
        animation: fadeIn 0.5s forwards;
    }
    .assistant-message {
        text-align: left;
        background: linear-gradient(135deg, #f1f1f1, #d1d1d1);
        color: #343a40;  /* Dark text color for better contrast */
        border-radius: 25px;
        padding: 10px 20px;
        max-width: 70%;
        margin: 5px auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        opacity: 1;
        animation: fadeIn 0.5s forwards;
    }
    .stTextInput input {
        border-radius: 15px;
        padding-left: 20px;
        font-size: 16px;
        padding-right: 20px;
        margin-top: 10px;
    }
    .stButton button {
        background-color: #4c9dff;
        border-radius: 15px;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
    }
    @keyframes fadeIn {
        to {
            opacity: 1;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("Say something...", placeholder="Type your message here...")

# Function to handle input when "Enter" is pressed
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    
    # Display user message in chat window
    with st.container():
        st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

    # Stream LangGraph response
    full_response = ""
    with st.container():
        response_box = st.empty()
        for event in graph.stream({"messages": ("user", user_input)}):
            for value in event.values():
                if "messages" in value:
                    msg = value["messages"]
                    full_response = msg.content
                    response_box.markdown(f'<div class="assistant-message">{full_response}</div>', unsafe_allow_html=True)

    st.session_state.chat_history.append(("assistant", full_response))

# Display chat history with animation
for role, message in st.session_state.chat_history:
    with st.container():
        if role == "user":
            st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message}</div>', unsafe_allow_html=True)
