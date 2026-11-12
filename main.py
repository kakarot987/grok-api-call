import os

from dotenv import load_dotenv
from groq import Groq

MODEL = "llama-3.1-8b-instant"
PROMPT = "Explain what an API is in 2 sentences."


def get_api_key():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured")
    return api_key


def main():
    client = Groq(api_key=get_api_key())
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
