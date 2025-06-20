Predição de Temperatura Média Diária com Regressão Supervisionada

Este projeto tem como objetivo explorar a aplicação de algoritmos de regressão supervisionada na predição da temperatura média diária com base em dados meteorológicos do INMET. Ele faz parte de um cronograma prático de estudos em modelagem climática com machine learning.

🎯 Objetivo

Comparar diferentes modelos de regressão na tarefa de prever a temperatura média do dia seguinte, com base em dados meteorológicos (pressão, umidade, temperatura mínima/máxima, vento, precipitação, etc.).

📦 Dados

- Fonte: Instituto Nacional de Meteorologia (INMET)
- Frequência: Diária
- Local: Estações meteorológicas no Brasil (ex.: Florianópolis ou região Sudeste)
- Período: Aproximadamente 5 anos
- Formato: CSV ou coletado via API pública do INMET

📁 Estrutura

predicting-temperature/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_modelagem_baseline.ipynb
│   ├── 03_comparacao_modelos.ipynb
├── src/
│   ├── data.py           # funções para carregar/preprocessar dados
│   ├── train.py          # função principal de treinamento
│   ├── predict.py        # função de predição com novo dado
│   ├── metrics.py        # funções de avaliação
│   └── utils.py          # funções auxiliares
├── scripts/              # scripts prontos para execução em terminal
│   ├── train_model.py
│   └── predict_model.py
├── data/
│   └── raw/              # dados originais
│   └── processed/        # dados processados
├── outputs/
│   ├── figures/
│   └── models/
├── environment.yml       # dependências Conda
├── .gitignore
└── README.md             # documentação do projeto



⚙️ Ambiente

Crie o ambiente Conda com:

```bash
conda env create -f environment.yml
conda activate clima
```

📊 Modelos testados

Regressão Linear

K-Nearest Neighbors Regressor

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting (XGBoost)

Regressão por Vetores de Suporte (SVR)

🧪 Metodologia

Validação cruzada (K-Fold)

Engenharia de features temporais (lags, rolling means)

Avaliação com métricas:

RMSE (Root Mean Squared Error)

MAE (Mean Absolute Error)

R² Score

📌 Aprendizados esperados

Impacto de diferentes algoritmos em uma tarefa real de regressão

Como interpretar métricas e comportamento dos modelos

Como preparar e transformar dados temporais para predição

Fundamentos da regularização, overfitting e ajuste de hiperparâmetros

📚 Licença

Código sob a licença MIT. Dados meteorológicos são públicos e devem respeitar os termos de uso do INMET.
