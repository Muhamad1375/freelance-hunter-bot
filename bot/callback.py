import requests
from config import BOT_TOKEN
from database.db import save_favorite, save_skipped, remove_favorite
from bot.commands import send_saved_jobs

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def get_updates(offset=None):

    res = requests.get(
        BASE_URL + "/getUpdates",
        params={"timeout": 10, "offset": offset}
    )

    return res.json()


def handle_callback(update):

    print("🔥 CALLBACK RECEIVED:")
    print(update)

    callback = update["callback_query"]
    msg_data = callback["data"]

    print("📩 RAW DATA:", msg_data)

    action, job_id = msg_data.split("|")

    if action == "save":
        save_favorite(job_id)
        print("SAVE JOB:", job_id)
        requests.post(
            BASE_URL + "/answerCallbackQuery",
            data={
                "callback_query_id": callback["id"],
                "text": "✅ Saved"
            }
        )

    elif action == "skip":
        save_skipped(job_id)
        print("SKIP JOB:", job_id)
        requests.post(
            BASE_URL + "/answerCallbackQuery",
            data={
                "callback_query_id": callback["id"],
                "text": "❌ Skipped"
            }
        )
    elif action == "unsave":
        remove_favorite(job_id)
        print("UNSAVE JOB:", job_id)

        requests.post(
            BASE_URL + "/answerCallbackQuery",
            data={
                "callback_query_id": callback["id"],
                "text": "🗑 Removed from saved"
            }
        )


def run_callback_loop():

    offset = None

    print("🚀 Callback loop started...")

    while True:

        updates = get_updates(offset)

        for update in updates.get("result", []):

            offset = update["update_id"] + 1

            if "callback_query" in update:
                handle_callback(update)

            if "message" in update:
                handle_message(update["message"])


def handle_message(message):

    if not message:
        return

    text = message.get("text")
    chat_id = message["chat"]["id"]

    if not isinstance(text, str):
        return

    if text == "/saved":
        send_saved_jobs(chat_id)

if __name__ == "__main__":
    run_callback_loop()   