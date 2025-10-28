import pandas as pd

DATETIME_UNKNOWN_OBJ = '1900-01-01 00:00:00'

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

    unknown_data = {
            'store_sk': -1,
            'store_id': -1,
            'name': 'unknown',
            'line1': 'unknown',
            'line2': 'unknown',
            'country_code': 'unknown',
            'province': 'unknown',
            'province_code': 'unknown',
            'city': 'unknown',
            'postal_code': -1,
            'created_at': DATETIME_UNKNOWN_OBJ
    }
    unknown_store = pd.DataFrame([unknown_data])
    dim_store = pd.concat([unknown_store, dim_store], ignore_index=True)

    return dim_store