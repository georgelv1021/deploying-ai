import sys
from pathlib import Path

# Allows test file to import from assignment_chat/services
sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.semantic import (
    build_company_market_index,
    query_company_market_info,
)


def main():
    print("Testing Semantic Company Search...\n")

    print(build_company_market_index())
    print("-" * 60)

    questions = [
        "Which companies benefit from AI?",
        "Which companies are strong in semiconductors?",
        "Tell me about payment companies.",
        "Which companies are exposed to oil prices?",
        "Which companies are defensive consumer staples?",
    ]

    for question in questions:
        print(f"Question: {question}")
        print(query_company_market_info(question))
        print("-" * 60)


if __name__ == "__main__":
    main()