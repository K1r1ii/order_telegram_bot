START_USER_TEXT = """Добро пожаловать в <b>"КофеШтабот"</b> 🍔🎉
Приветствую тебя, мой <b>голодный друг!</b> Я - твой надежный гид в мире вкусных бургеров и захватывающих мероприятий в 
<i>Тутаеве</i>.
🍔 У нас самые сочные и аппетитные бургеры, которые подарят твоим вкусовым сосочкам незабываемые впечатления.
🎉 А наш "Событиявизор" всегда подскажет, что интересного происходит в Тутаеве: <i>яркие концерты, 
культурные мероприятия, фестивали и многое другое</i>!
Выбирай свой бургер, окунайся в море вкуса, и готовься к незабываемым приключениям вместе с нами!
🔥 Нажми на одну из кнопок и давай начнем нашу кулинарную и культурную экскурсию! 🚀'
"""
HELP_USER_TEXT = """
• <b>/start</b> - Начать волшебное путешествие в мир <b>"КофеШтабот"</b>. Здесь ты найдешь вкуснейшие 
бургеры и узнаешь о самых интересных мероприятиях в Тутаеве.

• <b>/desc</b> - Узнать подробное описание нашего бота.

• <b>/help</b> - Показать список доступных команд и их краткое описание. 
Мы всегда готовы помочь и ответить на ваши вопросы.🥰
"""
DESCRIPTION_USER = """
Путешествуйте по волшебному миру <i>бургеров и мероприятий</i> с нашим ботом! Откройте для себя вкуснейшие бургеры и 
узнайте о самых интересных событиях в Тутаеве.
"""

EVENTS_7DAYS = 'Вот <b>все</b> мероприятия на ближайшие 7 дней!🔥'
NO_EVENTS = 'Событий пока нет💁‍♂️, но они обязательно появятся!'
CHOOSE_BURGER = 'Выберите понравившийся бургер, чтобы узнать о нем подробнее!'
ADDRESS = 'Введите адрес для доставки, например, Тутаев, улица Волжская Набережная 19, ' \
         'квартира 1.'
IMPOSSIBLE_TO_ORDER = 'Невозможно сделать заказ, пока ваша корзина пуста.'
DONT_CORRECT_ADDRESS = 'Неверно введен адрес! Попробуйте еще раз.'
DONT_CORRECT_PAYMENT = 'Неверно выбран способ оплаты, напишите картой или наличными'

IN_USER_MENU = 'Вы вышли в главное меню user'
IN_ADMIN_MENU = 'Вы вышли в главное меню admin'
DONT_CORRECT_DATA = 'Вы ввели неверные данные. Вам нужно нажать на кнопку!'
TIPS_FOR_PASS = 'Пароль может быть представлен только в виде текста/emoji'
WHAT_U_WANR = 'Выберите что бы вы хотели сделать?'
EVENT_NAME = 'Введите название мероприятия:'
NEED_LINK = 'Можете передать мне ссылку на сторонние сайты/приложения или "-" ' \
            'если хотите пропустить этот этап...'
NO_LINK = 'Хорошо. У данного объявления не будет ссылки на сторонние сервисы.' \
          'Остался последний шаг) Подтвердите правильность заполненных данных'
NEED_DATE = 'Теперь мне нужно записать дату начала события в формате чч.мм.гггг'
ADM_CMD_HIDE = 'Вы зашли в скрытое поле регистрации!'
ADM_SIGNIN = 'Добро пожаловать в меню входа в аккаунта администратора'
ADM_CONF_PASS = 'Пароль успешно подтверждён!\nТеперь Вам доступен функционал администратора'
ADM_RE_REGISTR = 'Вы уже зарегистрированы как администратор. Повторная регистрация невозможна'
ADM_ALRADY_HAVE = 'Уже существует главный администратор бота\nЧтобы стать админом введите его пароль:'
UNCORECT_PASS = 'Неверный пароль!!!'
IMAG_NEW_PASS = 'Теперь придумайте свой пароль:'
CORRECT_PASS = 'Отлично вы ввели корректный пароль!'
YOU_ADM = 'Теперь вы стали администратором!'
DONT_ADM = 'Вы не являетесь администратором'
ENTER_PASS = 'Введите Ваш пароль:'

WARNING_EDIT_A = 'Предупреждение! Сейчас будет повторный процесс заполнения данных. ' \
                 'Всё прошлые данные мероприятия будут утеряны. Сохраните их!'
