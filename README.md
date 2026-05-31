# SwiftMind

A high-performance ChatGPT-style AI chat application built with Streamlit and LangChain, powered by LLaMA 3.1 8B on Groq infrastructure.

## Overview

SwiftMind delivers fast, intelligent responses by leveraging state-of-the-art language models through the Groq API. With minimal setup, users can interact with advanced AI capabilities without complex configurations.

## Features

- 🚀 **Fast Inference** - Powered by Groq's optimized hardware for rapid response times
- 🤖 **Multiple Models** - Support for LLaMA 3.1 8B, 70B, and Mixtral variants
- 💬 **Conversational Interface** - Built with Streamlit for an intuitive user experience
- 🔑 **User-Controlled API Keys** - Secure, user-provided Groq API keys for authentication

## Prerequisites

- Python 3.8 or higher
- A Groq API key ([Get one here](https://console.groq.com))

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Abu-Bakar-Rakib/AI_agent.git
cd AI_agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages manually:

```bash
pip install streamlit>=1.35.0 langchain-groq>=0.1.6 langchain-core>=0.2.0
```

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`. Enter your Groq API key when prompted.

## Requirements

| Package | Version |
|---------|---------|
| `streamlit` | ≥1.35.0 |
| `langchain-groq` | ≥0.1.6 |
| `langchain-core` | ≥0.2.0 |

## Project Structure

```
AI_agent/
├── app.py              # Main application entry point
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Available Models

Configure the model by editing the `model` parameter in `app.py`:

```python
llm = ChatGroq(model="llama-3.1-8b-instant", api_key=API_KEY)
```

| Model | Speed | Use Case |
|-------|-------|----------|
| `llama-3.1-8b-instant` | ⚡ Fastest | Quick responses, real-time interactions |
| `llama-3.1-70b-versatile` | ⚖️ Balanced | General-purpose tasks, nuanced responses |
| `mixtral-8x7b-32768` | 📚 High Quality | Complex reasoning, detailed outputs |

## Usage

1. Launch the application
2. Enter your Groq API key in the sidebar
3. Type your message in the chat input
4. Receive AI-powered responses instantly

## Technology Stack

- **[Streamlit](https://streamlit.io/)** - Interactive web framework
- **[LangChain](https://www.langchain.com/)** - LLM orchestration and integration
- **[Groq](https://groq.com/)** - High-performance inference engine
- **[LLaMA 3.1](https://www.llama.com/)** - Meta's advanced language model

## Deployment

The application is deployed and available at:
[SwiftMind on Streamlit Cloud](https://aiagent-dkmjkcy9632mbypgbppnbs.streamlit.app/)

## Getting Your Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up or log in
3. Create a new API key
4. Copy and paste it into the SwiftMind interface

## Troubleshooting

- **Invalid API Key**: Ensure your Groq API key is correct and active
- **Slow Responses**: Try switching to a faster model (e.g., llama-3.1-8b-instant)
- **Connection Issues**: Verify your internet connection and Groq service status

## License

This project is open source and available under the MIT License.

## Contact & Support

For issues, questions, or contributions, please open an issue on [GitHub](https://github.com/Abu-Bakar-Rakib/AI_agent/issues).

---

**SwiftMind** — Fast answers. Zero wait.
