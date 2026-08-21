import pandas as pd
from google.cloud import bigquery
from pathlib import Path

def MainLoad( df,project_id,filename="events",carpeta="data",dataset_id="gdelt_pipeline",table="events",bigquery=False,save=True):
    table_id=f"{project_id}.{dataset_id}.{table}"
    if bigquery:
        CreateDataset(project_id,dataset_id)
        LoadBigquery(df,table_id)
    if save:
        SaveParquet(df,filename,carpeta)



def LoadBigquery(df,table_id):

    """""
    Function to 
    """""
    print("Inicializando carga.....")
    client = bigquery.Client()

    job = client.load_table_from_dataframe(
        df,
        table_id
    )

    job.result()

    print(f"Datos cargados en: {table_id}")

def CreateDataset(project_id,dataset_id="gdelt_pipeline"):

    client = bigquery.Client()

    dataset = bigquery.Dataset(f"{project_id}.{dataset_id}")
    dataset.location = "US"

    client.create_dataset(
        dataset,
        exists_ok=True
    )


def SaveParquet(df, filename="events", carpeta="data"):
    print("Creando carpeta...")
    # Finding root
    project_root = Path(__file__).resolve().parent.parent
    carpeta = project_root / carpeta
    carpeta.mkdir(parents=True, exist_ok=True)

    path = carpeta / f"{filename}.parquet"

    print("Guardando datos en local...")

    df.to_parquet(path, index=False)

    print(f"Guardado con éxito como: {path}")
