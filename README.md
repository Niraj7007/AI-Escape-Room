# AI-Powered Escape Room

An interactive escape-room game built using Python, Streamlit and Google's Gemini AI. Players explore a mysterious library, interact with objects, solve puzzles and attempt to escape using natural-language conversations.

## Project Overview

This project explores how Large Language Models (LLMs) can be integrated into interactive applications.

It contains two versions:

- **Version 1:** A conversational AI-powered escape room where Gemini acts as the Game Master.
- **Version 2:** An improved implementation with structured game state, Python action validators and AI-generated narration.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI Python SDK
- Python dictionaries and session state
- python-dotenv

## Project Structure

```text
AI-Escape-Room/
│
├── Version-1/
│   └── app.py
│
├── Version-2/
│   └── app.py
│
├── Architecture/
│   ├── version1_architecture.png
│   └── version2_architecture.png
│
├── Screenshots/
│
├── Test-Cases/
│   └── test_cases.md
│
├── Report/
│   └── project_report.md
│
├── .env.example
├── .gitignore
└── README.md
```

## Version 1

Version 1 provides a conversational escape-room experience.

Players can explore five interactive objects, solve three puzzles, collect a Brass Key, unlock a drawer, discover a Secret Note and escape through the exit door.

Gemini acts as the Game Master and understands natural-language player interactions.

## Version 2

Version 2 improves reliability through structured game-state management and dedicated Python action validators.

Python controls important game actions, inventory, puzzle completion and victory conditions. Gemini interprets player requests and provides natural-language narration.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Escape-Room
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install streamlit google-genai python-dotenv
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never upload your actual `.env` file or API key to GitHub.

## Run the Application

Run Version 1:

```bash
python -m streamlit run Version-1/app.py
```

Run Version 2:

```bash
python -m streamlit run Version-2/app.py
```

## Architecture Diagrams

The architecture diagrams for both versions are available in the `Architecture` folder.

## Screenshots

Screenshots demonstrating the application are available in the `Screenshots` folder.

## Testing

Test scenarios and results are documented in:

`Test-Cases/test_cases.md`

## Project Report

The project report is available in:

`Report/Project_Report`

## Learning Outcomes

This project demonstrates:

- Integrating Gemini AI into a Python application.
- Building interactive interfaces using Streamlit.
- Processing natural-language player requests.
- Managing structured application state.
- Validating actions using Python.
- Improving the reliability of LLM-powered applications.

## Security

API keys are stored in environment variables and should never be committed to the repository.

## Author

Student project - AI-Powered Escape Room.
