import sqlite3
import logging
from handlers.login.chat_id_handler import *
from handlers.registration.phone_number_handler import *
from handlers.faq.faq import *
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, InlineQueryHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


conn = sqlite3.connect('../db.sqlite3')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6201725037:AAFMh2_lg8slH7eiBVvLyK2NdkWKTLJryXg').build()

    start_handler = CommandHandler('start', handle_chat_id)
    phone_number_handler = MessageHandler(filters.CONTACT, handle_button_press)
    faq_handler = MessageHandler(filters.Regex('FAQ'), faq_button_handler)
    # answer_handler = MessageHandler(filters.Regex('^Вопрос:'), get_answer_handler)
    application.add_handler(start_handler)
    application.add_handler(faq_handler)
    # application.add_handler(answer_handler)
    application.run_polling()
