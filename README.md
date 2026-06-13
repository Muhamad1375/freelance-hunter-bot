🚀 Freelance Hunter Bot

A Telegram bot that scrapes remote job listings and delivers them in real-time with smart filtering, saving, skipping, and unsaving features.

📌 Features
🔎 Scrapes jobs from RemoteOK
🧠 Keyword-based filtering
📝 Auto job description extraction (HTML scraping)
⭐ Save / Unsave jobs
❌ Skip jobs (won't show again)
💾 SQLite database storage
👥 Multi-user support (via Telegram chat_id)
🔁 Continuous background scraping
📲 Inline buttons (Telegram UI)
⚙️ Tech Stack
Python 3
Requests
BeautifulSoup4
SQLite3
Telegram Bot API
Threading
📂 Project Structure
freelance-hunter-bot/
│
├── bot/
│   ├── bot.py
│   ├── callback.py
│   └── commands.py
│
├── core/
│   └── runner.py
│
├── scrapers/
│   └── remoteok.py
│
├── database/
│   └── db.py
│
├── utils/
│   └── matcher.py
│
├── launcher.py
├── start.py
├── requirements.txt
└── README.md
🚀 How to Run Locally
1. Install dependencies
pip install -r requirements.txt
2. Set environment variables

Create .env file:

BOT_TOKEN=your_telegram_bot_token
3. Run project
python start.py
💡 How It Works
Bot starts callback listener
Scraper fetches jobs every minute
Jobs are filtered using keywords
New jobs are sent to Telegram users
Users can:
⭐ Save jobs
❌ Skip jobs
🗑 Unsave jobs
🧠 Database Tables
jobs → all scraped jobs
favorites → saved jobs
skipped → ignored jobs
users → registered users
📦 Deployment

Recommended: Render (Background Worker)

Start command:
python start.py
📈 Future Improvements
AI-based job ranking
Per-user personalization
Web dashboard
FastAPI backend version
Job notifications scheduling
👨‍💻 Author

Built by Mohammadali
