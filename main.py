from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from config import TOKEN
from logica import *

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [MessageHandler(Filters.text, menu)],
            ESTUDO: [MessageHandler(Filters.text, estudo)],
            LIVROS: [MessageHandler(Filters.text, livros)]
        },
        fallbacks=[]
    )

    dp.add_handler(conv)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
