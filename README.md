# OrasisBot 🤖

**OrasisBot** is a quick and interactive AI-powered chatbot built using **LangChain**, **Groq LLM**, and **Streamlit**. It enables real-time, intelligent conversations through a sleek and engaging web interface.

## Features
- ⚡ Instant and intelligent responses powered by Groq.
- 🧠 LangGraph integration for contextual conversation flow.
- 🎨 Clean, animated chat interface built with HTML/CSS on top of Streamlit.
- 💬 Session-based chat history.
- 🔄 Option to start fresh by clearing chat history.

## Tech Stack
- **Streamlit:** UI framework for creating web apps in Python.
- **LangChain + Groq LLM:** Powers the language understanding and generation.
- **Python:** Backend logic and orchestration.
- **dotenv:** For secure environment variable handling.
- **HTML/CSS:** Used for custom frontend design.

## Getting Started

To run **OrasisBot** locally, follow these steps:

### Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/orasisbot.git
    cd orasisbot
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add Groq API key:
    ```bash
    touch .env
    ```

### Run the App

Launch the chatbot using:

```bash
streamlit run app.py
