import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    params=None
    headers=None

    url = "https://airqino-api.magentalab.it/v3/getStationHourlyAvg/283164601"

    """
    Loads data from API and returns a pandas DataFrame.
    
    Parameters:
    url (str): The API endpoint URL.
    params (dict): The URL parameters to be sent with the API request (default is None).
    headers (dict): The headers to be sent with the API request (default is None).
    
    Returns:
    pd.DataFrame: DataFrame containing the data from the API response.
    """
    # Define data types for the columns
    station_dtypes = {
        'CO': float,
        'T': float,
        'T. int.': float,
        'NO2': float,
        'O3': float,
        'PM10': float,
        'PM2.5': float,
        'RH': float
    }
    
    parse_dates = ["timestamp"]
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        json_data = response.json()
        
        data = json_data['data']
        
        df = pd.DataFrame(data)
        
        for col, dtype in station_dtypes.items():
            if col in df.columns:
                df[col] = df[col].astype(dtype)
        
        for date_col in parse_dates:
            if date_col in df.columns:
                df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        
        return df
    else:
        response.raise_for_status() 


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
