import sqlite3
import telegram
from main import *
import requests
import json
from telegram import ReplyKeyboardMarkup, KeyboardButton


def is_phone_number_in_db(phone_number):
    c = conn.cursor()
    c.execute("SELECT * FROM employee_employees WHERE phone_number=?", (phone_number,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False


async def handle_messages(update, context):
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
        url = 'http://127.0.0.1:8000/faq/faq'
        response = requests.get(url)
        faq_list = response.json()

        buttons = []
        for faq in faq_list:
            buttons.append([InlineKeyboardButton(faq['question'], callback_data=faq['id'])])

        faq_keyboard = InlineKeyboardMarkup(buttons)
        faq_text = 'Выберите вопрос:'
        await context.bot.send_message(chat_id=chat_id, text=faq_text, reply_markup=faq_keyboard)
        # button_id = int(update.callback_query.data)
        #
        # # Get the answer text corresponding to the ID
        # rows = context.user_data.get('rows', [])
        # for row in rows:
        #     if row['faq_id'] == button_id:
        #         answer_text = row['answer']
        #         break
        # else:
        #     answer_text = 'Answer not found.'
        #
        # # Send the answer to the user
        # update.callback_query.answer(answer_text)
        #
