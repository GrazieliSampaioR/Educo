# Imports usados no bot
from telegram.ext import ConversationHandler
from menus import *
import csv
# Banco de Conteúdos
VIDEOAULAS = {
    "Lógica de Programação": [
        (
            "Curso de Algoritmos - Curso em Vídeo",
            "https://www.youtube.com/watch?v=iF2MdbrTiBM"
        ),
        (
            "Lógica de Programação - Dev Aprender",
            "https://www.youtube.com/watch?v=8mei6uVttho"
        ),
        (
            "Introdução à Lógica de Programação",
            "https://www.youtube.com/watch?v=4p7axLXXBGU"
        )
    ],

    "SQL": [
        (
            "Curso em Vídeo - MySQL",
            "https://www.cursoemvideo.com/curso/mysql/"
        ),
        (
            "Curso SQL Completo",
            "https://www.youtube.com/watch?v=zSznqN754MY"
        ),
        (
            "SQL para Análise de Dados",
            "https://dados.pgdinamica.com/sql/aula0/"
        )
    ],

    "Estatística": [
        (
            "Estatística para Ciência de Dados",
            "https://www.youtube.com/watch?v=K_q6uCgV0Mk"
        ),
        (
            "Estatística Básica - USP",
            "https://eaulas.usp.br/portal/course.action?course=16775"
        ),
        (
            "Material Didático de Estatística - UFV",
            "https://lapea.ufv.br/sem-categoria-pt/material-didatico-cursos-tutoriais/"
        )
    ],

    "Banco de Dados": [
        (
            "Curso de Banco de Dados MySQL",
            "https://www.portalgsti.com.br/cursos/curso-de-banco-de-dados-mysql-gratuito/"
        ),
        (
            "Fundamentos de Banco de Dados",
            "https://www.webmundi.com/curso-banco-de-dados-sql-server-fundamentos/"
        ),
        (
            "Playlist de Banco de Dados",
            "https://programariscool.com.br/playlist"
        )
    ]
}

EXERCICIOS = {
    "Lógica de Programação": [
        ("Beecrowd","https://www.beecrowd.com.br/"),
        ("Neps Academy", "https://neps.academy/"),
        ("HackerRank Lógica de Programação", "https://www.hackerrank.com/")
    ],
    "SQL": [
        ("HackerRank SQL", "https://www.hackerrank.com/domains/sql"),
        ("LeetCode Database", "https://leetcode.com/problemset/database/"),
        ("SQL Practice", "https://www.sql-practice.com/")
    ],

    "Estatística": [
        ("Khan Academy", "https://pt.khanacademy.org/math/statistics-probability"),
        ("Exercícios USP", "https://www.ime.usp.br/~pam/bdados/exercicios.html"),
        ("W3Resource Statistics", "https://www.w3resource.com/statistics-exercises/")
    ],

    "Banco de Dados": [
        ("DB Fiddle", "https://www.db-fiddle.com/"),
        ("W3Resource SQL", "https://www.w3resource.com/sql-exercises/"),
        ("SQL Practice", "https://www.sql-practice.com/")
    ]
}

PDFS = [
    (
        "Introdução à Programação - UFSC",
        "https://arquivos.ufsc.br/programacao.pdf"
    ),
    (
        "Apostila SQL Básico",
        "https://www.devmedia.com.br/apostila-sql.pdf"
    ),
    (
        "Estatística Básica",
        "https://www.ime.usp.br/~pam/material.html"
    )
]

SITES_UTEIS = [
    (
        "W3Schools",
        "https://www.w3schools.com/"
    ),
    (
        "Khan Academy",
        "https://pt.khanacademy.org/"
    ),
    (
        "MDN Web Docs",
        "https://developer.mozilla.org/pt-BR/"
    )
]

FERRAMENTAS = [
    (
        "Visual Studio Code",
        "https://code.visualstudio.com/"
    ),
    (
        "MySQL Workbench",
        "https://www.mysql.com/products/workbench/"
    ),
    (
        "Draw.io",
        "https://app.diagrams.net/"
    )
]

