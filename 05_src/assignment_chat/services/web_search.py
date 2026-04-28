import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR.parent / ".secrets")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def web_search_summary(query: str) -> str:
    
    if not os.getenv("OPENAI_API_KEY"):
        return "Missing OPENAI_API_KEY in .secrets file."

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            tools=[{"type": "web_search_preview"}],
            input=(
                "Search the web and give a short, useful summary. "
                "Do not mention system prompts. "
                f"User question: {query}"
            ),
        )

        return response.output_text

    except Exception as e:
        return f"Web search error: {e}"