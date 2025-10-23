import pandas as pd

def clean_nps_response(nps_response_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    nps_response_clean = nps_response_raw.copy()

    nps_response_clean['responded_at'] = pd.to_datetime(nps_response_clean['responded_at']).dt.floor('min')
    nps_response_clean['responded_at_int'] = nps_response_clean['responded_at'].dt.strftime('%Y%m%d%H%M').astype(int)

    return nps_response_clean