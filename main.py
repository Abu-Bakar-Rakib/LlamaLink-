import streamlit as st
from langchain_groq import ChatGroq


st.set_page_config(
    page_title="SwiftMind • LLaMA 3.1",
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
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.2rem !important;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
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
    .user-bubble {
        display: flex;
        justify-content: flex-end;
        margin: 0.6rem 0;
    }
    .user-bubble .bubble {
        background: linear-gradient(135deg, #7c3aed, #2563eb);
        color: #ffffff;
        border-radius: 18px 18px 4px 18px;
        padding: 0.75rem 1.1rem;
        max-width: 75%;
        font-size: 0.97rem;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(124,58,237,0.35);
    }
    .ai-bubble {
        display: flex;
        justify-content: flex-start;
        margin: 0.6rem 0;
    }
    .ai-bubble .avatar {
        font-size: 1.4rem;
        margin-right: 0.6rem;
        align-self: flex-end;
    }
    .ai-bubble .bubble {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(167,139,250,0.25);
        color: #e2e8f0;
        border-radius: 18px 18px 18px 4px;
        padding: 0.75rem 1.1rem;
        max-width: 75%;
        font-size: 0.97rem;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .thinking-bubble {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #94a3b8;
        font-size: 0.88rem;
        margin: 0.5rem 0 0.5rem 2.2rem;
    }
    .dot-flashing {
        display: inline-flex;
        gap: 4px;
    }
    .dot-flashing span {
        width: 6px; height: 6px;
        background: #a78bfa;
        border-radius: 50%;
        animation: blink 1.2s infinite;
    }
    .dot-flashing span:nth-child(2) { animation-delay: 0.2s; }
    .dot-flashing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes blink {
        0%, 80%, 100% { opacity: 0.2; transform: scale(0.9); }
        40% { opacity: 1; transform: scale(1.1); }
    }

    /* ── FIX: hide label box ── */
    .stTextArea label { display: none !important; }
    .stTextArea > div:first-child { display: none !important; }

    /* ── FIX: force dark background + white text on ALL states ── */
    .stTextArea textarea,
    .stTextArea textarea:focus,
    .stTextArea textarea:active,
    .stTextArea textarea:hover,
    div[data-baseweb="textarea"] textarea,
    div[data-baseweb="base-input"] textarea {
        background-color: #1a1535 !important;
        color: #f1f5f9 !important;
        -webkit-text-fill-color: #f1f5f9 !important;
        border: 1px solid rgba(167,139,250,0.4) !important;
        border-radius: 16px !important;
        font-size: 0.97rem !important;
        padding: 0.85rem 1rem !important;
        resize: none !important;
        caret-color: #a78bfa !important;
    }
    .stTextArea textarea::placeholder,
    div[data-baseweb="textarea"] textarea::placeholder {
        color: #64748b !important;
        -webkit-text-fill-color: #64748b !important;
    }
    div[data-baseweb="textarea"],
    div[data-baseweb="base-input"] {
        background-color: #1a1535 !important;
        border-radius: 16px !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.4rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        height: 100%;
        width: 100%;
        box-shadow: 0 4px 15px rgba(124,58,237,0.4) !important;
        transition: all 0.25s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(124,58,237,0.55) !important;
    }
    .clear-btn > button {
        background: rgba(255,255,255,0.05) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        font-size: 0.8rem !important;
        padding: 0.3rem 0.9rem !important;
        box-shadow: none !important;
    }
    .clear-btn > button:hover {
        background: rgba(255,255,255,0.1) !important;
        transform: none !important;
    }
    .chat-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.07);
        margin: 1rem 0;
    }
    .welcome-card {
        text-align: center;
        padding: 6rem 1rem 2rem;
        margin-top: -5rem;
        color: #475569;
    }
    .welcome-card .icon { font-size: 3rem; margin-bottom: 0.5rem; }
    .welcome-card p { font-size: 0.95rem; }
    #MainMenu, footer, header { visibility: hidden; }
    .stSpinner > div { border-top-color: #a78bfa !important; }
</style>
""", unsafe_allow_html=True)

_k = [103,115,107,95,66,53,102,53,101,115,76,69,69,53,66,86,73,117,79,120,112,90,90,53,87,71,100,121,98,51,70,89,106,121,49,53,119,49,106,84,109,86,100,54,97,106,88,87,67,114,49,77,55,104,78,76]
API_KEY = ''.join(chr(c) for c in _k)
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("<h1>🤖 SwiftMind </h1>", unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">'
    '<span class="badge">⚡ Groq</span>'
    '<span class="badge">🦙 LLaMA 3.1 8B</span>'
    '<span class="badge">🚀 Instant</span>'
    '</p>',
    unsafe_allow_html=True
)

if st.session_state.messages:
    col_spacer, col_clear = st.columns([5, 1])
    with col_clear:
        st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
        if st.button("🗑 Clear"):
            st.session_state.messages = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="chat-divider">', unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown("""
        <div class="welcome-card">
            <div class="icon">💬</div>
            <p>Start a conversation below — ask me anything!</p>
        </div>
    """, unsafe_allow_html=True)
else:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
                <div class="user-bubble">
                    <div class="bubble">{msg["content"]}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="ai-bubble">
                    <div class="avatar">🤖</div>
                    <div class="bubble">{msg["content"]}</div>
                </div>
            """, unsafe_allow_html=True)

st.markdown('<hr class="chat-divider">', unsafe_allow_html=True)

col_input, col_btn = st.columns([5, 1])
with col_input:
    user_input = st.text_area(
        "Message",
        placeholder="Type your message here Rakib Vai...",
        height=68,
        key=f"input_{len(st.session_state.messages)}",
        label_visibility="collapsed"
    )
with col_btn:
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    send = st.button("➤", use_container_width=True)

if send:
    if user_input.strip():
        st.session_state.messages.append({"role": "user", "content": user_input.strip()})
        with st.spinner(""):
            st.markdown("""
                <div class="thinking-bubble">
                    <div class="dot-flashing">
                        <span></span><span></span><span></span>
                    </div>
                    Thinking...
                </div>
            """, unsafe_allow_html=True)
            try:
                history = [
                    ("human" if m["role"] == "user" else "assistant", m["content"])
                    for m in st.session_state.messages
                ]
                response = llm.invoke(history)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
            except Exception as e:
                st.session_state.messages.append({"role": "assistant", "content": f"❌ Error: {str(e)}"})
        st.rerun()
    else:
        st.warning("⚠️ Please type a message first.")
