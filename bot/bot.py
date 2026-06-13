import requests
import hashlib
from config import BOT_TOKEN, CHAT_ID


def make_id(link):
    return hashlib.md5(link.encode()).hexdigest()


def send_job(job):

    job_id = make_id(job["link"])

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    desc = job.get("description", "No description available")
    desc = desc[:500] + "..." if len(desc) > 500 else desc

    text = f"""
🚀 {job['title']}
🏢 {job['company']}
📝 {desc}
"""

    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "👍 Save",
                    "callback_data": f"save|{job_id}"
                },
                {
                    "text": "❌ Skip",
                    "callback_data": f"skip|{job_id}"
                }
            ],
            [
                {
                    "text": "🔗 Open",
                    "url": job["link"]
                }
            ]
        ]
    }

    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text,
        "reply_markup": keyboard
    })

    print(response.text)