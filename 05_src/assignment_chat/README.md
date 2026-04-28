# MARKETBRO CHATBOT

MarketBro Chatbot is a multi-purpose financial assistant that provides users with the latest stock market information, company insights, and market trends based on their needs. It is designed with a fun “finance bro” conversational style to make interactions more engaging and enjoyable.

---

# Services

## 1. MARKETSTACK API

I use the MarketStack API as the primary data source for live and recent stock market information. This API provides global market data and allows the chatbot to deliver accurate and timely stock updates to users.

Reference: [MARKETSTACK API DOCUMENTATION](https://docs.apilayer.com/marketstack/docs/api-documentation?utm_source=dashboard&utm_medium=Referral)

### Values Extracted from the API:
- **Open Price** – Opening price of the trading day  
- **Close Price** – Closing price of the trading day  
- **High Price** – Highest price of the day  
- **Low Price** – Lowest price of the day  
- **Volume** – Trading volume for the day  

This service is used when users ask for stock prices or ticker-related information.

---

## 2. SEMANTIC SEARCH

I created a custom dataset containing the top 20 companies, including:

- Company ticker symbols  
- Sector classification  
- Brief company descriptions  

I then used OpenAI’s embedding model to convert the dataset into vector embeddings. These embeddings are stored in a ChromaDB PersistentClient database for semantic retrieval.

This allows the chatbot to answer meaning-based questions such as:

- Which companies benefit from AI?  
- What are some strong semiconductor companies?  
- Which companies are defensive investments?  

Please see `semantic.py` for implementation details.

---

## 3. TOOL – WEB SEARCH

I implemented OpenAI Web Search as the third service to expand the chatbot’s capabilities beyond the local dataset.

This service helps users obtain:

- Latest stock market news  
- Industry trends  
- Recent financial developments  
- Current market events  

All web search responses are summarized into short, clear, and user-friendly answers.

---

# Guardrails

Specific guardrails are implemented in `main.py`.

They include:

1. Protection against revealing the system prompt or internal instructions  
2. Blocking attempts to modify system behavior through prompt injection  
3. Refusal to answer questions related to:
   - Cats  
   - Dogs  
   - Horoscopes  
   - Zodiac Signs  
   - Taylor Swift  
4. Maintaining friendly and appropriate responses

---

# User Interface

I used **Gradio** to build a simple and user-friendly chat interface.

The interface supports natural conversation and allows users to interact with all three services through one chatbot window.

---

# Personality / Theme

MarketBro Chatbot uses a casual and energetic finance-themed tone to make financial information more approachable and entertaining.
