from telegram.ext import CallbackContext
from functools import wraps


def wait_message(func):
    @wraps(func)
    async def wrapper(update, context):
        chat_id = update.effective_chat.id
        await context.bot.send_message(chat_id=chat_id, text="Пожалуйста, подождите")

        await func(update, context)

    return wrapper


