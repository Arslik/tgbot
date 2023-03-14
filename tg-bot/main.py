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
    application = ApplicationBuilder().token('6201725037:AAFMh2_lg8slH7eiBVvLyK2NdkWKTLJryXg').build()

    start_handler = CommandHandler('start', handle_messages)
    application.add_handler(start_handler)

    application.run_polling()
