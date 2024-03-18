from aiogram import Bot
from aiogram.types import Message
import json


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"<b>Salom {message.from_user.first_name},Sizni ko'rgandan xurzandman</b>")
    await message.answer(f"<s>Salom{message.from_user.first_name},Sizni ko'rgandan xursandman</s>")
    await message.reply(f"<tg-spoiler>Salom{message.from_user.frist_name}.Sizni ko'rgandan xursandman</tg-spoiler>")



async def get_photo(message:Message, bot:Bot):
    await message.answer(f'Yaxshi sen rasm tashadiz , men uni soxranit qildim')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_hello(message:Message,bot:Bot):
    await message.answer(f"Sizga xam Salom")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)