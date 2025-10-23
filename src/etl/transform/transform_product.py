import pandas as pd

def clean_product(product_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    product_clean = product_raw.copy()

    product_clean['created_at'] = pd.to_datetime(product_clean['created_at']).dt.floor('min')
    return product_clean