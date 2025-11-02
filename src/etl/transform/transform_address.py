import pandas as pd

LINE2_UNKNOWN = -1

def clean_address(address_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    address_clean = address_raw.copy()

    address_clean['line2'] =     address_clean['line2'].fillna(LINE2_UNKNOWN)
    try:
        return address_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'address' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROT: Failed cleaning 'address' | Unexpected error: {str(e)}") from e