# Freelance Hunter Bot

Telegram bot that scrapes remote job listings and sends them directly to users with simple actions like save, skip, and unsave.

---

## Features

- Scrapes jobs from RemoteOK
- Filters jobs based on keywords
- Extracts job title, company, and description
- Save / Unsave jobs
- Skip jobs (hide permanently)
- SQLite database storage
- Inline buttons in Telegram
- Continuous background scraping

---

## Tech Stack

- Python
- Requests
- BeautifulSoup
- SQLite
- Telegram Bot API
- Threading

---

## Project Structure

freelance-hunter-bot/

bot/
- bot.py
- callback.py
- commands.py

core/
- runner.py

scrapers/
- remoteok.py

database/
- db.py

utils/
- matcher.py

launcher.py  
start.py  
requirements.txt  

---

## How to Run

Install dependencies:

pip install -r requirements.txt

---

Create .env file:

BOT_TOKEN=your_token

---

Run project:

python start.py

---

## How It Works

- Bot starts callback system
- Scraper fetches jobs every minute
- Jobs are filtered by keywords
- New jobs are sent to Telegram
- Users can save, skip, or unsave jobs

---

## Database

- jobs → all scraped jobs
- favorites → saved jobs
- skipped → ignored jobs
- users → bot users

---

## Deployment

Recommended: Render (Background Worker)

Start command:

python start.py

---

## Future Improvements

- AI job ranking
- Personal job feed per user
- Web dashboard
- Faster scraping system

---

## Author

Built by Mohammadali
