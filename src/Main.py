from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Hello World")


def main():
    updater = Updater("5778932769:AAEuzdbUPPBSLXcffPgiZS7Y2NwmcFJWI4o", use_context=True)
    dp = updater.dispatcher # dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
        
if __name__ == "__main__":
    main()
    # to be added