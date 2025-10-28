import pandas as pd

def clean_sales_order(sales_order_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    sales_order_clean = sales_order_raw.copy()

    try:
        sales_order_clean['order_date'] = pd.to_datetime(sales_order_clean['order_date']).dt.floor('min')
        sales_order_clean['order_date_int'] = (
            sales_order_clean['order_date']
            .dt.strftime('%Y%m%d%H%M')
            .astype(int)
        )
        return sales_order_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'sales_order_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'sales_order_raw' | Unexpected error: {str(e)}") from e
    