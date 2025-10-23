import pandas as pd

def clean_channel(channel_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    channel_clean = channel_raw.copy()
    return channel_clean