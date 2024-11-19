from variables.event_meneger import text_event
from variables.bot import  dp



# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    #await pass_meneger.progress(message.chat.id,"Halloween",1000)
    asyncio.create_task(try_delete_message(chat_id=message.chat.id, message_id=message.message_id))
    user_id = message.from_user.id
    add_new_user_activity(user_id)
    # Разбиваем текст и получаем аргументы
    args = message.text.split()

    # Проверяем, есть ли аргументы и получаем ID из них
    referred_by_id = int(args[1]) if len(args) > 1 else None

    if not db.user_exists(user_id):
        db.add_user(user_id)
        db.set_nickname(user_id, gen_nik())
        await bot.send_message(user_id, "Здравствуйте, ваше имя: " + db.get_nickname(user_id))
        await asyncio.sleep(1)

        if referred_by_id and db.user_exists(referred_by_id):  # Проверяем, что ID действительный
            # Сообщаем, что новый пользователь зарегистрировался по реферальной ссылке
            await bot.send_message(referred_by_id,
                                   f"Пользователь с ID {user_id} зарегистрировался по вашей реферальной ссылке! Ваша награда : {db.set_referal(referred_by_id)}")
            info.add_blok('Рег', user_id, id_pol = referred_by_id)
        else:
            info.add_blok('Рег', user_id)
    #await bot.send_message(user_id, "Приветствую, " + db.get_nickname(user_id), reply_markup=_button.gl_menu_keyboard_inline(), parse_mode='HTML')
    await send_menu_message_v2(message.chat.id)
