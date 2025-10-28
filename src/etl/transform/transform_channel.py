import pandas as pd

def clean_channel(channel_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''
    channel_clean = channel_raw.copy()
    
    try:
        return channel_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'channel' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'channel' | Unexpected error: {str(e)}") from e