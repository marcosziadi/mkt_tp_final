import pandas as pd

def clean_product(product_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    product_clean = product_raw.copy()

    try:
        product_clean['created_at'] = pd.to_datetime(product_clean['created_at']).dt.floor('min')
        return product_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'product_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'product_raw' | Unexpected error: {str(e)}") from e