from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from handlers.keybords import actions_keyboard

router = Router()

@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "/start — start bot\n"
        "/help — help\n"
        "Use buttons to manage candidates"
    )

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Hello 👋\nThis is Candidate Tracking Bot.\nChoose an option:"
        "\n /help — list of commands",
        reply_markup=actions_keyboard()
    )

@router.message(lambda msg: msg.text == "add candidate")       
async def add_candidate(message: Message):
    await message.answer("Candidate logic here")

@router.message(lambda msg: msg.text == "view candidates")     
async def view_candidates(message: Message):
    await message.answer("Candidates list here")

@router.message(lambda msg: msg.text == "delete candidate")   
async def delete_candidate(message: Message):
    await message.answer("Delete candidate logic here")

@router.message(lambda msg: msg.text == "status")
async def unknown_command(message: Message):
    await message.answer("Update status logic here")