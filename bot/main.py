# для ф-ии start_bot and _on_start_up
import os

from aiogram import Bot, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv


from handlers.admin.ahandlers import *
from handlers.user.uhandlers import *
from order_telegram_bot.sqlite_bot.sqlite import *

# забираем токен из .env
load_dotenv()
TOKEN = os.getenv('API_KEY')


# запуск базы данных(создание)
# async def on_startup(_):
#     await db_start()


def start_bot():
    """ф-ия для инициализации bot dp и запуска через executor"""
    my_storage = MemoryStorage()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=my_storage)
    db_start()

    # admin handlers
    dp.register_message_handler(hide_command, commands=['hide'])
    dp.register_message_handler(admin_signin, Text(equals='Вход'), state=AdminStatesGroup.hide_field)
    dp.register_message_handler(enter_login, state=AdminStatesGroup.enter_login)
    dp.register_message_handler(enter_password, state=AdminStatesGroup.enter_password)

    # user handlers
    # команда /start для обычного пользователя
    dp.register_message_handler(start_user_cmd, commands=['start'])

    # команда /help для обычного пользователя
    dp.register_message_handler(help_user_cmd, commands=['help'])

    # команда /desc (описание бота) для обычного пользователя
    dp.register_message_handler(description_cmd, commands=['desc'])

    # команда для получения ближайших событий
    dp.register_message_handler(get_events, Text(equals='Что будет?', ignore_case=True))

    # команда для перехода в меню
    dp.register_message_handler(get_menu_position, Text(equals='Меню', ignore_case=True))

    # состояние выбора позиций меню
    dp.register_message_handler(choice_position_menu, state=UserMenuStatesGroup.viewing_menu)

    executor.start_polling(dp, skip_updates=True)

