import requests

BOT_TOKEN = "8906810626:AAGY-PhVlHkHxgEM4wsn2mNmvOesVMdmHu8"
CHAT_ID="246929048"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "test message"
})

print(r.status_code)
print(r.text)