import sqlite3
import telegram
from main import *
import requests
import json
from telegram import ReplyKeyboardMarkup, Update, CallbackQuery, Contact
from telegram import KeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def show_wait_message(chat_id, context):
    message = "Please wait some time, the operation is executing at the moment"
    await context.bot.send_message(chat_id=chat_id, text=message)


async def handle_messages(update:Update, context: CallbackContext):
    chat_id = update.message.chat_id
    url = f'http://127.0.0.1:8000/employee/?type=chat_id&value={chat_id}'

    await show_wait_message(chat_id, context)

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
        keyboard = {
            'keyboard': [[{'text': 'Share your phone number', 'request_contact': True}]],
            'resize_keyboard': True,
        }
        keyboard_json = json.dumps(keyboard)
        message = 'Please share your phone number:'
        send_message_url = f'https://api.telegram.org/bot6131018390:AAH-rxg7k23Gd1dbVChPnysn-Asx333fcZU/sendMessage' \
                           f'?chat_id={chat_id}&text={message}&reply_markup={keyboard_json} '
        requests.get(send_message_url)


async def handle_phone_number(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    phone_number = update.message.contact.phone_number

    await show_wait_message(chat_id, context)

    url = f'http://127.0.0.1:8000/employee/?type=phone&value={phone_number}'
    response = requests.get(url)
    database_phone_number = response.json()['phone_number']

    if database_phone_number == phone_number:
        chat_id = query.message.chat_id
        new_chat_id = data['chat_id']

        url = f'http://127.0.0.1:8000/employee/?type=phone&value={phone_number}'
        patch_data = {"chat_id": f"{new_chat_id}"}

        response = requests.patch(url, json=patch_data)
        if response.status_code == 200:
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
            print("Error updating chat_id")
    else:
        await context.bot.send_message(chat_id=chat_id, text="Вашего номера нет в базе данных, доступ воспрещен")
