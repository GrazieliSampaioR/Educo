from telegram.ext import ConversationHandler
from menus import *

MENU, ESTUDO, LIVROS = range(3)

def start(update, context):
    update.message.reply_text(
        "Olá companheiro de estudos, aqui você vai achar todo tipo de conteúdo para te ajudar nos estudos!" \
        " Escolha uma opção para começar seus estudos:",
        reply_markup=menu_principal()
    )
    return MENU

def menu(update, context):
    texto = update.message.text

    if texto == "📚 Conteúdo para estudo":
        update.message.reply_text(
            "Escolha a área que você quer estudar:",
            reply_markup=menu_estudo()
        )
        return ESTUDO

    elif texto == "📖 Livros":
        update.message.reply_text(
            "Escolha o tipo:",
            reply_markup=menu_livros()
        )
        return LIVROS

def estudo(update, context):
    texto = update.message.text

    if texto == "⬅️ Voltar":
        update.message.reply_text(
            "Menu principal:",
            reply_markup=menu_principal()
        )
        return MENU

    update.message.reply_text(
        f"Você escolheu: {texto}\n(Imagine links aqui)"
    )
    return ESTUDO

def livros(update, context):
    texto = update.message.text

    if texto == "⬅️ Voltar":
        update.message.reply_text(
            "Menu principal:",
            reply_markup=menu_principal()
        )
        return MENU

    update.message.reply_text(
        f"Você escolheu: {texto}\n(Aqui entram os livros)"
    )
    return LIVROS
