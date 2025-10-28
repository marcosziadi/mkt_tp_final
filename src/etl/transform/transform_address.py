import pandas as pd

def clean_address(address_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    address_clean = address_raw.copy()

    try:
        return address_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'address' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROT: Failed cleaning 'address' | Unexpected error: {str(e)}") from e