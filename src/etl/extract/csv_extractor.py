import pandas as pd
from pathlib import Path

class CSVExtractor:

    def __init__(self):
        pass

    def load_csv(self, file_path: Path) -> pd.DataFrame:
        """
        CSV file reader.
        """

        try:
            df = pd.read_csv(file_path)

        except FileNotFoundError:
            raise FileNotFoundError(f"File in {file_path} does not exist.")
        except Exception as e:
            raise RuntimeError(f"Failed to read CSV file '{file_path}': {type(e).__name__}: {e}") from e
        
        return df

    def read_all_csv_files(self, dir_path) -> dict:
        """
        Reads all CSV files from a specific directory.
        """

        dataframes = {}

        for file_path in dir_path.glob("*.csv"):
            table_name = file_path.stem
            try:
                df = self.load_csv(file_path)
                dataframes[table_name] = df
            except Exception as e:
                raise RuntimeError(f"Failed to read CSV file '{file_path}' in directory '{dir_path}': {e}") from e

        return dataframes