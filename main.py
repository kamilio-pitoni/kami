import os
import sys
import time
import telebot

# Бот берёт токен из настроек самого хостинга (Переменные окружения)
TOKEN = os.getenv("7210536235:AAGCl2u-WTpZpuLQxvj60sxZgZdePivBG2g")

if not TOKEN:
    print(
        "Ошибка: Переменная BOT_TOKEN не найдена в настройках хостинга!",
        file=sys.stderr,
    )
    sys.exit(1)

bot = telebot.TeleBot(TOKEN)


# Обработчик абсолютно всех текстовых сообщений
@bot.message_handler(content_types=["text"])
def echo_all(message):
    try:
        bot.reply_to(message, message.text)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


# Главный конвейер запуска
if __name__ == "__main__":
    print("Бот успешно запущен и готов к работе...")

    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as error:
            print(f"Произошел сбой сети: {error}. Перезапуск через 5 секунд...")
            time.sleep(5)
