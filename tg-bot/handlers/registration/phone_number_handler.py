import sqlite3
import telegram
from main import *
import requests
import json
from telegram import ReplyKeyboardMarkup, Update, CallbackQuery, Contact, \
    Update, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, \
    filters, InlineQueryHandler, CallbackQueryHandler, Updater


async def handle_button_press(update, context):
    contact = update.message.contact.phone_number
    if contact is not None:
        chat_id = update.effective_chat.id
        is_phone_number_exist = await check_phone_number(chat_id, contact)
        if is_phone_number_exist:
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
            await context.bot.send_message(chat_id=chat_id, text="Доступ воспрещен")
    else:
        query.answer("Please share your contact information to proceed.")


async def check_phone_number(chat_id: int, phone_number: str):

    url = f'http://127.0.0.1:8000/employee/?type=phone&value={phone_number}'
    response = requests.get(url)
    database_phone_number = response.json()['phone_number']

    if database_phone_number == phone_number:

        url = f'http://127.0.0.1:8000/employee/?type=phone&value={phone_number}'
        patch_data = {"chat_id": f"{chat_id}"}

        response = requests.patch(url, json=patch_data)
        if response.status_code == 200:
            return True
        else:
            print("Error updating chat_id")
    else:
        return False


