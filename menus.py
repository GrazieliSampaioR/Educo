from telegram import ReplyKeyboardMarkup as RKM

def menu_principal():
    return RKM(
        [
            ["📚 Conteúdo para estudo"],
            ["📖 Recursos Extras"],
            ["Sugestões"]
        ],
        resize_keyboard=True
    )

def menu_estudo():
    return RKM(
        [
            ["Lógica de Programação"],
            ["SQL"],
            ["Estatística"],
            ["Banco de Dados"],
            ["⬅️ Voltar"]
        ],
        resize_keyboard=True
    )

def menu_recursos():
    return RKM(
        [
            ["📄 PDFs"],
            ["🌐 Sites Úteis"],
            ["🛠️ Ferramentas"],
            ["⬅️ Voltar"]
        ],
        resize_keyboard=True
    )

def menu_materia():
    return RKM(
        [
            ["📹 Videoaulas"],
            ["📝 Exercícios"],
            ["⬅️ Voltar"]
        ],
        resize_keyboard=True
    )

