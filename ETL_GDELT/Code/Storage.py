from pathlib import Path
import pandas as pd


def SaveParquet(df, path):
    
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(path, index=False)

    print(f"Guardado con éxito en : {path}")


def ReadParquet(path):
    print(f"Leyendo {path}")

    return pd.read_parquet(path)