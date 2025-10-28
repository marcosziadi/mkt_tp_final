import pandas as pd

def clean_sales_order_item(sales_order_item_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''
    try:
        sales_order_item_clean = sales_order_item_raw.copy()
        return sales_order_item_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'sales_order_item_raw' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failes cleaning 'sales_order_item_raw' | Unexpected error: {str(e)}") from e
