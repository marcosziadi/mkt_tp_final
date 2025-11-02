import pandas as pd

UNKNOWN_STORE_ID = -1
UNKNOWN_ADDRESS_ID = -1

def clean_sales_order(sales_order_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    sales_order_clean = sales_order_raw.copy()

    try:
        sales_order_clean['order_date_int'] = (
            pd.to_datetime(sales_order_clean['order_date'])
            .dt.strftime('%Y%m%d%H%M')
            .astype(int))

        sales_order_clean['store_id'] = sales_order_clean['store_id'].fillna(UNKNOWN_STORE_ID)
        sales_order_clean['billing_address_id'] = sales_order_clean['store_id'].fillna(UNKNOWN_ADDRESS_ID)

        return sales_order_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'sales_order_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'sales_order_raw' | Unexpected error: {str(e)}") from e
    