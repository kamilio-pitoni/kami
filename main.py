import time
import telebot

# Твой тестовый токен зашит прямо в код
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
            # Настройки для стабильного удержания соединения
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as error:
            # Если оборвется сеть, бот не упадет, а перезапустится через 5 секунд
            print(f"Произошел сбой сети: {error}. Перезапуск через 5 секунд...")
            time.sleep(5)
            
