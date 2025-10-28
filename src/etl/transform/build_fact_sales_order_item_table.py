import pandas as pd

def build_fact_sales_order_item(
        clean_sales_order_item: pd.DataFrame,
        clean_sales_order: pd.DataFrame,
        dim_channel: pd.DataFrame,
        dim_product: pd.DataFrame,
        dim_customer: pd.DataFrame,
        dim_address: pd.DataFrame,
        dim_store: pd.DataFrame,
        dim_calendar: pd.DataFrame
    ) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    fact_sales_order_item = (
        clean_sales_order_item
        .merge(clean_sales_order, on='order_id', how='inner')
        .drop(columns=['subtotal'])
    )

    fact_sales_order_item = (
        fact_sales_order_item
        .merge(dim_channel[['channel_sk','channel_id']], on='channel_id', how='left')
        .merge(dim_product[['product_sk','product_id']], on='product_id', how='left')
        .merge(dim_customer[['customer_sk','customer_id']], on='customer_id', how='left')
        .merge(dim_address[['address_sk','address_id']], left_on='billing_address_id', right_on='address_id', how='left')
        .merge(dim_address[['address_sk','address_id']], left_on='shipping_address_id', right_on='address_id', how='left', suffixes=['','_shipping'])
        .merge(dim_store[['store_sk','store_id']], on='store_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='order_date_int', right_on='datetime_id', how='left')
        .drop(columns=['channel_id','product_id','customer_id','address_id','address_id_shipping','store_id','order_date_int','order_date','datetime_id'])
        .rename(columns={'time_sk':'order_date_sk','address_sk':'billing_address_sk','address_sk_shipping':'shipping_address_sk'})
    )

    fact_sales_order_item = fact_sales_order_item.reset_index(drop=True)
    fact_sales_order_item['order_item_sk'] = fact_sales_order_item.index + 1

    fact_sales_order_item = (
        fact_sales_order_item[[
            'order_item_sk',
            'order_item_id',
            'order_id',
            'product_sk',
            'customer_sk',
            'channel_sk',
            'store_sk',
            'billing_address_sk',
            'shipping_address_sk',
            'order_date_sk',
            'quantity',
            'unit_price',
            'discount_amount',
            'line_total',
            'status',
            'currency_code',
            'tax_amount',
            'shipping_fee'
        ]]
        .copy()
    )

    return fact_sales_order_item