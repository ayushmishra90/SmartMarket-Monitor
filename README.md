📈 SmartMarket Monitor
SmartMarket Monitor is an AI-enhanced stock market news analyzer that scrapes, filters, and interprets financial news from top Indian sources. It offers personalized insights based on user portfolios or general market sentiment using a local LLM like Ollama.

🚀 Features
📰 News Scraping Module
Automatically scrapes the latest stock market news from Indian sources like Moneycontrol, Economic Times Markets, etc.

Displays a continuous feed in the General News section.

📊 Portfolio Linking Module
Allows users to link their stock portfolios using broker APIs (Zerodha Kite Connect sandbox, Groww sandbox)

If APIs aren't available, supports manual mock input (user can input stock symbols like INFY, TCS, etc.)

🧠 AI Analysis Module
Uses Ollama (local LLM) to analyze filtered news

Classifies sentiment as:

✅ Positive Impact

⚠️ Neutral

❌ Negative Impact

If no portfolio is linked, provides a general market sentiment summary

🗂️ Filtered News Section
Filters and displays news relevant only to user-linked or input stocks

Continuously updates with the latest relevant articles

✉️ Bonus Features (Optional)
Adds confidence scores and short explanations for each AI-generated sentiment

Push notifications or email alerts for significant updates (via FastAPI background tasks or SMTP)

🛠️ Tech Stack
Layer	Technology
Frontend	React.js / Next.js
Backend	FastAPI (Python)
Web Scraping	BeautifulSoup, Requests
AI Analysis	Ollama (LLM)
Notifications	SMTP or Push.js
Optional DB	MongoDB / Firebase

🧪 How It Works
Scraper gathers news headlines and links from predefined financial websites.

Portfolio Manager links the user’s stock list (either via API or manual input).

News Filter selects only the headlines that match the user's stocks.

Sentiment Analyzer (Ollama) processes these headlines and returns:

Label (Positive / Neutral / Negative)

Confidence score (optional)

Brief reasoning

Display UI shows general and filtered news along with AI insights.

💻 Setup Instructions
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/ayushmishra90/SmartMarket-Monitor.git

# 2. Navigate to project folder
cd SmartMarket-Monitor

# 3. Start backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# 4. Start frontend
cd ../frontend
npm install
npm start
📦 Folder Structure (Example)
css
Copy
Edit
SmartMarket-Monitor/
├── backend/
│   ├── main.py
│   ├── scraper.py
│   └── ai_analysis.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── pages/
├── README.md
📌 Future Enhancements
Real-time broker API integration (Groww, Zerodha)

Multilingual sentiment analysis

Deployable version on Vercel / Render / Hugging Face Spaces
