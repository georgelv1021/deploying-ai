import os
import json
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "company_market_profiles.jsonl"
CHROMA_PATH = BASE_DIR / "chroma_db"

COLLECTION_NAME = "company_market_profiles"

load_dotenv(BASE_DIR.parent / ".secrets")


def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY in .secrets file.")

    return api_key.strip()


def get_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))

    embedding_function = OpenAIEmbeddingFunction(
        api_key=get_openai_api_key(),
        model_name="text-embedding-3-small"
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    return collection


def load_company_documents():
    ids = []
    documents = []
    metadatas = []

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for line in file:
            item = json.loads(line)

            ids.append(item["id"])
            documents.append(item["text"])
            metadatas.append({
                "company": item["company"],
                "ticker": item["ticker"],
                "sector": item["sector"]
            })

    return ids, documents, metadatas


def build_company_market_index():
    collection = get_collection()

    if collection.count() > 0:
        return f"Semantic company index already exists with {collection.count()} documents."

    ids, documents, metadatas = load_company_documents()

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    return f"Semantic company index created with {len(ids)} company profiles."


def query_company_market_info(question: str, n_results: int = 3) -> str:
    collection = get_collection()

    if collection.count() == 0:
        build_company_market_index()

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    if not docs:
        return "I could not find relevant company information."

    output = []

    for meta, doc in zip(metas, docs):
        output.append(
            f"{meta['company']} ({meta['ticker']}) | Sector: {meta['sector']}\n{doc}"
        )

    return "\n\n".join(output)