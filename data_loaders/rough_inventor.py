import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/yash-chauhan-dev/test_data/raw/main/yellow_tripdata_2021-01.csv.gz'
    
    taxi_dtypes = {
        'VendarID': pd.Int64Dtype(),
        'passenger count': pd.Int64Dtype(),
        'trip distance': float, 
        "RatecodeID": pd.Int64Dtype(),
        'store and fwd flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        "payment type": pd.Int64Dtype(),
        "fare acount": float,
        'estra': float,
        "ota tax": float, 
        "tip amount": float,
        'tolls amount': float,
        "improvement surcharge's": float,
        "total amount": float,
        'congestion surcharge': float
    }
    
    parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

    
    #response = requests.get(url)

    return pd.read_csv(url, sep = ',', compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
