from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater):
    tymext = """Привет, пользователь!
Я простой бот и понимаю только команду /start
"""
    update.message.reply_text(mytext)
    ptint("start")

def main():
    updtr = Updater('559166681:AAETkAV20RGQbexKJ_YVateSp8JVDNapzxA')
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.start_polling()
    updtr.idle()

if __name__ == "__main__":
    main()