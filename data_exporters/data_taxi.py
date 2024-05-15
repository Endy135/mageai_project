from pandas import DataFrame
from mageio import FileIO

def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    # Export DataFrame to CSV locally
    local_filepath = 'C:\Users\Utilisateur\Documents\Stage_orange\mageAi\data.csv'
    df.to_csv(local_filepath, index=False)

    # Upload the CSV file to MageAI
   # remote_filepath = 'to.csv'  # Adjust the remote filepath as needed
   # FileIO().upload(local_filepath, remote_filepath)