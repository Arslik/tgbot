import sqlite3
import telegram
from main import *
import requests
import json
from telegram import ReplyKeyboardMarkup, KeyboardButton


async def faq_show(update, context):
    chat_id = update.message.chat_id
    url = f'http://127.0.0.1:8000/employee/?type=chat_id&value={chat_id}'

    response = requests.get(url)
    database_chat_id = response.json()['chat_id']
    if chat_id == database_chat_id:
        response = requests.get('http://127.0.0.1:8000/faq/faq')
        rows = response.json()

        buttons = []
        for row in rows:
            button_text = row['question']
            button_data = str(row['faq_id'])
            buttons.append([KeyboardButton(button_text, callback_data=button_data)])
        faq_keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        await context.bot.send_message(chat_id=chat_id, text='Выберите вопрос:', reply_markup=faq_keyboard)

        context.user_data['rows'] = rows

        await update.callback_query.answer(answer_text)

        button_id = int(update.callback_query.data)

        rows = context.user_data.get('rows', [])
        for row in rows:
            if row['faq_id'] == button_id:
                answer_text = row['answer']
                break
        else:
            answer_text = 'Answer not found.'

        await update.callback_query.answer(answer_text)


# def faq_button(update, context):
#     button_id = int(update.callback_query.data)
#
#     rows = context.user_data.get('rows', [])
#     for row in rows:
#         if row['faq_id'] == button_id:
#             answer_text = row['answer']
#             break
#     else:
#         answer_text = 'Answer not found.'
#
#     update.callback_query.answer(answer_text)
