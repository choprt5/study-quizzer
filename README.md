# Study Quizzer
Paste lecture notes → get a multiple-choice quiz with misconception-trap distractors and question-specific hints.
<<<<<<< HEAD
=======

>>>>>>> 232b9309d93049b83ed8e843ef6ae9d4396eb8b4
Built with Streamlit + OpenAI Responses API.

## Features
- Generate 10 MCQs from your notes (grounded to the text you paste)
- Hints shown only when you miss a question
<<<<<<< HEAD
- “Hints only mode” toggle (hide correctness + score)
- Basic grounding check (warns if notes are too short)
=======
- Optional “Hints only mode” toggle (will hide the score)
- Will warn if notes are too short
>>>>>>> 232b9309d93049b83ed8e843ef6ae9d4396eb8b4

## Tech Stack
- Python
- Streamlit
- OpenAI Python SDK (Responses API)

## Run locally

### 1) Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
<<<<<<< HEAD
pip install -r requirements.txt
=======
pip install -r requirements.txt
>>>>>>> 232b9309d93049b83ed8e843ef6ae9d4396eb8b4
