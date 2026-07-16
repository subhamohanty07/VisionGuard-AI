import requests

BOT_TOKEN = "8875175932:AAEqeA3Z8FJthcdBLewIgJ3OrP-059ddd7w"
CHAT_ID = "8514374546"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "🚀 VisionGuard AI is connected successfully!"
}

response = requests.post(url, data=payload)

print(response.json())