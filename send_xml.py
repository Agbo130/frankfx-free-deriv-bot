import requests

# === CONFIG ===
BOT_TOKEN = "8095298712:AAHYCpAQi-28XrcII7gf_yELnH0BroTcl2g"
CHAT_ID = "-1001695498156"  # FrankFx Bot channel
GITHUB_BASE = "https://raw.githubusercontent.com/Agbo130/frankfx-free-deriv-bot/main/bots"

# === Get current index from bot_index.txt ===
def get_current_index():
    res = requests.get("https://raw.githubusercontent.com/Agbo130/frankfx-free-deriv-bot/main/bot_index.txt")
    if res.status_code != 200:
        raise Exception(f"❌ Failed to fetch index file: {res.status_code}")
    return int(res.text.strip())

# === Send the XML bot link ===
def send_xml(index):
    file_url = f"{GITHUB_BASE}/free{index}.zip"
    caption = (
        f"📦 FREE DERIV BOT #{index}\n\n"
        f"👇 Tap below to download:\n"
        f"[⬇️ Download XML Bot]({file_url})\n\n"
        f"🚀 Load bot on: https://bot.frankfxx.com\n"
        f"━━━━━━━━━━━━━━━\n"
        f"👉 [JOIN VIP](https://t.me/frankfx22)\n"
        f"🤖 [AUTOMATED BOT](http://bot.frankfxx.com/)\n"
        f"📊 [TRADINGVIEW](https://www.tradingview.com/u/FrankFx14/)\n"
        f"📍 [TOP BROKER](https://t.me/frankfxforextrade/355) | [V75 BROKER](https://track.deriv.com/_X4my-_6ZqrDUC5-fI8wshmNd7ZgqdRLk/1/)\n"
        f"▶️ [YOUTUBE](https://www.youtube.com/channel/UCp_YkAKg_N3JmTL_LI4cSuA?sub_confirmation=1)\n"
        f"📸 [INSTAGRAM](https://www.instagram.com/frankfx120/)\n"
        f"🐦 [TWITTER](https://x.com/FrankFx14)\n"
        f"🌍 [MY WEBSITE](https://frankfxx.com/)"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": caption,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=data)
    print("✅ Sent bot:", file_url)
    print("📨 Telegram response:", response.status_code)

# === Main ===
def run():
    index = get_current_index()
    send_xml(index)
    print(f"✅ Finished sending free{index}.zip")

run()
