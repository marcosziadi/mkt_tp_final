import pandas as pd
import numpy as np

CUSTOMER_UNKNOWN_ID = -1
DATETIME_UNKNOWN_OBJ = '1900-01-01 00:00:00'

def clean_web_session(web_session_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    Cleaning of web_session.csv.
    '''
    
    web_session_clean = web_session_raw.copy()

    try:
        web_session_clean['started_at'] = pd.to_datetime(web_session_clean['started_at']).dt.floor('min')
        web_session_clean['ended_at'] = (
            pd.to_datetime(web_session_clean['ended_at'])
            .dt.floor('min')
            .fillna(str(DATETIME_UNKNOWN_OBJ))
        )

        web_session_clean['customer_id'] = web_session_clean['customer_id'].fillna(CUSTOMER_UNKNOWN_ID)

        web_session_clean['started_at_int'] = (
            web_session_clean['started_at']
            .fillna(str(DATETIME_UNKNOWN_OBJ))
            .dt.strftime("%Y%m%d%H%M")
            .astype(int)
        )

        web_session_clean['ended_at_int'] = (
            web_session_clean['ended_at']
            .fillna(str(DATETIME_UNKNOWN_OBJ))
            .dt.strftime("%Y%m%d%H%M")
            .astype(int)
        )

        duration_seconds = (web_session_clean['ended_at'] - web_session_clean['started_at']).dt.total_seconds()
        web_session_clean['duration_sec'] = np.where(duration_seconds < 0, -1, duration_seconds)
                
        return web_session_clean

    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning web_session.csv | Missing required column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed cleaning web_session.csv | Unexpected Error: {e}") from e  