"""
Groq LLM integration.
Voice-friendly responses: short, natural, no bullets.
"""

import os
from dotenv import load_dotenv
from groq import Groq

from .mock_data import build_context

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Please add it to your .env file."
    )

client = Groq(api_key=GROQ_API_KEY)

MODEL = "openai/gpt-oss-120b"


SYSTEM_PROMPT = """You are COVIS, a voice AI Copilot for an event management company in Saudi Arabia.

You have live PMS data below. Use ONLY this data.

ABSOLUTE RULES — VOICE ASSISTANT:
- Your answers are SPOKEN ALOUD. Keep them to 1-2 short sentences maximum.
- NEVER write paragraphs. NEVER write more than 2 sentences.
- NO bullet points, NO markdown, NO lists, NO asterisks.
- Get straight to the answer. No preamble like "Sure" or "Let me check".
- If listing multiple items, name at most 3 — then stop.
- NEVER say "I don't have that information" if the data has a related answer.

EXAMPLES — copy this style:

Q: "What proposals are in review?"
A: "Three proposals: Al-Rashed gala at 450 thousand, Saudi Tech Summit at 180 thousand, and Jeddah Municipality at 620 thousand."

Q: "Who is free today?"
A: "Faisal Al-Qahtani and Abdullah Al-Harbi are fully free today."

Q: "Who is busy today?"
A: "Noura Al-Saud has six hours planned, Turki Al-Shammari five, and Bandar Al-Otaibi six."

Q: "What events are in Riyadh next week?"
A: "Riyadh Expo 2026 is on September 27 in Riyadh."

Q: "What is our win ratio?"
A: "Forty percent, ten points above the thirty percent target."

Q: "Who can handle the wedding catering?"
A: "Khalid Al-Otaibi. He handles catering and only has two hours booked today."

Team availability:
- "Who is free?" → read FREE TODAY list from pre-computed section.
- "Who is busy?" → read BUSY TODAY list.

Skills to people:
- catering → Khalid Al-Otaibi
- venue → Noura Al-Saud
- decor/stage → Sultan Al-Dosari
- AV/LED → Turki Al-Shammari
- guest/VIP → Reem Al-Mutairi
- planning/coordinating → Abdullah Al-Harbi or Faisal Al-Qahtani
- entertainment → Bandar Al-Otaibi
- logistics → Lama Al-Qahtani

Names may be mispronounced by speech-to-text. Match phonetically.

=== LIVE PMS DATA ===
{context}
=== END DATA ===
"""


def get_response(user_message: str, conversation_history: list = None) -> str:
    system_content = SYSTEM_PROMPT.format(context=build_context())

    messages = [{"role": "system", "content": system_content}]

    if conversation_history:
        messages.extend(conversation_history)

    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=400,
        )
        content = response.choices[0].message.content
        if not content or not content.strip():
            return "Could you rephrase that?"
        return content

    except Exception as e:
        return f"Sorry, I ran into an issue: {str(e)}"


def get_lead_summary() -> str:
    system_content = SYSTEM_PROMPT.format(context=build_context())

    messages = [
        {"role": "system", "content": system_content},
        {
            "role": "user",
            "content": (
                "In 2 short sentences, tell me this week's priority leads "
                "and any client follow-ups."
            ),
        },
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=400,
        )
        content = response.choices[0].message.content
        if not content or not content.strip():
            return "No lead updates right now."
        return content

    except Exception as e:
        return f"Sorry, I ran into an issue: {str(e)}"