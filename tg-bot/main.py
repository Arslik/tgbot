import sqlite3
import logging
from commands import *
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, InlineQueryHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


conn = sqlite3.connect('../db.sqlite3')

if __name__ == '__main__':
    application = ApplicationBuilder().token('5994687353:AAFo63X3zGnhHYmSv8l7e0A-43n3Fsv6JIk').build()

    start_handler = CommandHandler('start', handle_messages)
    application.add_handler(start_handler)

    application.run_polling()