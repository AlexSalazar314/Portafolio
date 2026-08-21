import pandas as pd
from Storage import ReadParquet, SaveParquet
from pathlib import Path


def transform_data():
    """
    Transforms the extracted GDELT data.
        
    """

    project_root = Path(__file__).resolve().parent.parent
    
    reference_dir = project_root / "data" / "reference"
    
    event_path = reference_dir / "event_codes.parquet"
    country_path = reference_dir / "country_codes.parquet"
    df_transform_path=project_root / "data" /"raw"/"extractRaw.parquet"
    events = ReadParquet(event_path)
    country = ReadParquet(country_path)

    df=ReadParquet(df_transform_path)
    # Convert SQLDATE to datetime
    df['SQLDATE'] = pd.to_datetime(df['SQLDATE'], format='%Y%m%d')

    # Change format of date to YYYY-MM-DD
    df['SQLDATE'] = df['SQLDATE'].dt.strftime('%Y-%m-%d')
    # Handle missing values
    df.fillna({'Actor1Name': 'Unknown', 'Actor2Name': 'Unknown'}, inplace=True)

    df=MergeCountryEvents(df,events,country)
    SaveParquet(df,project_root / "data" /"raw"/"transformRaw.parquet")

    return 



def MergeCountryEvents(df,events,country):
    """""
    Function to add country and events information con dataframe

    Parameters: 
    df: dataframe
    events: dataframe with information of the events in the news

    """""


    
    #df["EventCode"]= df["EventCode"].astype(str).str.zfill(4) 
    df = df.merge(
        events,
        on="EventCode",
        how="left"
        )

    df=df.merge(
        country,
        on="ActionGeo_CountryCode",
        how="left"
        )

    return df