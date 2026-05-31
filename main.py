import streamlit as st
from langchain_groq import ChatGroq
import base64

st.set_page_config(
    page_title="AI Agent • LLaMA 3.1",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #f0f0f0;
    }

    .main-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        margin-bottom: 1.5rem;
    }

    h1 {
        text-align: center;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.2rem !important;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }

    /* ── FIX: Hide the empty label box above textarea ── */
    .stTextArea label {
        display: none !important;
    }

    /* ── FIX: Dark background + visible dark text ── */
    .stTextArea textarea {
        background: #1e1b3a !important;
        border: 1px solid rgba(167,139,250,0.4) !important;
        border-radius: 12px !important;
        color: #f1f5f9 !important;
        font-size: 1rem !important;
        padding: 0.8rem !important;
        resize: vertical !important;
        caret-color: #a78bfa !important;
    }
    .stTextArea textarea:focus {
        border-color: #a78bfa !important;
        box-shadow: 0 0 0 2px rgba(167,139,250,0.25) !important;
    }
    .stTextArea textarea::placeholder {
        color: #64748b !important;
    }

    /* ── FIX: Remove extra wrapper spacing from hidden label ── */
    .stTextArea > div:first-child {
        display: none !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 20px rgba(124,58,237,0.4) !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(124,58,237,0.55) !important;
    }

    .response-box {
        background: rgba(52, 211, 153, 0.08);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin-top: 1.2rem;
        color: #d1fae5;
        font-size: 1rem;
        line-height: 1.75;
        white-space: pre-wrap;
    }

    .badge {
        display: inline-block;
        background: rgba(167,139,250,0.15);
        border: 1px solid rgba(167,139,250,0.35);
        border-radius: 20px;
        padding: 3px 14px;
        font-size: 0.78rem;
        color: #c4b5fd;
        margin: 0 4px;
    }

    .stSpinner > div {
        border-top-color: #a78bfa !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤖 AI Agent</h1>", unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">'
    '<span class="badge">⚡ Groq</span>'
    '<span class="badge">🦙 LLaMA 3.1 8B</span>'
    '<span class="badge">🚀 Instant</span>'
    '</p>',
    unsafe_allow_html=True
)

_k = b"Z3NrX0RQT0lvZEpYSDdraUxjbkcyNXRUV0dkeWIzRllXWDF6akZlQmRsYWZ4MmlXUHlVOGdNdUs="
API_KEY = base64.b64decode(_k).decode()
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=API_KEY)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

user_input = st.text_area(
    "💬 Your Question",
    placeholder="Ask me anything Rakib Vai..",
    height=150,
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("✨ Generate Response", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if generate:
    if user_input.strip():
        with st.spinner("🔮 Thinking..."):
            try:
                response = llm.invoke(user_input)
                st.markdown(
                    f'<div class="response-box">🧠  {response.content}</div>',
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a question before generating a response.")
