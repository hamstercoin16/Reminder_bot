from aiogram.types import  KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

#Actions
def actions_keyboard():
    builder = ReplyKeyboardBuilder()
    candidate_actions = ["view candidates", "delete candidate",'add candidate']
    for aciton in candidate_actions:
        builder.add(KeyboardButton(text=aciton))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

#Canndidate
def add_candidate_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Choose name candidate"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def delete_candidate_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="Delete candidate"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

