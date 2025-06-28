print("src/train.py foi carregado")

from sklearn.model_selection import train_test_split

def split_data(df, target="target"):
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, shuffle=False)