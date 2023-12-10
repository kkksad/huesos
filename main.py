import asyncio
import logging
import sys
from random import randint
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6924411701:AAFgkV_T8dSMii3bmYVrFEvUwMBrh46QCtc"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
huesos_list=[]
admin_list=['AXAXAXAXXAXAXAXAXAXXAXAX','Olegabfbf','Vvvicit']
boy1=["Тупой", "Конченный", "Ебанутый", "Лихоеблимудый", "Пизданутый", "Высохший", "Уебищный", "Умерший",
 "Толстомудый", "Опиздолюбый", "Мелкотроемудрый", "Хуйлолюбивый", "Хуячий", "Жирномногоканальный", "Аналочленный","хуйня", "залупа", "манда", "шлюха", "лихохуярка", "блядь", 
"залупоеблогнойница", "выхухоль", "пидораска", "ебланка", "нервостенничка", "мозгоебка", "дермоблядунья","низтроехериница","приятельница червей"]
boy2=["даун", "еблан", "пидорас", "хуйлан", "говноед", "конч", "шизик", "страходуроног", "аналомокроблядник", 
"попечитель мочалок", "лизатель червей", "духопер", "блядохероблядник", "и плюшевый муфлон", "долбоблядскожопый","Тупая", "Конченная", "Ебанутая", "Блядскоеблиёбая", "Гнусная",
 "Жирная", "Токсичная", "Обтраханная", "Ебаная", "Задротская", "Горбатая", "Малость многострахоблядская", "Хуйлодуроблядская", "Соплежопая", "Мудоскотоебая"]




# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text=f"привет {message.from_user.full_name} это бот который будет хуесосить плохих людей ")

@dp.message(Command('add_huesos'))
async def command_add(message: Message) -> None:
    if message.from_user.username in admin_list:
        await message.reply(f'{message.text.split()[1]} теперь хуесос')
        
        huesos_list.append(message.text.split()[1])

@dp.message(Command('delete_huesos'))
async def command_delete(message: Message) -> None:
    if message.from_user.username in admin_list:
        await message.reply(f'{message.text.split()[1]} теперь не хуесос')
        try:
            huesos_list.remove(message.text.split()[1])
        except:
            await message.reply(f'{message.text.split()[1]} теперь не хуесос')
dp.message(Command('clear_huesos'))
async def echo_handler_clear(message: types.Message) -> None:
    global huesos_list
    if message.from_user.username in admin_list:
        for i in huesos_list:
            huesos_list.remove(i)
    

        


        
        
    
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`

   



@dp.message()
async def echo_handler(message: types.Message) -> None:
    print(message.from_user.username)
    if message.from_user.username in huesos_list:
        await message.reply(text=f"Привет {message.from_user.full_name} хочу сообщить тебе что ты {str(boy1[randint(0, len(boy1)-1)])} {str(boy2[randint(0, len(boy2)-1)])}")
    # if "ясно" in message.text.lower():
    #     црш
    #     await message.reply(text=f"Привет {message.from_user.full_name} хочу сообщить тебе что ты {str(boy1[randint(0, len(boy1)-1)])} {str(boy2[randint(0, len(boy2)-1)])}")
        
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    # try:
    #     await message.answer(text=f"Привет {message.from_user.full_name} хочу сообщить тебе что ты {str(boy1[randint(0, len(boy1)-1)])} {str(boy2[randint(0, len(boy2)-1)])}")
    # except TypeError:
    #     # But not all the types is supported to be copied so need to handle it
    #     await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
