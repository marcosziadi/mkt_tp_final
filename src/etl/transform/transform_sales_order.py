import pandas as pd

def clean_sales_order(sales_order_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    sales_order_clean = sales_order_raw.copy()

    sales_order_clean['order_date'] = pd.to_datetime(sales_order_clean['order_date']).dt.floor('min')

    sales_order_clean['order_date_int'] = (
        sales_order_clean['order_date']
        .dt.strftime('%Y%m%d%H%M')
        .astype(int)
    )

    return sales_order_clean
    