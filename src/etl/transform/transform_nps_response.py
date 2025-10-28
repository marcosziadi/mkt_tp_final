import pandas as pd

def clean_nps_response(nps_response_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''
    nps_response_clean = nps_response_raw.copy()
    
    try:
        nps_response_clean['responded_at'] = pd.to_datetime(nps_response_clean['responded_at']).dt.floor('min')
        nps_response_clean['responded_at_int'] = nps_response_clean['responded_at'].dt.strftime('%Y%m%d%H%M').astype(int)
        return nps_response_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'nps_response_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'nps_response_raw' | Unexpected error: {str(e)}") from e