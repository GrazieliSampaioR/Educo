from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from config import TOKEN
from logica import *

def main():

    application = Application.builder().token(TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu)],
            ESTUDO: [MessageHandler(filters.TEXT & ~filters.COMMAND, estudo)],
            RECURSOS: [MessageHandler(filters.TEXT & ~filters.COMMAND, recursos)],
            MATERIA: [MessageHandler(filters.TEXT & ~filters.COMMAND, materia)],
             SUGESTAO: [MessageHandler(filters.TEXT & ~filters.COMMAND, sugestao)]
        },
        fallbacks=[]
    )

    application.add_handler(conv)

    print("Educo iniciado!")

    application.run_polling()

if __name__ == "__main__":
    main()
