import pandas as pd

def build_dim_device(web_session_clean_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Creates device dimension.
    '''

    dim_device = pd.DataFrame()

    try:
        dim_device['name'] = web_session_clean_df['device'].unique()
        dim_device['device_id'] = dim_device.index + 1
        dim_device = dim_device[['device_id','name']].copy()
        return dim_device

    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed creating dim_device | Missing required column: {e}") from e

    except Exception as e:
        raise RuntimeError(f"ERROR: Failed creating dim_device | Unexpected Error: {e}") from e