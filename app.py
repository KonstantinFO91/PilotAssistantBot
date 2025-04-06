from flask import Flask, request
import telegram
import os

app = Flask(__name__)
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route("/")
def index():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Echo: {text}")
    return "ok"

if __name__ == "__main__":
    app.run(port=5000)
