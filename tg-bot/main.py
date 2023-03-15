import sqlite3
import logging
from handlers.login.chat_id_handler import *
from handlers.registration.phone_number_handler import *
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, \
    filters, InlineQueryHandler, CallbackQueryHandler, Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

conn = sqlite3.connect('../db.sqlite3')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6131018390:AAH-rxg7k23Gd1dbVChPnysn-Asx333fcZU').build()

    start_handler = CommandHandler('start', handle_chat_id)
    phone_number_handler = MessageHandler(filters.CONTACT, handle_button_press)

    application.add_handler(start_handler)
    application.add_handler(phone_number_handler)

    application.run_polling()
