import streamlit as st
import os, json
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI()
MODEL = "gpt-4o-mini"

MIN_CHARS = 400

def generate_questions_from_notes(notes: str, n: int = 10):
    system = (
        "You write difficult multiple-choice questions for studying.\n"
        "Use ONLY the provided notes.\n"
        "Each question must test a common confusion or non-obvious detail.\n"
        "Avoid definition-only questions unless they include a subtle trap.\n"
        "Return JSON only matching the schema.\n"
        "Hints must be a nudge, not the answer.\n"
        "IMPORTANT: Each hint must be SPECIFIC to that question.\n"
        "Each hint must mention at least one keyword or symbol from the question stem.\n"
        "Do NOT reuse the same hint wording across questions.\n"
        "Make questions that test understanding, not plug-and-chug.\n"
        "At least 4/5 questions must be conceptual or scenario-based (reasoning about meaning, assumptions, edge cases, interpretations).\n"
        "At most 1/5 can be computation, but NOT straightforward.\n"
        "Every question must include a plausible misconception trap.\n"
        "Avoid questions solvable by applying a single formula with one step.\n"
        "If computation is used, it must require interpretation (e.g., choosing the right concept/assumption), not just arithmetic.\n"
        "Have “edge case / why this is false” style stems (like “Which statement is not always true?”) and require at least 2 scenario-based questions per 5.\n"
        "If notes are too short to support good questions, return need_more_notes=true."
    )

    user = f"""
NOTES:
{notes}

TASK:
Create {n} MCQs. Each must be answerable from the notes.

Return JSON in this exact format:
{{
  "need_more_notes": false,
  "message": "",
  "questions": [
    {{
      "text": "question stem",
      "choices": ["choice A", "choice B", "choice C", "choice D"],
      "correct": 0,
      "hint": "one hint that nudges but doesn't reveal the answer"
    }}
  ]
}}

Rules:
- 'correct' is an integer 0-3.
- Distractors should be plausible misconceptions.
- If notes are too short: set need_more_notes=true, put a message, and return questions=[].
"""

    resp = client.responses.create(
        model=MODEL,
        input=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        # Responses API uses text.format (NOT response_format)  [oai_citation:1‡OpenAI Platform](https://platform.openai.com/docs/api-reference/responses)
        text={"format": {"type": "json_object"}},
        temperature=0.4,
    )

    # Most recent SDKs give you resp.output_text
    data = json.loads(resp.output_text)
    return data

# --- session state ---
st.session_state.setdefault("show_quiz", False)
st.session_state.setdefault("questions", [])
st.session_state.setdefault("submitted", False)
st.session_state.setdefault("answers", {})

st.title("Study Quizzer")

hints_only_mode = st.toggle("Hints only mode (hide correctness + score)", value=False)

notes = st.text_area("Paste your notes here:")

if st.button("Generate quiz (10 questions)"):
    if notes.strip() == "":
        st.warning("Please paste some notes first.")
    elif len(notes.strip()) < MIN_CHARS:
        st.warning("Your notes look too short. Add more (definitions, formulas, examples).")
    else:
        st.session_state.submitted = False
        st.session_state.answers = {}

        out = generate_questions_from_notes(notes, 10)

        if out.get("need_more_notes", False):
            st.warning(out.get("message", "Need more notes to generate good questions."))
            st.session_state.show_quiz = False
            st.session_state.questions = []
        else:
            st.session_state.show_quiz = True
            st.session_state.questions = out["questions"]

if st.session_state.show_quiz:
    st.subheader("Quiz")

    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**{i+1}. {q['text']}**")
        choice = st.radio(
            label="Select one:",
            options=q["choices"],
            index=None,
            key=f"q_{i}",
        )
        st.session_state.answers[i] = choice
        st.divider()

    if st.button("Submit quiz"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        score = 0
        for i, q in enumerate(st.session_state.questions):
            chosen = st.session_state.answers.get(i)
            correct_choice = q["choices"][q["correct"]]

            is_correct = (chosen == correct_choice)
            if is_correct:
                score += 1

            # show hints ONLY when incorrect/unanswered (your preference)
            if not is_correct:
                st.info(f"Q{i+1} hint: {q['hint']}")

            # in normal mode, also show correctness feedback
            if not hints_only_mode:
                if is_correct:
                    st.success(f"Q{i+1}: Correct")
                else:
                    st.error(f"Q{i+1}: Incorrect")

        if not hints_only_mode:
            st.markdown(f"### Score: {score}/{len(st.session_state.questions)}")