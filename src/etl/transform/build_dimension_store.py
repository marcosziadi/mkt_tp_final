import pandas as pd

def build_dim_store(
    store_clean: pd.DataFrame,
    address_clean: pd.DataFrame,
    province_clean: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    dim_store = (
        store_clean
        .merge(address_clean, on='address_id', how='inner')
        .merge(province_clean, on='province_id', how='inner', suffixes=['','_province'])
        .drop(columns=['address_id','province_id'])
        .rename(columns={'name_province':'province','code':'province_code'}))
    dim_store = dim_store.reset_index(drop=True)
    dim_store['store_sk'] = dim_store.index + 1

    dim_store = (
        dim_store[[
            'store_sk',
            'store_id',
            'name',
            'line1',
            'line2',
            'country_code',
            'province',
            'province_code',
            'city',
            'postal_code',
            'created_at'
        ]]
        .copy()
    )

    return dim_store