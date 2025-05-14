from telegram.ext import Application, MessageHandler, filters, CommandHandler
from flask import Flask
import asyncio
import threading

# Настройки бота
BOT_TOKEN = "7655690664:AAEVjJSCMMpuV6WxSsp1cUb2HeX_t7brm4I"
ADMIN_CHAT_ID = "-1002532410390"

# Инициализация Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот активен и работает 24/7!"

# Функции бота (обработчики сообщений)
async def handle_message(update, context):
    await update.message.reply_text(" Сообщение получено!")

async def start_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    await app.run_polling()

# Запуск в отдельном потоке
def run_bot():
    asyncio.run(start_bot())

if __name__ == "__main__":
    # Запускаем бота в фоне
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    
    # Запускаем веб-сервер
    app.run(host='0.0.0.0', port=5000)
