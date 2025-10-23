import pandas as pd

def build_dim_channel(channel_clean: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    dim_channel = channel_clean.copy()

    dim_channel = dim_channel.reset_index(drop=True)
    dim_channel['channel_sk'] = dim_channel.index + 1

    dim_channel = (
        dim_channel[[
            'channel_sk',
            'channel_id',
            'code',
            'name'
        ]]
        .copy()
    )

    return dim_channel