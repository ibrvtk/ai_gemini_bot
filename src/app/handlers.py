from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from config import (
    BOT, AI_MODEL,
    generate_response
)


rt = Router()



@rt.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f"<b>Общение началось.</b>\nМодель ИИ: <code>{AI_MODEL}</code>.")

@rt.message(F.text)
async def f_response(message: Message):
    answer_message_obj = await message.answer("⏳ <i>Подождите...</i>")
    response = await generate_response(message.text)
    await BOT.edit_message_text(
        chat_id=message.from_user.id,       
        message_id=answer_message_obj.message_id,
        text=response
    )