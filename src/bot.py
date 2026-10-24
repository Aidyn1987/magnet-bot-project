# src/bot.py
import os
import asyncio
from maxapi import Bot, Dispatcher, types
from dotenv import load_dotenv

# Импортируем нашу логику из соседних файлов
from logic import calculate_rating, generate_motivation

# Загружаем токен из файла .env
load_dotenv()
BOT_TOKEN = os.getenv("MAX_BOT_TOKEN")

# Небольшая проверка на всякий случай
if not BOT_TOKEN:
    print("ОШИБКА: Токен не найден! Проверь файл .env")
    exit(1)

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Правильный декоратор для новых сообщений в maxapi
@dp.message_created()
async def handle_message(event: types.MessageCreated):
    # Безопасно достаем текст сообщения (на случай если прислали стикер или картинку)
    text = event.message.body.text.lower() if event.message.body.text else ""
    
    # Получаем имя отправителя
    user_name = event.message.sender.first_name

    # Обработка команды /start
    if text == "/start":
        await event.message.answer(
            f"Привет, {user_name}! 🧲 Я — бот «Магнит».\n"
            "Мои команды:\n"
            "/rating — посмотреть рейтинг класса\n"
            "/motivation — получить заряд мотивации на день"
        )
        
    # Обработка команды /rating
    elif text == "/rating":
        rating_data = calculate_rating()
        response = "🏆 **Рейтинг класса «Магнит»** 🏆\n\n"
        for i, (name, score) in enumerate(rating_data, start=1):
            response += f"{i}. {name} — {score} баллов\n"
        await event.message.answer(response)
        
    # Обработка команды /motivation
    elif text == "/motivation":
        motivation = generate_motivation(user_name)
        await event.message.answer(motivation)
        
    # Если написали что-то другое
    else:
        await event.message.answer("Я тебя не понял. Напиши /start, чтобы увидеть меню.")

# Запуск бота
async def main():
    print("Бот 'Магнит' запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
