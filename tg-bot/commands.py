import sqlite3
import telegram
from main import *


def is_chat_id_in_db(chat_id):
    c = conn.cursor()
    c.execute("SELECT * FROM employee_employees WHERE chat_id=?", (chat_id,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False


async def handle_messages(update, context):
    chat_id = update.message.chat_id
    if is_chat_id_in_db(chat_id):
        await context.bot.send_message(chat_id=chat_id, text="Here's the menu")
    else:
        await context.bot.send_message(chat_id=chat_id, text="Pass the registration,please")