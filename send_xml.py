import requests

# === CONFIGURATION ===
BOT_TOKEN = '8095298712:AAHYCpAQi-28XrcII7gf_yELnH0BroTcl2g'  # FrankFx Bot Token
CHAT_ID = '-1001695498156'  # FRANKFX BOT channel (@unrulytech1)

GITHUB_USER = 'Agbo130'
REPO = 'frankfx-free-deriv-bot'
MAX_XML_COUNT = 50

# Base GitHub raw URL
GITHUB_BASE = f'https://raw.githubusercontent.com/{GITHUB_USER}/{REPO}/main'

def get_current_index():
    url = f'{GITHUB_BASE}/bot_index.txt'
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"❌ Failed to fetch index file: {res.status_code}")
    return int(res.text.strip())

def generate_message(index):
    file_url = f"{GITHUB_BASE}/bots/free{index}.xml"
    return f"""
🎁 <b>FREE DERIV BOT XML #{index}</b>

Tap below to download and test 👇

🔗 <a href="{file_url}">Download XML Bot</a>
🧠 Load it on Deriv: <a href="https://bot.frankfxx.com">bot.frankfxx.com</a>

#V75 #BoomCrash #Deriv #TradingBot
"""

def send_to_telegram(message):
    telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    res = requests.post(telegram_url, data=payload)
    if res.status_code == 200:
        print('✅ Message sent successfully.')
    else:
        print(f'❌ Telegram API error: {res.status_code}, {res.text}')

def run():
    index = get_current_index()
    message = generate_message(index)
    send_to_telegram(message)

    # Show what the next index should be
    next_index = 1 if index >= MAX_XML_COUNT else index + 1
    print(f"📌 Next time, update 'bot_index.txt' on GitHub to: {next_index}")

if __name__ == '__main__':
    run()
