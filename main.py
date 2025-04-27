import os
import random
import asyncio
import qrcode
import io
import logging

from dotenv import load_dotenv
from PIL import Image 
from aiogram import Dispatcher, Bot, types
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
dp = Dispatcher()



@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("hello. how are u?")


@dp.message(Command("ping"))
async def ping(message: Message):
    await message.answer("Pong!")


@dp.message(Command("help"))
async def help(message: Message):
    description = (
        "/start\n"
        "/ping\n"
        "/random <your number(optional)>\n"
        "/qrcode <your text(optional)>\n"
        "/dice\n"
        "/time\n"
        "/date\n"
        "/say <your text(optional)>\n"
        "/avatar\n"
        "/user_info\n"
        "/get_id\n"
        "/color <your hex color(optional)>\n"
    )
    await message.answer(description)


@dp.message(Command("random"))
async def rand(message: Message):
    try:
        random_num = message.text[8:].strip()
        if not random_num:
            random_num = 10
    except ValueError:
        random_num = 10
    num = random.randint(0, int(random_num))
    await message.answer(f"Random number is: {num}")


@dp.message(Command("qrcode"))
async def qrc(message: Message):

    text = message.text[8:].strip()
    if not text:
        text = "https://botsnare.vercel.app`"

    qr = qrcode.make(text)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
        
    filedata = buffer.getvalue()
    photo = types.BufferedInputFile(filedata, filename="qrcode.png")

    await message.answer_photo(photo)
@dp.message(Command("dice"))
async def dice(message: Message):
    await message.answer_dice(emoji="🎲")

@dp.message(Command("time"))
async def time(message: Message):
    now = datetime.now()
    now__time = now.strftime("%H:%M:%S")
    await message.answer(f"Now time is: {now__time}")   


@dp.message(Command("date"))
async def date(message: Message):
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    await message.answer(f"Now date is: {now_date}")    


@dp.message(Command("say"))
async def say(message: Message):
    text = message.text[5:].strip()
    if not text:
        text = "hello"
    await message.answer(text)


@dp.message(Command("avatar"))
async def avatar(message: Message):
    user_avatar = await message.bot.get_user_profile_photos(message.from_user.id)    
    await message.answer_photo(dict((user_avatar.photos[0][0])).get("file_id"))


@dp.message(Command("user_info"))
async def user_info(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    firstname = message.from_user.first_name
    fullname = message.from_user.full_name
    useravatar = await message.bot.get_user_profile_photos(message.from_user.id)
    description = (
        f"About <b>@{username}</b>\n"
        f"User id: <code>{user_id}</code>\n"
        f"Firstname: {firstname}\n"
        f"Fullname: {fullname}\n"
    )
    file_id = useravatar.photos[0][0].file_id
    await message.answer_photo(file_id, caption=description, parse_mode="HTML")

@dp.message(Command("get_id"))
async def get_id(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    await message.answer(f"Chat id: {chat_id}\nUser id: {user_id}")

@dp.message(Command("color"))
async def color(message: Message):
    try:
        hex = message.text[7:].strip()
        if not hex:
            hex = "#ffffff"
        if not hex.startswith("#"):
            hex = f"#{hex}"
        
        
        
        img = Image.new("RGB", (120, 40), hex)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        filedata = buffer.getvalue()
        photo = types.BufferedInputFile(filedata, filename="color.png")

        await message.answer_photo(photo)
        
    except Exception as err:
        await message.answer(str(err))

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=("%(asctime)s - %(levelname)s - %(message)s"), handlers=[logging.FileHandler("bot.log", encoding="utf-8"), logging.StreamHandler()])
    asyncio.run(main())
