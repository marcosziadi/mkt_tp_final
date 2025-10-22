import pandas as pd

def build_dim_customer(customer_clean_df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates customer dimension.
    """

    dim_customer = customer_clean_df.copy()
    dim_customer['customer_key'] = customer_clean_df.index + 1
    dim_customer = (
        dim_customer[[
            'customer_key',
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