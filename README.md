# Summoner's Oracle - AI League of Legends Coach

An interactive, web-based AI coach for League of Legends, powered by OpenAI's GPT. This application provides a chat interface where players can get personalized advice to improve their gameplay.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Configuration](#installation--configuration)
- [Usage](#usage)

## Features

- **AI-Powered Coaching**: Leverages `gpt-3.5-turbo` to provide insightful and conversational gameplay advice.
- **Interactive Persona**: The AI adopts the persona of the "Summoner's Oracle", a character from the League of Legends universe.
- **Personalized Guidance**: The Oracle will ask for your rank, role, and main champion to tailor its advice to your specific needs.
- **Web-Based Interface**: A simple and clean chat interface built with Flask.
- **Conversation History**: The chatbot remembers the context of your conversation for a more natural interaction.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pip (Python's package installer)
- An **OpenAI API Key**. You can get one from the OpenAI Platform.

## Installation & Configuration

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/SummonersOracle.git
    cd SummonersOracle
    ```

2.  **Install dependencies:**
    It's recommended to create a virtual environment first. Then, install the required Python packages.
    ```bash
    pip install Flask openai
    ```
    *(For a more robust setup, you can create a `requirements.txt` file.)*

3.  **Set up your API Key:**
    You need to provide your OpenAI API key to the application. The most secure way is to use an environment variable.

    **Windows (Command Prompt):**
    ```cmd
    set OPENAI_API_KEY="YOUR_API_KEY_HERE"
    ```

    **macOS/Linux:**
    ```bash
    export OPENAI_API_KEY="YOUR_API_KEY_HERE"
    ```
    You will also need to modify `app.py` to read this environment variable.

## Usage

1.  Run the Flask application:
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```
3.  Start chatting with the Summoner's Oracle!

