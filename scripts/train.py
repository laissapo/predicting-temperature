import sys
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression


# Adiciona a raiz do projeto ao sys.path
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

print(sys.path)  # <== imprime para ver se o path foi adicionado

from src.features import build_features
from src.data import load_raw_nasa
from src.train import split_data
from src.models import train_model, evaluate_model



def main():
    print("🔄 Carregando dados brutos...")
    df = load_raw_nasa()

    print("🔧 Aplicando engenharia de features...")
    df = build_features(df)

    print("✂️ Separando treino e teste...")
    X_train, X_test, y_train, y_test = split_data(df)

    print("✅ Conjuntos criados:")
    print(f"🔹 X_train: {X_train.shape}")
    print(f"🔹 X_test:  {X_test.shape}")
    print(f"🔹 y_train: {y_train.shape}")
    print(f"🔹 y_test:  {y_test.shape}")

    print("🤖 Treinando modelo...")
    model = train_model(LinearRegression(), X_train, y_train)


    print("📊 Avaliando modelo...")
    metrics = evaluate_model(model, X_test, y_test)
    print(f"MAE: {metrics['MAE']:.2f}")
    print(f"RMSE: {metrics['RMSE']:.2f}")
    print(f"R²: {metrics['R2']:.2f}")

if __name__ == "__main__":
    main()

