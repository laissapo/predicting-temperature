import pandas as pd

def clean_and_rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove espaços dos nomes de colunas e renomeia colunas relevantes.
    """
    df = df.copy()
    df.columns = df.columns.str.strip()
    return df.rename(columns={
        'YEAR': 'year',
        'DOY': 'day_of_year',
        'T2M': 'temperature',
        'RH2M': 'humidity',
        'PRECTOTCORR': 'precipitation',
        'WS2M': 'wind_speed',
        'ALLSKY_SFC_SW_DWN': 'irradiance'
    })


def add_date_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria a coluna 'date' a partir de 'year' e 'day_of_year' e define como índice.
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["year"].astype(str), format="%Y") + pd.to_timedelta(df["day_of_year"] - 1, unit="D")
    df = df.set_index("date")
    return df


def convert_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converte todas as colunas para numérico, forçando valores inválidos para NaN.
    """
    return df.apply(pd.to_numeric, errors="coerce")


def add_temporal_variables(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona variáveis de tempo derivadas da data.
    """
    df = df.copy()
    df["month"] = df.index.month
    return df


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona defasagens (lags) da temperatura.
    """
    df = df.copy()
    df['temperature_lag1'] = df['temperature'].shift(1)
    df['temperature_lag3'] = df['temperature'].shift(3)
    df['temperature_lag7'] = df['temperature'].shift(7)
    return df


def add_rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona médias e somas móveis de variáveis climáticas.
    """
    df = df.copy()
    df['temperature_roll3'] = df['temperature'].rolling(window=3).mean()
    df['humidity_roll3'] = df['humidity'].rolling(window=3).mean()
    df['precipitation_roll7'] = df['precipitation'].rolling(window=7).sum()
    return df

def add_target_variable(df: pd.DataFrame, target_col: str = 'temperature') -> pd.DataFrame:
    """
    Adiciona a variável alvo (target) como a temperatura do dia seguinte.
    """
    df = df.copy()
    df['target'] = df[target_col].shift(-1)
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todas as etapas de limpeza e criação de features, compondo as funções anteriores, e remove linhas com valores NaN
    """
    df = clean_and_rename_columns(df)
    df = add_date_index(df)
    df = convert_to_numeric(df)
    df = add_temporal_variables(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    df = add_target_variable(df)
    df = df.dropna(axis=0, how='any')
    return df
