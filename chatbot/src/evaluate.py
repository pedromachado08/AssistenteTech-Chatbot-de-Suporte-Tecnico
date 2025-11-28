import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from .config import MODEL_PATH, DATA_PROCESSED_PATH


def avaliar():
    # Carrega o modelo
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em: {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    # Carrega os dados processados
    if not os.path.exists(DATA_PROCESSED_PATH):
        raise FileNotFoundError(f"Dados processados não encontrados em: {DATA_PROCESSED_PATH}")

    data = pd.read_pickle(DATA_PROCESSED_PATH)

    X_test = data["X_test"]
    y_test = data["y_test"]

    # Predições
    y_pred = model.predict(X_test)

    # Criar pastas finais
    os.makedirs("reports/figures", exist_ok=True)

    # --------------------------------------------------
    # 1. Acurácia
    # --------------------------------------------------
    acc = accuracy_score(y_test, y_pred)
    print(f"\n✔ Acurácia: {acc:.2f}")

    # --------------------------------------------------
    # 2. Classification Report
    # --------------------------------------------------
    report = classification_report(y_test, y_pred)
    print("\n✔ Relatório de Classificação:\n")
    print(report)

    with open("reports/classification_report.txt", "w") as f:
        f.write(report)

    # --------------------------------------------------
    # 3. Matriz de Confusão (gráfico)
    # --------------------------------------------------
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Purples")
    plt.xlabel("Predito")
    plt.ylabel("Real")
    plt.title("Matriz de Confusão")
    plt.tight_layout()
    plt.savefig("reports/figures/confusion_matrix.png")
    plt.close()

    # --------------------------------------------------
    # 4. Distribuição das Classes Reais
    # --------------------------------------------------
    plt.figure(figsize=(6, 4))
    sns.countplot(x=y_test, palette="Purples")
    plt.title("Distribuição das Classes (Reais)")
    plt.tight_layout()
    plt.savefig("reports/figures/class_distribution.png")
    plt.close()

    # --------------------------------------------------
    # 5. Distribuição das Predições
    # --------------------------------------------------
    resultado = pd.DataFrame({
        "Real": y_test,
        "Predito": y_pred
    })

    plt.figure(figsize=(6, 4))
    sns.countplot(x=resultado["Predito"], palette="Purples")
    plt.title("Distribuição das Predições")
    plt.tight_layout()
    plt.savefig("reports/figures/prediction_distribution.png")
    plt.close()

    # Salvar CSV com real x predito
    resultado.to_csv("reports/resultados.csv", index=False)

    print("\n✔ Todos os gráficos e relatórios foram gerados!")
    print("📁 reports/figures/")
    print("📄 reports/classification_report.txt")
    print("📄 reports/resultados.csv")
    print("\nAvaliação concluída com sucesso! 🔥")


if __name__ == "__main__":
    avaliar()
