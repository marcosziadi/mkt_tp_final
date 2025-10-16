import pandas as pd
import pathlib as Path

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
            raise FileNotFoundError(f"File in {file_path} does not exists.")
        
        except Exception as e:
            raise IOError(f"Failed to read {file_path}: {str(e)}")
        
        return df

    def read_all_csv_files(self, dir_path) -> dict:
        """
        Reads all CSV files from a specific directory.
        """

        dataframes = {}
        
        try:
            for file_path in dir_path.glob("*.csv"):
                table_name = file_path.stem
                df = self.load_csv(file_path)
                dataframes[table_name] = df
        
        except Exception as e:
            raise IOError(f"{str(e)}")

        return dataframes