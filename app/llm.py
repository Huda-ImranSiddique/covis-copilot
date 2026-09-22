"""
Groq LLM integration.

This module handles all communication with the Groq API.
We use Llama 3.3 70B (free on Groq's free tier).
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


# This is the AI's "personality" — it tells the LLM:
# 1. What it is
# 2. What data it has access to
# 3. How to respond
SYSTEM_PROMPT = """You are COVIS, an AI Copilot for an event management company in Saudi Arabia.

You help the team by answering questions about:
- Team members and their availability
- Open tasks and who should handle them
- Employee leaves this week
- Client meetings and follow-ups
- Sales leads

You have access to live PMS (Project Management System) data, provided below.

Rules:
1. Always base your answers ONLY on the data provided below. Do not invent details.
2. Be concise and direct — like a helpful assistant, not a chatbot.
3. When recommending someone for a task, explain briefly why (skills, availability, workload).
4. If the data doesn't contain the answer, say so honestly.
5. Use PKR/SAR amounts and Arabic-friendly names naturally.
6. Keep responses short and conversational — this is a voice assistant, so no long bullet lists.

=== LIVE PMS DATA ===
{context}
=== END DATA ===
"""


def get_response(user_message: str, conversation_history: list = None) -> str:
    """
    Send a user message to Groq and get the AI's response.

    Args:
        user_message: what the user said
        conversation_history: optional list of previous messages for context

    Returns:
        The AI's response as a string.
    """
    system_content = SYSTEM_PROMPT.format(context=build_context())

    messages = [{"role": "system", "content": system_content}]

    # Add conversation history if provided (for multi-turn chat)
    if conversation_history:
        messages.extend(conversation_history)

    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.4,
            max_tokens=400,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry, I ran into an issue: {str(e)}"


def get_lead_summary() -> str:
    """
    Generate a concise lead summary — this is the 'nice to have' feature.
    Uses the same LLM but with a focused prompt.
    """
    system_content = SYSTEM_PROMPT.format(context=build_context())

    messages = [
        {"role": "system", "content": system_content},
        {
            "role": "user",
            "content": (
                "Give me a short summary of this week's priority leads and any "
                "client follow-ups coming up. Keep it to 3-4 sentences, voice-friendly."
            ),
        },
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.4,
            max_tokens=250,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry, I ran into an issue: {str(e)}"