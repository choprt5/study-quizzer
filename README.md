# Study Quizzer
Paste lecture notes → get a multiple-choice quiz with misconception-trap distractors and question-specific hints.

Built with Streamlit + OpenAI Responses API.

## Features
- Generate 10 MCQs from your notes (grounded to the text you paste)
- Hints shown only when you miss a question
- Optional “Hints only mode” toggle (will hide the score)
- Will warn if notes are too short

## Tech Stack
- Python
- Streamlit
- OpenAI Python SDK (Responses API)

## Run locally

### 1) Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
