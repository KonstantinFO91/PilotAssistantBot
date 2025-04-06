import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот активен и готов к работе!")

# Инициализация приложения
app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

# Добавление обработчика
app.add_handler(CommandHandler("start", start))

# Запуск webhook-сервера
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
    url_path=os.getenv("TELEGRAM_TOKEN"),
    webhook_url=f"https://pilot-assistant-bot.onrender.com/{os.getenv('TELEGRAM_TOKEN')}"
)
