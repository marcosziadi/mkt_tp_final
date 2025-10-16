import pandas as pd

CUSTOMER_UNKNOWN_ID = -1
DATETIME_UNKNOWN = '1900-01-01 00:00:00'

def clean_web_session(web_session_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    Cleaning of web_session.csv.
    '''
    
    web_session_clean = web_session_raw.copy()

    try:
        web_session_clean['started_at'] = pd.to_datetime(web_session_clean['started_at']).dt.floor('min')
        web_session_clean['ended_at'] = pd.to_datetime(web_session_clean['ended_at']).dt.floor('min')

        web_session_clean['ended_at'] = web_session_clean['ended_at'].fillna(DATETIME_UNKNOWN)
        web_session_clean['customer_id'] = web_session_clean['customer_id'].fillna(CUSTOMER_UNKNOWN_ID)
        
        web_session_clean['duration_sec'] = (web_session_clean['ended_at'] - web_session_clean['started_at']).dt.total_seconds()
        web_session_clean.loc[web_session_clean['ended_at' == DATETIME_UNKNOWN], 'duration_sec'] = -1
    
    except Exception as e:
        raise IOError('Failed cleaning web_session.csv')
    
    return web_session_clean