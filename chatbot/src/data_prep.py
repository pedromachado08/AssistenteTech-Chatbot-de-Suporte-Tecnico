import os
import pandas as pd
from .config import DATA_RAW_PATH, DATA_PROCESSED_PATH

def preparar():
    # Garante que o arquivo de dados existe
    if not os.path.exists(DATA_RAW_PATH):
        raise FileNotFoundError(f"Arquivo de dados não encontrado em: {DATA_RAW_PATH}")

    # Lê a base inteira
    df = pd.read_csv(DATA_RAW_PATH)

    # Aqui NÃO tem train_test_split. Vamos usar tudo como treino.
    X_train = df["pergunta"]
    y_train = df["intencao"]

    data = {
        "X_train": X_train,
        "X_test": X_train,   # gambiarra: usa o mesmo como teste só pra não quebrar o train.py
        "y_train": y_train,
        "y_test": y_train,
    }

    # Garante que a pasta existe
    os.makedirs(os.path.dirname(DATA_PROCESSED_PATH), exist_ok=True)

    # Salva o pickle
    pd.to_pickle(data, DATA_PROCESSED_PATH)

    print("✔ Dados processados e salvos em:", DATA_PROCESSED_PATH)
    print(f"   -> Total de amostras: {len(X_train)}")

if __name__ == "__main__":
    preparar()
