import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "faq_suporte.csv")

os.makedirs(os.path.dirname(DATA_RAW_PATH), exist_ok=True)

linhas = [
    {
        "pergunta": "Como formatar meu PC?",
        "intencao": "formatacao",
        "resposta": "Para formatar seu PC siga os passos basicos de backup e reinstalacao do sistema"
    },
    {
        "pergunta": "Quero restaurar o PC para configuracoes de fabrica",
        "intencao": "formatacao",
        "resposta": "Use a opcao de restauracao do Windows nas configuracoes do sistema"
    },
    {
        "pergunta": "Meu Wi-Fi caiu",
        "intencao": "rede",
        "resposta": "Reinicie o modem e o roteador e confira os cabos de rede"
    },
    {
        "pergunta": "Nao consigo conectar na internet",
        "intencao": "rede",
        "resposta": "Verifique se o wifi esta ativado e se a senha foi digitada corretamente"
    },
    {
        "pergunta": "Como instalar o Google Chrome?",
        "intencao": "instalacao",
        "resposta": "Acesse o site oficial do Google Chrome e baixe o instalador"
    },
    {
        "pergunta": "Quero instalar o WhatsApp no PC",
        "intencao": "instalacao",
        "resposta": "Acesse o site do WhatsApp e baixe o aplicativo para computador"
    },
]

df = pd.DataFrame(linhas)
df.to_csv(DATA_RAW_PATH, index=False)

print("✔ Base gerada em:", DATA_RAW_PATH)
print(df)