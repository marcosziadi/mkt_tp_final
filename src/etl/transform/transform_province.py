import pandas as pd

def clean_province(province_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    province_clean = province_raw.copy()
    try:
        return province_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'province_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'province_raw' | Unexpected error: {str(e)}") from e