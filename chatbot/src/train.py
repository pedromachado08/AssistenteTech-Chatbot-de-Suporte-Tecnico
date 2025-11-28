import os
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression  # pode trocar por outro depois

from .config import DATA_PROCESSED_PATH, MODEL_PATH


def treinar():
    # Carrega o dicionário salvo no data_prep
    if not os.path.exists(DATA_PROCESSED_PATH):
        raise FileNotFoundError(f"Arquivo de dados processados não encontrado em: {DATA_PROCESSED_PATH}")

    data = pd.read_pickle(DATA_PROCESSED_PATH)

    X_train = data["X_train"]
    y_train = data["y_train"]

    # Pipeline: texto -> TF-IDF -> Modelo de classificação
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1500))
    ])

    print("🔧 Treinando modelo...")
    model.fit(X_train, y_train)

    # Garante que a pasta models/ existe
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    # Salva o pipeline completo (tfidf + modelo)
    joblib.dump(model, MODEL_PATH)
    print("✔ Modelo treinado e salvo em:", MODEL_PATH)


if __name__ == "__main__":
    treinar()
