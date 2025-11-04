import pandas as pd

def build_fact_sales_order(
        clean_sales_order: pd.DataFrame,
        dim_channel: pd.DataFrame,
        dim_customer: pd.DataFrame,
        dim_address: pd.DataFrame,
        dim_store: pd.DataFrame,
        dim_calendar: pd.DataFrame
    ) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    fact_sales_order = (
        clean_sales_order
        .merge(dim_channel[['channel_sk','channel_id']], on='channel_id', how='left')
        .merge(dim_customer[['customer_sk','customer_id']], on='customer_id', how='left')
        .merge(dim_address[['address_sk','address_id']], left_on='billing_address_id', right_on='address_id', how='left')
        .merge(dim_address[['address_sk','address_id']], left_on='shipping_address_id', right_on='address_id', how='left', suffixes=['','_shipping'])
        .merge(dim_store[['store_sk','store_id']], on='store_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='order_date_int', right_on='datetime_id', how='left')
        .drop(columns=['channel_id','customer_id','address_id','address_id_shipping','store_id','order_date_int','order_date','datetime_id'])
        .rename(columns={'time_sk':'order_date_sk','address_sk':'billing_address_sk','address_sk_shipping':'shipping_address_sk'})
    )

    fact_sales_order = fact_sales_order.reset_index(drop=True)
    fact_sales_order['order_sk'] = fact_sales_order.index + 1

    fact_sales_order = (
        fact_sales_order[[
            'order_sk',
            'order_id',
            'customer_sk',
            'channel_sk',
            'store_sk',
            'billing_address_sk',
            'shipping_address_sk',
            'order_date_sk',
            'status',
            'currency_code',
            'subtotal',
            'tax_amount',
            'shipping_fee',
            'total_amount'
        ]]
        .copy()
    )

    return fact_sales_order