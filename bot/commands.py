from database.db import get_favorites, get_job_by_id
from config import BOT_TOKEN, CHAT_ID
import requests

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_saved_jobs(chat_id):

    favorites = get_favorites()

    if not favorites:
        requests.post(BASE_URL + "/sendMessage", data={
            "chat_id": chat_id,
            "text": "⭐ No saved jobs yet."
        })
        return

    for job_id in favorites:

        job = get_job_by_id(job_id)

        if not job:
            continue

        title, link, source = job

        keyboard = {
            "inline_keyboard": [
                [
                    {
                        "text": "❌ Unsave",
                        "callback_data": f"unsave|{job_id}"
                    }
                ],
                [
                    {
                        "text": "🔗 Open",
                        "url": link
                    }
                ]
            ]
        }

        requests.post(BASE_URL + "/sendMessage", json={
            "chat_id": chat_id,
            "text": f"⭐ {title}",
            "reply_markup": keyboard
        })