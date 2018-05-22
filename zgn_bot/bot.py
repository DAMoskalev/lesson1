# coding=utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater("559166681:AAETkAV20RGQbexKJ_YVateSp8JVDNapzxA", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


if __name__ == "__main__":
    main()


