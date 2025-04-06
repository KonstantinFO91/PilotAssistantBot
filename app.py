import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Бот активен и готов к работе!")

# Инициализация приложения
app = ApplicationBuilder().token(os.environ.get("TELEGRAM_TOKEN")).build()
app.add_handler(CommandHandler("start", start))

# Запуск webhook-сервера
if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        url_path=os.environ.get("TELEGRAM_TOKEN"),
        webhook_url=f"https://pilot-assistant-bot.onrender.com/{os.environ.get('TELEGRAM_TOKEN')}"
    )
