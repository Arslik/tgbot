import sqlite3
import telegram
from main import *
import requests
import json


# def is_chat_id_in_db(request):
#     telegram_chat_id = update.message.chat_id
#     c = conn.cursor()
#     c.execute("SELECT * FROM employee_employees WHERE chat_id=?", (chat_id,))
#     result = c.fetchone()
#     if result:
#         return True
#     else:
#         return False


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
        await context.bot.send_message(chat_id=chat_id, text="Добро пожаловать!")
    else:
        keyboard = {
            'keyboard': [[{'text': 'Share your phone number', 'request_contact': True}]],
            'resize_keyboard': True,
        }
        keyboard_json = json.dumps(keyboard)
        message = 'Please click one of the buttons below:'
        send_message_url = f'https://api.telegram.org/bot6131018390:AAH-rxg7k23Gd1dbVChPnysn-Asx333fcZU/sendMessage' \
                           f'?chat_id={chat_id}&text={message}&reply_markup={keyboard_json} '
        requests.get(send_message_url)


# async def handle_phone(update, context):
#     phone_number = update.message.phone_number
#     if is_phone_number_in_db(phone_number):
#         await context.bot.send_message(chat_id=chat_id, text="Вы зарегистрированы!")
#     else:
#         await context.bot.send_message(chat_id=chat_id, text="Нет доступа!")

