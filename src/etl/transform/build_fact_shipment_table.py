import pandas as pd

def build_fact_shipment(
    shipment_clean: pd.DataFrame,
    sales_order_clean: pd.DataFrame,
    dim_channel: pd.DataFrame,
    dim_customer: pd.DataFrame,
    dim_address: pd.DataFrame,
    dim_store: pd.DataFrame,
    dim_calendar: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    fact_shipment = (
        shipment_clean
        .merge(sales_order_clean, on='order_id', how='left', suffixes=['','_order'])
        .merge(dim_customer[['customer_sk','customer_id']], on='customer_id', how='left')
        .merge(dim_channel[['channel_sk','channel_id']], on='channel_id', how='left')
        .merge(dim_store[['store_sk','store_id']], on='store_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='order_date_int', right_on='datetime_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='shipped_at_int', right_on='datetime_id', how='left', suffixes=['','_shipped_at'])
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='delivered_at_int', right_on='datetime_id', how='left', suffixes=['','_delivered_at'])
        .merge(dim_address[['address_sk','address_id']], left_on='billing_address_id', right_on='address_id', how='left')
        .merge(dim_address[['address_sk','address_id']], left_on='shipping_address_id', right_on='address_id', how='left', suffixes=['','_shipping'])
        # .drop(columns=['customer_id','channel_id','store_id','datetime_id','datetime_id_shipped_at','datetime_id_delivered_at','address_id','address_id_shipping','shipped_at','paid_at_int','billing_address_id','shipping_address_id','order_date','order_date_int','status_order'])
        .rename(columns={'time_sk':'order_date_sk','time_sk_shipped_at':'shipped_at_sk','time_sk_delivered_at':'delivered_at_sk','address_sk':'billing_address_sk','address_sk_shipping':'shipping_address_sk'})
    )

    fact_shipment = fact_shipment.reset_index(drop=True)
    fact_shipment['shipment_sk'] = fact_shipment.index + 1

    fact_shipment = (
        fact_shipment[[
            'shipment_sk',
            'shipment_id',
            'order_id',
            'customer_sk',
            'channel_sk',
            'store_sk',
            'billing_address_sk',
            'shipping_address_sk',
            'order_date_sk',
            'shipped_at_sk',
            'delivered_at_sk',
            'carrier',
            'tracking_number',
            'status',
            'shipping_fee'
        ]]
        .copy()
    )

    return fact_shipment
