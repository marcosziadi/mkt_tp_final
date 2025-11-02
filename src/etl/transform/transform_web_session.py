import pandas as pd
import numpy as np

CUSTOMER_UNKNOWN_ID = -1
DATETIME_UNKNOWN_OBJ = '-1'

def clean_web_session(web_session_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    Cleaning of web_session.csv.
    '''
    
    web_session_clean = web_session_raw.copy()

    try:
        web_session_clean['started_at_int'] = (
            pd.to_datetime(web_session_clean['started_at'])
            .dt.strftime('%Y%m%d%H%M')
            .fillna(DATETIME_UNKNOWN_OBJ)
            .astype(int))

        web_session_clean['ended_at_int'] = (
            pd.to_datetime(web_session_clean['ended_at'])
            .dt.strftime('%Y%m%d%H%M')
            .fillna(DATETIME_UNKNOWN_OBJ)
            .astype(int))

        web_session_clean['customer_id'] = web_session_clean['customer_id'].fillna(CUSTOMER_UNKNOWN_ID)
                
        return web_session_clean

    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning web_session.csv | Missing required column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed cleaning web_session.csv | Unexpected Error: {e}") from e  