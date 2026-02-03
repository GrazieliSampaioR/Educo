from telegram import ReplyKeyboardMarkup as RKM

def menu_principal():
    return RKM(
        [
            ["📚 Conteúdo para estudo"],
            ["📖 Livros"],
            ["Sugestões"]
        ],
        resize_keyboard=True
    )

def menu_estudo():
    return RKM(
        [
            ["Computação em Nuvem"],
            ["Programação"],
            ["Estatística"],
            ["Banco de Dados"],
            ["⬅️ Voltar"]
        ],
        resize_keyboard=True
    )

def menu_livros():
    return RKM(
        [
            ["PDFs"],
            ["Links"],
            ["⬅️ Voltar"]
        ],
        resize_keyboard=True
    )
