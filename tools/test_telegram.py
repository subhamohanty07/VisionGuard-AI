import requests

BOT_TOKEN = "8875175932:AAEqeA3Z8FJthcdBLewIgJ3OrP-059ddd7w"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)

print(response.json())