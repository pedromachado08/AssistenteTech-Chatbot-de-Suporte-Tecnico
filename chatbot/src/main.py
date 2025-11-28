import joblib
import pandas as pd
import random

from .config import MODEL_PATH, DATA_RAW_PATH


def carregar_respostas():
    df = pd.read_csv(DATA_RAW_PATH)

    # agrupa todas as respostas por intenção
    respostas_por_intent = {}
    for _, row in df.iterrows():
        intent = row["intencao"]
        resp = row["resposta"]

        if intent not in respostas_por_intent:
            respostas_por_intent[intent] = []
        respostas_por_intent[intent].append(resp)

    return respostas_por_intent


def escolher_resposta(respostas_por_intent, intent):
    opcoes = respostas_por_intent.get(intent)
    if not opcoes:
        return "Ainda não tenho uma resposta certinha pra isso, mas posso tentar te orientar melhor se você detalhar um pouco mais."

    # escolhe uma resposta aleatória daquela intenção (se tiver mais de uma)
    base = random.choice(opcoes)

    # “embalagem” mais humana em volta da resposta
    iniciadores = [
        "Beleza, vamos por partes:",
        "Show, olha só:",
        "Tranquilo, o caminho é esse:",
        "Boa pergunta! Segue o passo a passo:",
        "Fechou, dá uma olhada nisso:"
    ]

    return f"{random.choice(iniciadores)}\n\n{base}"


def chat():
    model = joblib.load(MODEL_PATH)
    respostas_por_intent = carregar_respostas()

    print("🤖 AssistenteTech iniciado!")
    print("Pode mandar suas dúvidas de suporte (formatação, rede, instalação etc.).")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        pergunta = input("Você: ").strip()
        if not pergunta:
            continue

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("Bot: Fechou! Se precisar de mais alguma coisa é só chamar. 👋")
            break

        intent = model.predict([pergunta])[0]
        resposta = escolher_resposta(respostas_por_intent, intent)
        print(f"\nBot: {resposta}\n")


if __name__ == "__main__":
    chat()
