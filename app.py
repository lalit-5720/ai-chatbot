import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/chat"
SYSTEM_PROMPT = "You are a helpful assistant. Answer clearly and concisely."

st.set_page_config(page_title="Local AI Chatbot", page_icon="💬", layout="centered")
st.title("💬 Local AI Chatbot")
st.caption("A Streamlit chatbot powered by a model running locally with Ollama — no OpenAI API key required.")

with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Local model", ["llama3.2", "qwen2.5:3b"], index=0)
    
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    ollama_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    ollama_messages.extend(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Thinking locally..."):
            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={"model": model, "messages": ollama_messages, "stream": False},
                    timeout=300,
                )
                response.raise_for_status()
                answer = response.json()["message"]["content"]
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to Ollama. Make sure Ollama is installed and running. "
                    "In a terminal, run `ollama run llama3.2`, then try again."
                )
            except requests.exceptions.Timeout:
                st.error("The local model took too long to respond. Try again or use a smaller model.")
            except requests.exceptions.HTTPError as exc:
                st.error("Ollama returned an error. Check that the selected model is downloaded.")
                st.code(str(exc))
            except (KeyError, ValueError):
                st.error("Ollama returned an unexpected response. Please try again.")
