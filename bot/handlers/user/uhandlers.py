from aiogram import types
from aiogram.dispatcher import FSMContext

from order_telegram_bot.bot.config import *
from order_telegram_bot.bot.keyboards.user.replykb import *
from order_telegram_bot.bot.keyboards.user.inlinekb import *
from order_telegram_bot.sqlite_bot.sqlite import *
from order_telegram_bot.bot.handlers.user.user_states import UserMenuStatesGroup


# обработчики команд пользователя


async def start_user_cmd(message: types.Message):
    """Обработчик команды /start"""

    # # ВРЕМЕННО
    # await create_event()
    # await create_menu()

    await message.answer(text=START_USER_TEXT, reply_markup=user_start_keyboard(message.from_user.id))


async def help_user_cmd(message: types.Message):
    """Обработчик команды /help"""
    await message.answer(text=HELP_USER_TEXT)


async def description_cmd(message: types.Message):
    """Обработчик команды /desk(описание бота)"""
    await message.answer(text=DESCRIPTION_USER)


async def get_events(message: types.Message):
    """Обработчик команды 'Что будет?' для получения событий на ближайшие 7 дней"""
    data_events = week_events()
    if data_events:
        await message.answer(text='Вот все мероприятия на ближайшие 7 дней!')
    else:
        await message.answer(text='Событий пока нет, но они обязательно появятся!')
    # вывод событий
    for i in data_events:
        # await message.answer_photo(i[1], caption=f'{i[2]}\n{i[3]}')
        # ВРЕМЕННЫЙ ВАРИАНТ СООБЩЕНИЯ БЕЗ ФОТО
        await message.answer(text=f'{i[2]}\n{i[3]}')


async def get_menu_position(message: types.Message):
    """Отправка пользователю карточки меню"""
    await UserMenuStatesGroup.viewing_menu.set()
    await message.answer(text='Выберите понравившийся бургер, чтобы узнать о нем подробнее!',
                         reply_markup=user_menu_keyboard())


async def choice_position_menu(message: types.Message, state: FSMContext):
    """Пользователь выбирает позицию меню"""

    # действия при нажатии кнопки выхода
    if message.text.lower() == 'вернуться':
        await state.finish()
        await message.answer(text='Вы в главном меню!', reply_markup=user_start_keyboard(message.from_user.id))
    else:
        await state.finish()
        # словарь с данными о продуктах(ключ - название продукта)
        menu_dict = menu_positions()

        await message.delete()
        await message.answer(text='Хороший выбор!', reply_markup=user_menu_position())
        # await message.answer_photo(menu_dict[message.text][0], caption=f'{message.text}\n'
        #                                                                f'{menu_dict[message.text][1]}\n'
        #                                                                f'Стоимость: {menu_dict[message.text][2]}')

        # ВРЕМЕННЫЙ ВАРИАНТ СООБЩЕНИЯ БЕЗ ФОТО
        await message.answer(text=f'{message.text}\n'
                                  f'{menu_dict[message.text][1]}\n'
                                  f'Стоимость: {menu_dict[message.text][2]}',
                             reply_markup=inline_basket_keyboard())


async def back_menu_cmd(message: types.Message):
    """Обработчик выхода в главное меню"""
    await message.answer(text='Вы в главном меню!', reply_markup=user_start_keyboard(message.from_user.id))


async def back_in_menu_cmd(message: types.Message):
    """Обработчик возврата в продуктовое меню"""
    await UserMenuStatesGroup.viewing_menu.set()
    await message.answer(text='Вы в меню доставки!', reply_markup=user_menu_keyboard())


async def callback_add_basket(callback: types.CallbackQuery):
    """Действия при нажатии inline кнопки"""
    data = callback.data
    # обработка callback данных
    # если решили увеличить кол-во
    if data.split()[0] == '+':
        await callback.message.edit_reply_markup(reply_markup=inline_basket_keyboard(count_product=int(
                                                                                        data.split()[1]) + 1))
    # если решили уменьшить кол-во
    elif data.split()[0] == '-':
        # проверка на то, чтобы при уменьшении не уходить < 0
        if data.split()[1] != '1':
            await callback.message.edit_reply_markup(reply_markup=inline_basket_keyboard(count_product=int(
                                                                                        data.split()[1]) - 1))
        else:
            await callback.answer()
    else:
        # отправка данных в БД
        for i in range(int(data)):
            add_basket(callback.from_user.id, callback.message.text.split('\n')[0])
        await callback.answer(text='Товар добавлен в корзину!')


async def viewing_basket(message: types.Message):
    """Обработчик команды просмотра содержимого корзины"""
    await message.delete()
    await message.answer(text='В вашей корзине сейчас:', reply_markup=edit_basket_keyboard())
    data = get_basket_data(message.from_user.id)
    if data:
        # получаем список продуктов
        product_names = data[1].split(',')

        product_count = dict()
        menu_dict = menu_positions()

        # собираем все в словарь (название продукта: кол-во)
        for product in product_names:
            if product in product_count.keys():
                product_count[product] += 1
            else:
                product_count[product] = 1
        for product in product_count:
            await message.answer(text=f'{product} - {product_count[product]}шт.'
                                      f' {product_count[product] * menu_dict[product][2]}руб'
                                      f' ({menu_dict[product][2]}руб/шт.)')
    else:
        await message.answer(text='Ваша корзина пуста')
