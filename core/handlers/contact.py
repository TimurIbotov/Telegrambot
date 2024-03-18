from aiogram.types import Message
from aiogram import Bot

async def get_true_contact(messange: Message, bot: Bot):
    if messange.contact.user_id == messange.from_user.id:
        await messange.answer(f"Siz <b>O'z</b>kontaktizni tashadiz")
    else:
        await messange.answer(f'Boshqa kontact yubordiz')