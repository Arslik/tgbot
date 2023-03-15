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

if __name__ == '__main__':
    application = ApplicationBuilder().token('6131018390:AAH-rxg7k23Gd1dbVChPnysn-Asx333fcZU').build()

    application.add_handler(start_handler)
    application.add_handler(phone_number_handler)

    application.run_polling()
