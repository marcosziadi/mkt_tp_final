import pandas as pd

def build_fact_payment(
    payment_clean: pd.DataFrame,
    sales_order_clean: pd.DataFrame,
    dim_channel: pd.DataFrame,
    dim_customer: pd.DataFrame,
    dim_address: pd.DataFrame,
    dim_store: pd.DataFrame,
    dim_calendar: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCIRPTION
    '''

    fact_payment = (
        payment_clean
        .merge(sales_order_clean, on='order_id', how='left', suffixes=['','_order'])
        .merge(dim_customer[['customer_sk','customer_id']], on='customer_id', how='left')
        .merge(dim_channel[['channel_sk','channel_id']], on='channel_id', how='left')
        .merge(dim_store[['store_sk','store_id']], on='store_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='order_date_int', right_on='datetime_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='paid_at_int', right_on='datetime_id', how='left', suffixes=['','_paid_at'])
        .merge(dim_address[['address_sk','address_id']], left_on='billing_address_id', right_on='address_id', how='left')
        .merge(dim_address[['address_sk','address_id']], left_on='shipping_address_id', right_on='address_id', how='left', suffixes=['','_shipping'])
        .drop(columns=['customer_id','channel_id','store_id','datetime_id','datetime_id_paid_at','address_id','address_id_shipping','paid_at','paid_at_int','billing_address_id','shipping_address_id','order_date','order_date_int','status_order'])
        .rename(columns={'time_sk':'order_date_sk','time_sk_paid_at':'paid_at_sk','address_sk':'billing_address_sk','address_sk_shipping':'shipping_address_sk'})
    )

    fact_payment = fact_payment.reset_index(drop=True)
    fact_payment['payment_sk'] = fact_payment.index + 1

    fact_payment = (
        fact_payment[[
            'payment_sk',
            'payment_id',
            'order_id',
            'customer_sk',
            'channel_sk',
            'store_sk',
            'billing_address_sk',
            'shipping_address_sk',
            'order_date_sk',
            'paid_at_sk',
            'method',
            'status',
            'currency_code',
            'subtotal',
            'tax_amount',
            'shipping_fee',
            'amount',
            'transaction_ref'
        ]]
        .copy()
    )

    return fact_payment
