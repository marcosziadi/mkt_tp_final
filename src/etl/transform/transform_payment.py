import pandas as pd

DATETIME_UNKNOWN_OBJ = '1900-01-01 00:00:00'
TRANSACTION_REF_UNKNOWN = '-1'

def clean_payment(payment_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    payment_clean = payment_raw.copy()

    try: 
        payment_clean['paid_at'] = payment_clean['paid_at'].fillna(DATETIME_UNKNOWN_OBJ)
        payment_clean['paid_at'] = pd.to_datetime(payment_clean['paid_at']).dt.floor('min')

        payment_clean['paid_at_int'] = (
            payment_clean['paid_at']
            .dt.strftime('%Y%m%d%H%M')
            .astype(int)
        )

        payment_clean['transaction_ref'] = payment_clean['transaction_ref'].fillna(TRANSACTION_REF_UNKNOWN)
        return payment_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning payment.csv | Missing required column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed cleaning payment.csv | Unexpected Error: {e}") from e
    
