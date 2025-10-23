import pandas as pd

def build_dim_source(web_session_clean_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Creates source dimension.
    '''

    dim_source = pd.DataFrame()

    try:
        dim_source['source'] = web_session_clean_df['source'].unique()
        dim_source['source_sk'] = dim_source.index + 1
        dim_source = dim_source[['source_sk','source']].copy()
        return dim_source
    
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed creating dim_source | Missing required column: {e}") from e
    
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed creating dim_source | Unexpected Error: {e}") from e