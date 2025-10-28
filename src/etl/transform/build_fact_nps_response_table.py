import pandas as pd

def build_fact_nps_response(
    clean_nps_response: pd.DataFrame,
    dim_customer: pd.DataFrame,
    dim_channel: pd.DataFrame,
    dim_calendar: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    fact_table = clean_nps_response.copy()

    fact_table = (
        fact_table
        .merge(dim_customer[['customer_sk','customer_id']], on='customer_id', how='left')
        .merge(dim_channel[['channel_sk','channel_id']], on='channel_id', how='left')
        .merge(dim_calendar[['time_sk','datetime_id']], left_on='responded_at_int', right_on='datetime_id', how='left')
        .drop(columns=['customer_id','channel_id','datetime_id','responded_at_int'])
        .rename(columns={'time_sk': 'responded_at_sk'})
    )

    fact_table = fact_table.reset_index(drop=True)
    fact_table['nps_sk'] = fact_table.index + 1

    fact_table = (
        fact_table[[
            'nps_sk',
            'responded_at_sk',
            'nps_id',
            'score',
            'comment'
        ]]
        .copy()
    )

    return fact_table