# Imports usados no bot
from telegram.ext import ConversationHandler
from menus import *
import csv
# Banco de Conteúdos

VIDEOAULAS = {
    "Lógica de Programação": [
        (
            "Curso de Algoritmos - Curso em Vídeo",
            "Introdução aos algoritmos e ao raciocínio lógico.",
            "https://www.youtube.com/watch?v=iF2MdbrTiBM"
        ),
        (
            "Lógica de Programação - Dev Aprender",
            "Conceitos fundamentais para quem está começando a programar.",
            "https://www.youtube.com/watch?v=8mei6uVttho"
        ),
        (
            "Introdução à Lógica de Programação",
            "Apresentação dos princípios básicos da lógica de programação.",
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
        (
            "Beecrowd",
            "Plataforma para praticar resolução de problemas e desenvolver o raciocínio lógico.",
            "https://www.beecrowd.com.br/"
        ),
        (
            "Neps Academy",
            "Ambiente de aprendizagem com exercícios de programação e algoritmos.",
            "https://neps.academy/"
        ),
        (
            "HackerRank Lógica de Programação",
            "Plataforma de desafios para desenvolver habilidades de programação.",
            "https://www.hackerrank.com/"
        )
    ],

    "SQL": [
    (
        "HackerRank SQL",
        "Plataforma de desafios práticos para desenvolver conhecimentos em consultas SQL.",
        "https://www.hackerrank.com/domains/sql"
    ),
    (
        "LeetCode Database",
        "Exercícios para praticar consultas, manipulação e resolução de problemas com bancos de dados.",
        "https://leetcode.com/problemset/database/"
    ),
    (
        "SQL Practice",
        "Ambiente interativo para praticar comandos SQL e desenvolver habilidades com consultas.",
        "https://www.sql-practice.com/"
    )
],

    "Estatística": [
    (
        "Khan Academy",
        "Conteúdos e exercícios interativos sobre probabilidade, estatística e interpretação de dados.",
        "https://pt.khanacademy.org/math/statistics-probability"
    ),
    (
        "Exercícios USP",
        "Material de apoio com exercícios para praticar conceitos estatísticos.",
        "https://www.ime.usp.br/~pam/bdados/exercicios.html"
    ),
    (
        "W3Resource Statistics",
        "Exercícios práticos para desenvolver conhecimentos em estatística e análise de dados.",
        "https://www.w3resource.com/statistics-exercises/"
    )
],

    "Banco de Dados": [
    (
        "DB Fiddle",
        "Ferramenta online para criar bancos de dados e testar consultas SQL em diferentes ambientes.",
        "https://www.db-fiddle.com/"
    ),
    (
        "W3Resource SQL",
        "Coleção de exercícios para praticar comandos SQL e desenvolver habilidades com bancos de dados.",
        "https://www.w3resource.com/sql-exercises/"
    ),
    (
        "SQL Practice",
        "Plataforma interativa para praticar consultas e operações em bancos de dados.",
        "https://www.sql-practice.com/"
    )
]
}


PDFS = {
    "Lógica de Programação": [
    (
        "Introdução à Programação - UFSC",
        "Material de apoio para estudar conceitos fundamentais de programação e lógica.",
        "https://arquivos.ufsc.br/programacao.pdf"
    )
],

    "SQL": [
        (
            "Apostila SQL Básico",
            "Material de apoio para estudar conceitos fundamentais de SQL.",
            "https://www.devmedia.com.br/apostila-sql.pdf"
        )
    ],

    "Estatística": [
        (
            "Estatística Básica - USP",
            "Material de apoio para estudar conceitos fundamentais de estatística.",
            "https://www.ime.usp.br/~pam/material.html"
        )
    ],

    "Banco de Dados": [
        (
            "Materiais de apoio - Banco de Dados",
            "Material de apoio para estudar conceitos fundamentais de bancos de dados.",
            "https://www.ime.usp.br/~pam/material.html"
        )
    ]
}
PDFS = {
    "Lógica de Programação": [
    (
        "Introdução à Programação - UFSC",
        "Material de apoio para estudar conceitos fundamentais de programação e lógica.",
        "https://arquivos.ufsc.br/programacao.pdf"
    )
],

    "SQL": [
    (
        "Apostila SQL Básico",
        "Material de apoio para aprender os fundamentos da linguagem SQL e praticar consultas em bancos de dados.",
        "https://www.devmedia.com.br/apostila-sql.pdf"
    )
],

    "Estatística": [
    (
        "Estatística Básica - USP",
        "Material de apoio para compreender conceitos fundamentais de estatística e desenvolver a interpretação de dados.",
        "https://www.ime.usp.br/~pam/material.html"
    )
],

    "Banco de Dados": [
    (
        "Materiais de apoio - Banco de Dados",
        "Material complementar para revisar conceitos de bancos de dados e apoiar os estudos sobre organização e consulta de informações.",
        "https://www.ime.usp.br/~pam/material.html"
    )
]

}

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

# Atualizado 11/11/2026 - Nova apresentação do bot com informações detalhadas sobre o Educo e suas funcionalidades.
async def start(update, context):
    await update.message.reply_text(
        "Olá! Seja bem-vindo(a) ao Educo! 🤖📚\n\n"
        "Sou um assistente educacional desenvolvido para "
        "facilitar o acesso a materiais de estudo e apoiar "
        "estudantes da modalidade EAD.\n\n"

        "📚 O que você encontra por aqui?\n\n"
        "• Lógica de Programação\n"
        "• SQL\n"
        "• Banco de Dados\n"
        "• Estatística\n\n"

        "📖 Você também pode acessar recursos complementares, "
        "como PDFs, sites úteis e ferramentas de apoio.\n\n"

        "💡 Tem alguma ideia ou sugestão? Utilize a opção "
        "'Sugestões' para contribuir com a melhoria do Educo.\n\n"

        "Para começar, escolha uma opção no menu abaixo. "
        "Você poderá voltar ao menu principal sempre que precisar.\n\n"

        "Bons estudos! 🚀",
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

        for disciplina, materiais in PDFS.items():
            mensagem += f"📚 {disciplina}\n"

            for i, item in enumerate(materiais, start=1):
                if len(item) == 3:
                    nome, descricao, link = item
                    mensagem += (
                        f"{i}️⃣ {nome}\n"
                        f"ℹ️ {descricao}\n"
                        f"🔗 {link}\n\n"
                    )
                else:
                    nome, link = item
                    mensagem += (
                        f"{i}️⃣ {nome}\n"
                        f"🔗 {link}\n\n"
                    )

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

    elif texto == "📝 Exercícios":
        links = EXERCICIOS.get(materia, [])
        mensagem = f"📝 Exercícios de {materia}\n\n"

    elif texto == "📚 Materiais Complementares":
        links = PDFS.get(materia, [])
        mensagem = f"📚 Materiais Complementares de {materia}\n\n"

    else:
        return MATERIA

    if not links:
        mensagem += "Ainda não há materiais cadastrados para esta disciplina."
    else:
        for i, item in enumerate(links, start=1):

            if len(item) == 3:
                nome, descricao, link = item
                mensagem += (
                    f"{i}️⃣ {nome}\n"
                    f"ℹ️ {descricao}\n"
                    f"🔗 {link}\n\n"
                )

            else:
                nome, link = item
                mensagem += (
                    f"{i}️⃣ {nome}\n"
                    f"🔗 {link}\n\n"
                )

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