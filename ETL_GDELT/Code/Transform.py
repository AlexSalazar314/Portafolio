import pandas as pd

def transform_data(df,events,country):
    """
    Transforms the extracted GDELT data.

    Parameters:
        df (pandas.DataFrame): The extracted data.

    Returns:
        pandas.DataFrame: The transformed data.
    """
    # Convert SQLDATE to datetime
    df['SQLDATE'] = pd.to_datetime(df['SQLDATE'], format='%Y%m%d')

    # Change format of date to YYYY-MM-DD
    df['SQLDATE'] = df['SQLDATE'].dt.strftime('%Y-%m-%d')
    # Handle missing values
    df.fillna({'Actor1Name': 'Unknown', 'Actor2Name': 'Unknown'}, inplace=True)

    df=MergeCountryEvents(df,events,country)

    return df



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