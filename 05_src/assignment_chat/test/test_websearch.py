import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.web_search import web_search_summary


def main():
    print("Testing Web Search Service...\n")

    questions = [
        "What are the latest trends in the semiconductor market?",
        "What is happening with AI stocks this week?",
    ]

    for question in questions:
        print(f"Question: {question}")
        print(web_search_summary(question))
        print("-" * 60)


if __name__ == "__main__":
    main()