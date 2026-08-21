from google.cloud import bigquery
import pandas as pd
from pathlib import Path
from Storage import SaveParquet ,ReadParquet

def Main_Extract(project_id, PartionTime_init, PartionTime_end, Limit):
    df=Extract_bigquery(project_id, PartionTime_init, PartionTime_end, Limit)
    CountryEventsCodes()

    # Save parquet
    project_root = Path(__file__).resolve().parent.parent
    df_dir = project_root / "data" / "raw"/"extractRaw.parquet"
    SaveParquet(df, df_dir)
    print("Extracción exitosa")
    return 
def Extract_bigquery(project_id, PartionTime_init, PartionTime_end, Limit):

    """
    Extracts data from GDELT using BigQuery.

    Parameters:
        project_id (str): The Google Cloud project ID.
        PartionTime_init (str): The initial partition time for the query.
        PartionTime_end (str): The end partition time for the query.
        Limit (int): The limit of records to extract.

    Returns:
        pandas.DataFrame: The extracted data.
    """
    client = bigquery.Client(project=project_id)
    query = f"""
    SELECT
        GLOBALEVENTID,
        SQLDATE,
        Actor1Name,
        Actor2Name,

        EventCode,
        GoldsteinScale,
        AvgTone,
        NumMentions,

        ActionGeo_CountryCode,
        ActionGeo_Lat,
        ActionGeo_Long

    FROM `gdelt-bq.gdeltv2.events_partitioned`

    WHERE _PARTITIONTIME >= TIMESTAMP('{PartionTime_init}')
    AND _PARTITIONTIME < TIMESTAMP('{PartionTime_end}')
    AND ActionGeo_CountryCode IS NOT NULL
    ORDER BY GLOBALEVENTID

    LIMIT {Limit}
    """

    df = client.query(query).to_dataframe()
    print(f"Se han extraído {len(df)} registros de GDELT.")
    return df




def CountryEventsCodes():

    """
    Load and prepare GDELT country and event reference codes.
    """

    project_root = Path(__file__).resolve().parent.parent

    reference_dir = project_root / "data" / "reference"
    source_dir = project_root / "data" / "CountryAndEventCodes"

    event_path = reference_dir / "event_codes.parquet"
    country_path = reference_dir / "country_codes.parquet"

    # Si las referencias ya existen, las cargamos
    if event_path.exists() and country_path.exists():

        return 

    # -------------------------
    # Eventos
    # -------------------------

    events = pd.read_csv(
        source_dir / "CAMEO_eventcodes.txt",
        sep="\t"
    )

    events["CAMEOEVENTCODE"] = (
        events["CAMEOEVENTCODE"]
        .astype(str)
        .str.zfill(4)
    )

    events = events.rename(
        columns={
            "CAMEOEVENTCODE": "EventCode"
        }
    )

    country = pd.read_csv(
        source_dir / "FIPS_country.txt",
        sep="\t",
        header=None,
        names=[
            "ActionGeo_CountryCode",
            "CountryName"
        ]
    )

    # Guardar referencias

    SaveParquet(events,event_path)

    SaveParquet(country,country_path)

    return 