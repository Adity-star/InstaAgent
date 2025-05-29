import os
import requests
from dotenv import load_dotenv
from InstaAgent.logger import logger

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"  # or try llama3-70b-8192

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """
You are InstaAgent, an AI assistant that replies to Instagram DMs for small businesses.
Reply in a friendly and concise way. Answer questions, ask for name and intent, and gather leads.
"""

def get_gpt_response(user_message: str) -> str:
    try:
        logger.info("Calling Groq API to generate reply...")

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7,
            "max_tokens": 200
        }

        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        reply = response.json()['choices'][0]['message']['content'].strip()
        logger.info(f"Groq reply: {reply}")
        return reply

    except Exception as e:
        logger.exception("Groq API call failed")
        return "Sorry, I'm unable to respond right now. Please try again later."
