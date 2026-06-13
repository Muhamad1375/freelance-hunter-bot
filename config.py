from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

KEYWORDS = [
    "python",
    "machine learning",
    "data science",
    "django",
    "flask",
    "ai"
]