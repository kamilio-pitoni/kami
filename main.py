import time
import telebot

# Сюда вставляешь токен, который взял у @BotFather
TOKEN = "7210536235:AAGCl2u-WTpZpuLQxvj60sxZgZdePivBG2g"

bot = telebot.TeleBot(TOKEN)


# Обработчик абсолютно всех текстовых сообщений
@bot.message_handler(content_types=["text"])
def echo_all(message):
    try:
        # Бот просто отправляет обратно тот же текст, что ты ему написал
        bot.reply_to(message, message.text)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


# Главный конвейер запуска, который защищает от падений
if __name__ == "__main__":
    print("Бот успешно запущен и готов к работе...")

    while True:
        try:
            # interval=0 и timeout=20 — самые стабильные настройки для длинных запросов
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as error:
            # Если упал интернет или легла телега, бот не выключится,
            # а просто подождет 5 секунд и попробует подключиться снова
            print(f"Произошел сбой сети: {error}. Перезапуск через 5 секунд...")
            time.sleep(5)
          
