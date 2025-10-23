import pandas as pd

def build_dim_product(product_clean: pd.DataFrame, product_category_clean: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''
    dim_product = (
        product_clean
        .merge(product_category_clean,
            on='category_id',
            how='left',
            suffixes=['','_category'])
        .rename(columns={'name_category':'category_name',
                        'parent_name':'category_parent_name'})
        .drop(columns=['category_id']))

    dim_product = dim_product.reset_index(drop=True)
    dim_product['product_sk'] = dim_product.index + 1

    dim_product = (
        dim_product[[
            'product_sk',
            'product_id',
            'sku',
            'name',
            'list_price',
            'status',
            'created_at',
            'category_name',
            'category_parent_name'
        ]])

    return dim_product