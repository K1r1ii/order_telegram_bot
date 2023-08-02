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


async def on_startup(_):
    """Запуск базы данных (создание)"""
    db_start()


def start_bot():
    """ф-ия для инициализации bot dp и запуска через executor"""
    my_storage = MemoryStorage()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=my_storage)

    # самая главная кнопка отмены
    dp.register_message_handler(cancel, Text(equals='Отмена'), state='*')

    # =======================admin handlers=======================
    # вход в скрытое поле
    dp.register_message_handler(hide_command, commands=['hide'])

    # Регистрация нового админа
    dp.register_message_handler(admin_login, Text(equals='Регистрация'), state=AdminStatesGroup.hide_field)

    # Запрос пароля при регистрации нового админа
    dp.register_message_handler(enter_new_password, state=AdminStatesGroup.enter_new_password)

    # подтверждение пароля админа если регистрируется 2 >= админов
    dp.register_message_handler(enter_pass_conf, state=AdminStatesGroup.enter_pass_conf)

    # вход в акк админа
    dp.register_message_handler(admin_signin, Text(equals='Вход'), state=AdminStatesGroup.hide_field)

    # ввод пароля
    dp.register_message_handler(enter_password, state=AdminStatesGroup.enter_password)

    # =======================user handlers=======================
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

    # ответ на нажатие inline кнопки
    dp.register_callback_query_handler(callback_add_basket)

    # обработчик выхода из меню (если пользователь ничего не выбрал)
    dp.register_message_handler(back_menu_cmd, Text(equals='Вернуться', ignore_case=True))

    # обработчик команды возврата в меню
    dp.register_message_handler(back_in_menu_cmd, Text(equals='Вернуться в меню', ignore_case=True))

    # обработчик выхода в корзину
    dp.register_message_handler(viewing_basket, Text(startswith='Корзина', ignore_case=True))

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
