import pandas as pd

def build_fact_web_session(
        clean_web_session: pd.DataFrame,
        dim_customer: pd.DataFrame,
        dim_calendar: pd.DataFrame
    ) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    fact_table = clean_web_session.copy()

    fact_table = (
        fact_table
        .merge(dim_customer[['customer_sk','customer_id']], on='customer_id', how="left")
        .merge(dim_calendar[['time_sk','datetime_id']].add_prefix("started_at_"), left_on='started_at_int', right_on='started_at_datetime_id', how="left")
        .merge(dim_calendar[['time_sk','datetime_id']].add_prefix("ended_at_"), left_on='ended_at_int', right_on='ended_at_datetime_id', how="left")
        .drop(columns=['customer_id','started_at','ended_at'])
        .rename(columns={'started_at_time_sk': "started_at_sk", 'ended_at_time_sk': "ended_at_sk"})
    )

    fact_table = fact_table.reset_index(drop=True)
    fact_table['session_sk'] = fact_table.index + 1

    fact_table = (
        fact_table[[
            'session_sk',
            'session_id',
            'customer_sk',
            'started_at_sk',
            'ended_at_sk',
            'source',
            'device', # VER AGREGAR DURACION EN SEGUNDOS POR SESION, EN TEORIA COLUMNA ESTA EN CLEAN
        ]]
        .copy()
    )

    return fact_table