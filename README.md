# 📊 SmartMarket Monitor

**SmartMarket Monitor** is an AI-powered platform that scrapes, filters, and analyzes Indian stock market news. It personalizes news feeds based on the user's portfolio and offers sentiment insights using a local language model (LLM) via **Ollama**.

---

## 🚀 Features

### 📰 1. News Scraping Module
- Scrapes real-time stock market news from Indian sources like **Moneycontrol** and **Economic Times**.
- Displays the latest headlines in a **General News** section.

### 📂 2. Portfolio Linking Module
- Users can link their portfolios via broker APIs (e.g., **Zerodha Kite Connect sandbox**, **Groww sandbox**).
- Supports **manual stock symbol input** as a fallback (mock portfolio).

### 🧠 3. AI Analysis Module
- Integrates **Ollama** (local LLM) to analyze headlines.
- Classifies sentiment as:
  - ✅ Positive Impact
  - ⚠️ Neutral
  - ❌ Negative Impact
- If no portfolio is linked, generates a **general market sentiment** summary.
- Optionally includes **confidence scores** and **short reasoning**.

### 🔍 4. Filtered News Section
- Filters and displays only the news relevant to the user's portfolio.
- Helps users focus on impactful updates.

### 🔔 5. Notifications (Optional)
- Sends **push notifications** or **email alerts** for important news events or sentiment changes.

---

## 🛠️ Tech Stack

| Layer            | Technology                      |
|------------------|----------------------------------|
| Frontend         | React.js / Next.js              |
| Backend          | FastAPI (Python)                |
| Web Scraping     | BeautifulSoup, Requests         |
| AI Integration   | Ollama (on-device LLM)          |
| Notifications    | Push.js / SMTP (optional)       |
| Portfolio Input  | Manual or Broker APIs (mocked)  |

---
