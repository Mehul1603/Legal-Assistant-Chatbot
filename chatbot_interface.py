import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
import streamlit as st
import time
from vectordb import similsearch

# Streamlit UI setup
st.set_page_config(page_title="Legal Assistant Chatbot")

# Custom CSS styling
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #ffd0d0;
    }
    div.stButton > button:active {
        background-color: #ff6262;
    }
    div[data-testid="stStatusWidget"] div button {
        display: none;
    }
    .reportview-container {
        margin-top: -2em;
    }
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
    button[title="View fullscreen"] {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Reset conversation function
def reset_conversation():
    st.session_state.messages = []
    st.session_state.memory.clear()

# Initialize session state variables if they don't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=2, memory_key="chat_history", return_messages=True)

# Initialize the LLM 
groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(groq_api_key=groq_api_key,
               model_name="mixtral-8x7b-32768",
               temperature=0.5,
               max_tokens=1024)

# Define the LLM Prompt
prompt_template = """<s>[INST]This is a chat template and As a legal chat bot specializing in Indian Penal Code queries, your primary objective is to provide accurate and concise information based on the user's questions. Do not generate your own questions and answers. You will adhere strictly to the instructions provided, offering relevant context from the knowledge base while avoiding unnecessary details. Your responses will be brief, to the point, and in compliance with the established format. If a question falls outside the given context, you will refrain from utilizing the chat history and instead rely on your own knowledge base to generate an appropriate response. You will prioritize the user's query and refrain from posing additional questions. The aim is to deliver professional, precise, and contextually relevant information pertaining to the Indian Penal Code.
CONTEXT: {context}
CHAT HISTORY: {chat_history}
QUESTION: {question}
ANSWER:
</s>[INST]
"""

prompt = PromptTemplate(template=prompt_template,
                        input_variables=['context', 'question', 'chat_history'])


def get_response_from_llm(query):
    # Retrieve relevant documents from the similarity search
    retrieved_docs = similsearch(query, k=4)
    
    # Combine the retrieved documents into a context string
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    # Retrieve chat history
    chat_history = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages]
    )
    
    # Format the full prompt for the LLM
    full_prompt = prompt.format(context=context, question=query, chat_history=chat_history)
    
    # Format messages for ChatGroq
    messages = [
        ("system", "You are a legal assistant specializing in the Indian Penal Code."),
        ("human", full_prompt)
    ]
    
    # Invoke the LLM to get a response
    ai_msg = llm.invoke(messages)
    
    # Return the response text directly
    return ai_msg.content.strip()


# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))

# Handle user input
input_prompt = st.chat_input("Ask your legal question")

if input_prompt:
    # Display the user's input
    with st.chat_message("user"):
        st.write(input_prompt)

    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": input_prompt})

    # Display the chatbot's thinking status
    with st.chat_message("assistant"):
        with st.status("Thinking 💡...", expanded=True):
            # Get the response from the LLM using the custom retrieval process
            result = get_response_from_llm(input_prompt)

            message_placeholder = st.empty()

            # Display the response
            full_response = "⚠️ **_Note: Information provided may be inaccurate._** \n\n\n" + result
            message_placeholder.markdown(full_response)

        # Add a reset button to clear the conversation
        st.button('Reset All Chat 🗑️', on_click=reset_conversation)

    # Add the assistant's response to the session state
    st.session_state.messages.append({"role": "assistant", "content": result})
