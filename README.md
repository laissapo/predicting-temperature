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

- `data/raw/`: dados brutos da estação meteorológica
- `data/processed/`: dados tratados e com variáveis preditoras criadas
- `notebooks/01_EDA.ipynb`: análise exploratória e visualizações
- `notebooks/02_regression_models.ipynb`: comparação entre modelos
- `src/`: funções auxiliares para limpeza, engenharia de features e avaliação
- `outputs/`: gráficos, métricas, modelos salvos
- `README.md`: documentação do projeto
- `environment.yml`: dependências Conda

⚙️ Ambiente

Crie o ambiente Conda com:

```bash
conda env create -f environment.yml
conda activate clima
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