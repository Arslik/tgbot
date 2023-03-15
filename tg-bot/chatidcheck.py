import sqlite3
import telegram
from main import *
import requests
import json
from telegram import Update


class ChatIdChecker:

    def __chat_id__(self, update: Update):
        self.chat_id = update.message.chat_id

    async def does_chat_id_exist(self):
        url = f'http://127.0.0.1:8000/employee/?type=chat_id&value={self.chat_id}'
        response = requests.get(url)
        database_chat_id = response.json()['chat_id']

        if self.chat_id == database_chat_id:
            return True
        else:
            return False
