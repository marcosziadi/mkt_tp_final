import pandas as pd

def clean_store(store_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''
    
    store_clean = store_raw.copy()

    try:
        return store_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'store_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'store_raw' | Unexpected error: {str(e)}") from e