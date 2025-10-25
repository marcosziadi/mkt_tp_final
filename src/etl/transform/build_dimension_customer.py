import pandas as pd

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
    return dim_customer    