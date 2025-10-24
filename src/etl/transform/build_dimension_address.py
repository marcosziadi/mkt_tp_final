import pandas as pd

def build_dim_address(address_clean: pd.DataFrame, province_clean: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    dim_address = (
        address_clean
        .merge(province_clean, on='province_id', how='inner')
        .drop(columns=['province_id'])
        .rename(columns={'name':'province', 'code':'province_code'})
    )

    dim_address = dim_address.reset_index(drop=True)
    dim_address['address_sk'] = dim_address.index + 1

    dim_address = (
        dim_address[[
            'address_sk',
            'address_id',
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

    return dim_address