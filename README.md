# COVIS AI Copilot — POC

A voice-driven AI Copilot for an event management company (Saudi client). The Copilot answers natural-language questions about team availability, tasks, events, proposals, equipment, pipeline, and client KPIs.

Built as a proof of concept for a real-time client project.

---

## What It Does

The Copilot is a conversational voice assistant that:

- Listens to the user's spoken question (Web Speech API)
- Understands the intent using a large language model (Groq)
- Reasons over live mock PMS data (team, tasks, events, proposals, inventory, KPIs)
- Responds with a short, natural spoken answer (Speech Synthesis)

The UI shows an animated orb that reflects the AI's state:
- Blue — idle
- Red — listening
- Orange — thinking
- Gold — speaking

---

## Features

- Voice chat — hands-free mode with automatic mic restart
- Typed input — fallback when voice isn't available
- Mock PMS data — team, tasks, leaves, meetings, leads, proposals, events, equipment, pipeline, client KPIs
- Lead summary — bonus feature for this-week leads
- Pre-computed answers — date ranges and team availability are pre-computed in Python to keep the LLM reliable
- Deployed on Railway — live demo URL available

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python 3.13) |
| LLM | Groq API (openai/gpt-oss-120b) |
| Voice Input | Web Speech API (browser-native) |
| Voice Output | Web Speech Synthesis API (browser-native) |
| Frontend | Plain HTML + CSS |
| Deployment | Railway |

---

## Project Structure

event_copilot/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app + routes
│   ├── llm.py            # Groq integration + system prompt
│   ├── mock_data.py      # Mock PMS data + context builder
│   ├── templates/
│   │   └── index.html    # Chat UI + voice logic
│   └── static/
│       └── style.css     # Orb animation + layout
├── .env                  # GROQ_API_KEY (not committed)
├── .gitignore
├── Procfile              # Railway startup command
├── requirements.txt
└── README.md

---

## How It Works

1. User speaks or types a question — e.g., "What proposals are in review?"
2. Frontend sends the text to /chat (FastAPI)
3. Backend builds context — build_context() flattens all PMS data into a plain-text block
4. LLM receives the system prompt + context + user question via Groq API
5. LLM returns a short, voice-friendly answer
6. Frontend displays the response in the chat and speaks it aloud

---

## Setup Instructions

### Prerequisites

- Python 3.11+
- A Groq API key (free at https://console.groq.com/keys)
- Chrome or Edge (for voice input)

### 1. Clone the repository

git clone https://github.com/Huda-ImranSiddique/covis-copilot.git
cd covis-copilot

### 2. Create a virtual environment

Windows (PowerShell):
python -m venv venv
.\venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

python -m pip install -r requirements.txt

### 4. Create a .env file

In the project root, create a file named .env with:

GROQ_API_KEY=your_actual_key_here

Replace with your actual Groq API key.

### 5. Run the app

uvicorn app.main:app --reload

### 6. Open in Chrome or Edge

http://127.0.0.1:8000

Allow microphone access when prompted.

---

## Environment Variables

| Variable | Purpose |
|---|---|
| GROQ_API_KEY | API key for Groq LLM (required) |

The key must be set in .env locally, or in the Railway Variables tab in production.

---

## Business Logic Assumptions

Since the POC uses mock data and provides a general-purpose voice assistant, the following assumptions were made:

1. Data source is mocked.
   All PMS data (team, tasks, events, proposals, equipment, pipeline, KPIs) is stored in mock_data.py. In production, these would come from real APIs or a database.

2. "Next week" = next 7 days.
   Date ranges are pre-computed in Python (TODAY, NEXT_WEEK, NEXT_MONTH) and injected into the context so the LLM doesn't have to do date math.

3. Team availability is pre-computed.
   "Who is free" and "Who is busy" answers are pre-computed from hours_planned_today so the LLM never has to infer the raw numbers.

4. Skills-to-people mapping.
   The system prompt contains explicit mappings like "catering → Khalid Al-Otaibi", "venue → Noura Al-Saud". This ensures the LLM recommends the right person even when the user's phrasing is vague.

5. Voice input may mispronounce names.
   The prompt instructs the LLM to match names phonetically (e.g., "Abdullah Habibi" ≈ "Abdullah Al-Harbi").

6. Responses must be short.
   Since answers are read aloud, the LLM is instructed to keep replies to 1–2 sentences, no bullet points, no markdown. This is enforced with max_tokens=400 and a low temperature (0.3).

7. Currency is SAR.
   All monetary values in the mock data are in Saudi Riyals.

8. Out of scope for this POC:
   - Task assignment
   - Email sending
   - Authentication
   - Multi-tenant support
   - Real PMS integration

   These can be added in Phase 2.

---

## How to Test

Once the app is running:

1. Typed test: Type "What proposals are in review?" in the input box → Send
2. Voice test: Click the mic → say "Who is busy today?" → wait 2 seconds
3. Hands-free: Check the "Hands-free" box → mic auto-restarts after each answer
4. Orb states: Watch the orb change color as you interact

### Example queries to try

| Query | Expected Answer |
|---|---|
| What is my team plan today? | 42 members, 175 tasks, 268 hours. |
| Who is free today? | Faisal Al-Qahtani and Abdullah Al-Harbi. |
| Who is busy today? | Noura Al-Saud, Turki Al-Shammari, Bandar Al-Otaibi. |
| Who can handle the wedding catering? | Khalid Al-Otaibi. |
| What events are in Riyadh next week? | Riyadh Expo 2026 on September 27. |
| What proposals are in review? | Al-Rashed gala, Saudi Tech Summit, Jeddah Municipality. |
| What is our win ratio? | 40%, above the 30% target. |
| What is the LTV for Al-Rashed Group? | 1.25 million SAR. |
| Do we have 40 sqm of P2.5 LED screens? | Yes, 55 sqm available. |

---

## Deployment

The app is deployed on Railway:

Live URL: https://web-production-f75fe.up.railway.app

### Deploying your own copy

1. Push the repo to GitHub
2. Go to https://railway.app → sign in with GitHub
3. New Project → Deploy from GitHub repo → select this repo
4. Add environment variable: GROQ_API_KEY = your key
5. Generate a public domain

Railway picks up the Procfile automatically for the start command.

---

## Known Limitations

- Voice input requires Chrome or Edge. Firefox and Safari have partial support.
- Groq free tier = 30 requests/minute. Rapid-fire queries may hit rate limits.
- Free-tier Railway services sleep when idle. First request may be slow.
- Mock data only — no real PMS integration yet.

---

## Author

Built as a POC for an internship task.