import pandas as pd

DATETIME_UNKNOWN_OBJ = '1900-01-01 00:00:00'

def build_dim_customer(customer_clean: pd.DataFrame) -> pd.DataFrame:
    """
    Creates customer dimension.
    """

    dim_customer = customer_clean.copy()
    dim_customer['customer_sk'] = dim_customer.index + 1

    dim_customer = (
        dim_customer[[
            'customer_sk',
            'customer_id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'status',
            'created_at'
        ]]
        .copy()
    )

    unknown_data = {
        'customer_sk': -1,
        'customer_id': -1,
        'email': 'Unknown',
        'first_name': 'Unknown',
        'last_name': 'Unknown',
        'phone': 'Unknown',
        'status': 'Unknown',
        'created_at': DATETIME_UNKNOWN_OBJ
    }

    unknown_customer = pd.DataFrame([unknown_data])
    dim_customer = pd.concat([unknown_customer, dim_customer], ignore_index=True)

    return dim_customer    