CREATE_NEW_ADV = 'В данном меню Вы можете создать мероприятие. ' \
                 'Уведомление о котором сможет получить пользователь' \
                 'Если на одном из этапов будут введены не точные данные не волнуйтесь' \
                 'в конце создания поста будет возможность переделать событие)'
CORRECT_NAME = 'Название должно быть текстом или emoji!' \
               'Попробуйте снова...'
CORRECT_DATE_ADV = 'В дате не должно быть букв + ' \
                   'должна быть записана в формате 29.10.2004 ' \
                   '+ не дальше чем на 3 года с тек.дня'
GET_DESC_DATE_ADV = 'Потерпите осталось ещё немного.. Необходимо заполнить описание события (2 - 3 предл)'
GET_PICT_ADV = 'Скинь мне красивую фоточку чтобы людям захотелось придти на этот праздник'
LAST_STEP_ADV = 'Отлично это то что нужно. Я думаю людям понравится!' \
                ' Остался последний шаг) Подтвердите правильность заполненных данных'
SUCESS_ADV_IN_DB = '<i>Отлично!</i> Мероприятие успешно добавлено, в список ближайших событий!\nПеревожу в гл.меню'
EDIT_EXIST_EVENTS = 'В данном разделе можно редактировать уже созданные события'
NO_EVENTS_TO_EDIT = 'Пока ещё не создано не одно мероприятие. Для начала нужно его создать!'
LIST_EXIST_EVENTS = 'Вот список мероприятий которые уже созданы формат(id|Название|Дата). Выберите нужное...'
NO_EVENT = 'Такого мероприятия не существует. В следующий раз выберите один из ' \
           'предложенных вариантов. Перехожу в гл.меню admin'
NO_DISH = 'Такого товара не существует. В следующий раз выберите один из ' \
          'предложенных вариантов. Перехожу в гл.меню admin'
BURGERS_MENU = 'В данном разделе вы можете добавлять/изменять товары в меню'
GET_BURGER_PHOTO = 'А сейчас отправь мне фото-карточку товара (постарайся найти ' \
                   'картинку которая будет вызывать аппетит)'
DISH_DESCRIP = 'Введите описание блюда [состав/описание] и т.д'
WARNING_EDIT_D = 'Предупреждение! Сейчас будет повторный процесс заполнения данных. ' \
                 'Всё прошлые данные блюда будут утеряны. Сохраните их!'

list_stickers = ['CAACAgIAAxkBAAEJ7wJkz0Eu9uEFWuaBN67vYWYkqBc4rgAC-wwAAtM_YUvr5BZL5j6FIi8E',
                 'CAACAgIAAxkBAAEJ7v5kz0AyJIVNpH7HfAOghaNwu69D1gAC7goAAp2hYUuW93rCAubsUC8E',
                 'CAACAgIAAxkBAAEJ7wZkz0FqrWOPVMUlvL3KnOiF7_TcgwAC_AsAAsgj6Eu8480GmNtDHi8E',
                 'CAACAgIAAxkBAAEJ7whkz0F_0d-iF4KBySwM8F2oh0mIvgACOAsAAk7kmUsysUfS2U-M0C8E',
                 'CAACAgIAAxkBAAEJ7wxkz0HG7-N1EMjBFFbPF2lxFM1THgACGwADT_uyHEqceSi_8-b8LwQ',
                 'CAACAgIAAxkBAAEJ7w5kz0H6JpUnadEYBAY104_YV_aM7gACUAADUomRI9GC8WQV4STYLwQ',
                 'CAACAgIAAxkBAAEJ7xBkz0IVEuP1BuHlIjLNfwVm-SKLAANGAANSiZEj-P7l5ArVCh0vBA',
                 'CAACAgIAAxkBAAEJ7xJkz0Iwu2iVSnFCouXdBBsH-at5swAC9QIAApzW5woDP3qDEC4Oby8E',
                 'CAACAgIAAxkBAAEJ7xZkz0Jy1GBXIik--Vdie9X9eINBdQAC7QwAAk-kKUjLaFqt0Ez7Di8E',
                 'CAACAgIAAxkBAAEJ7xhkz0KPryvw4xxgEp8MvKKr-Rj9agACNgkAAhhC7gjp6gM5iy-kUi8E']
