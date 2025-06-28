import pandas as pd

def load_raw_nasa(path="data/raw/nasa_rio_vermelho.csv") -> pd.DataFrame:
    return pd.read_csv(path, skiprows=26, sep=",", encoding="utf-8", engine="python")
