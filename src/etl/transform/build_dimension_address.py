import pandas as pd

DATETIME_UNKNOWN_OBJ = '1900-01-01 00:00:00'

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

    unknown_data = {
            'address_sk': -1,
            'address_id': -1,
            'line1': 'unknown',
            'line2': 'unknown',
            'country_code': 'unknown',
            'province': 'unknown',
            'province_code': 'unknown',
            'city': 'unknown',
            'postal_code': -1,
            'created_at': DATETIME_UNKNOWN_OBJ
    }

    unknown_address = pd.DataFrame([unknown_data])
    dim_address = pd.concat([unknown_address, dim_address], ignore_index=True)

    return dim_address