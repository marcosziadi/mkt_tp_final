import pandas as pd

def clean_product_category(product_category_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    product_category_clean = (
        product_category_raw
        .merge(product_category_raw[['category_id','name']].add_prefix("parent_"),
               left_on='parent_id',
               right_on='parent_category_id',
               how="left")
        .drop(columns=['parent_id','parent_category_id']))
    
    return product_category_clean