MENU, ESTUDO, RECURSOS, MATERIA, SUGESTAO = range(5)

async def start(update, context):
    await update.message.reply_text(
            "Olá! Eu sou o Educo 🤖📚\n\n"
            "Seu assistente de estudos.\n\n"
            "Aqui você encontrará videoaulas, exercícios e recursos complementares para auxiliar sua aprendizagem.\n\n"
            "Escolha uma opção abaixo:",
        reply_markup=menu_principal()
    )
    return MENU

async def menu(update, context):
    texto = update.message.text

    if texto == "📚 Conteúdo para estudo":
        await update.message.reply_text(
            "Escolha a área que você quer estudar:",
            reply_markup=menu_estudo()
        )
        return ESTUDO

    elif texto == "📖 Recursos Extras":
        await update.message.reply_text(
            "Escolha o tipo:",
            reply_markup=menu_recursos()
        )
        return RECURSOS
    
    elif texto == "Sugestões":
        await update.message.reply_text(
            "💬 Escreva sua sugestão ou feedback:"
        )
        return SUGESTAO

async def estudo(update, context):
    texto = update.message.text

    if texto == "⬅️ Voltar":
        await update.message.reply_text(
            "Menu principal:",
            reply_markup=menu_principal()
        )
        return MENU

    if texto in ["Lógica de Programação", "SQL", "Estatística", "Banco de Dados"]:
        context.user_data["materia"] = texto

        await update.message.reply_text(
            f"📚 {texto}\n\nEscolha uma opção:",
            reply_markup=menu_materia()
        )

        return MATERIA

async def recursos(update, context):
    texto = update.message.text

    if texto == "⬅️ Voltar":
        await update.message.reply_text(
            "Menu principal:",
            reply_markup=menu_principal()
        )
        return MENU

    if texto == "📄 PDFs":

        mensagem = "📄 PDFs Recomendados\n\n"

        for i, (nome, link) in enumerate(PDFS, start=1):
            mensagem += f"{i}️⃣ {nome}\n{link}\n\n"

        await update.message.reply_text(mensagem)

    elif texto == "🌐 Sites Úteis":

        mensagem = "🌐 Sites Úteis\n\n"

        for i, (nome, link) in enumerate(SITES_UTEIS, start=1):
            mensagem += f"{i}️⃣ {nome}\n{link}\n\n"

        await update.message.reply_text(mensagem)

    elif texto == "🛠️ Ferramentas":

        mensagem = "🛠️ Ferramentas Recomendadas\n\n"

        for i, (nome, link) in enumerate(FERRAMENTAS, start=1):
            mensagem += f"{i}️⃣ {nome}\n{link}\n\n"

        await update.message.reply_text(mensagem)

    return RECURSOS

async def materia(update, context):
    texto = update.message.text
    materia = context.user_data.get("materia")

    if texto == "⬅️ Voltar":
        await update.message.reply_text(
            "Escolha uma área:",
            reply_markup=menu_estudo()
        )
        return ESTUDO

    if texto == "📹 Videoaulas":

        links = VIDEOAULAS.get(materia, [])

        mensagem = f"📹 Videoaulas de {materia}\n\n"

        for i, (nome, link) in enumerate(links, start=1):
            mensagem += f"{i}️⃣ {nome}\n{link}\n\n"

        await update.message.reply_text(mensagem)
    
    elif texto == "📝 Exercícios":

        links = EXERCICIOS.get(materia, [])

        mensagem = f"📝 Exercícios de {materia}\n\n"

        for i, (nome, link) in enumerate(links, start=1):
            mensagem += f"{i}️⃣ {nome}\n{link}\n\n"

        await update.message.reply_text(mensagem)

    return MATERIA

async def sugestao(update, context):

    texto = update.message.text

    with open(
        "sugestoes.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            update.effective_user.id,
            update.effective_user.first_name,
            texto
        ])

    await update.message.reply_text(
        "✅ Obrigado pela sua sugestão!\n\n"
        "Sua contribuição ajuda a melhorar o Educo. 📚🤖",
        reply_markup=menu_principal()
    )

    return MENU