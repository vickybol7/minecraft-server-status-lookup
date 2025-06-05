import time
import requests

# CONFIG
LOG_FILE = "logs.txt"
BOT_TOKEN = "6165663083:AAHigA2Z0IUJYeuvCoGpU5OMCwv84zrx8uo"
CHAT_ID = "5721393154"
POLL_INTERVAL = 2  # seconds

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def monitor_log():
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(POLL_INTERVAL)
                continue
            if "Player connected:" in line:
                name = line.split("Player connected:")[1].split(",")[0].strip()
                send_telegram_message(f"✅ {name} joined the Bedrock world!")
            elif "Player disconnected:" in line:
                name = line.split("Player disconnected:")[1].split(",")[0].strip()
                send_telegram_message(f"❌ {name} left the Bedrock world.")

if __name__ == "__main__":
    monitor_log()
