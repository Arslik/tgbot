import sqlite3
import telegram
from main import *
import requests
import json
from telegram import ReplyKeyboardMarkup, Update, CallbackQuery, Contact, \
    Update, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, \
    filters, InlineQueryHandler, CallbackQueryHandler, Updater


async def handle_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    url = f'http://127.0.0.1:8000/employee/?type=chat_id&value={chat_id}'

    response = requests.get(url)
    database_chat_id = response.json()['chat_id']

    if chat_id == database_chat_id:
        menu_buttons = [
            [KeyboardButton("Инфо")],
            [KeyboardButton("Клубы")],
            [KeyboardButton("FAQ")],
            [KeyboardButton("Новости")],
            [KeyboardButton("Программа лояльности")],
        ]
        menu_keyboard = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
        menu_text = "Добро пожаловать!"
        await context.bot.send_message(chat_id=chat_id, text=menu_text, reply_markup=menu_keyboard)

    else:
        keyboard = [[KeyboardButton(text="Share contact", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await context.bot.send_message(chat_id=chat_id, text="Share Contact", reply_markup=reply_markup)


