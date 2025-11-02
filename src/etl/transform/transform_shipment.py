import pandas as pd

DATETIME_UNKNOWN_ID = '-1'
TRACKING_NUMBER_UNKNOWN = '-1'  

def clean_shipment(shipment_raw: pd.DataFrame) -> pd.DataFrame:
    '''
    DESCRIPTION
    '''

    shipment_clean = shipment_raw.copy()

    # pd.to_datetime() admite nulls y los deja null
    try:
        shipment_clean['shipped_at_int'] = (
            pd.to_datetime(shipment_clean['shipped_at'])
            .dt.strftime('%Y%m%d%H%M')
            .fillna(DATETIME_UNKNOWN_ID)
            .astype(int))
        
        shipment_clean['delivered_at_int'] = (
            pd.to_datetime(shipment_clean['delivered_at'])
            .dt.strftime('%Y%m%d%H%M')
            .fillna(DATETIME_UNKNOWN_ID)
            .astype(int))

        shipment_clean['tracking_number'] = shipment_clean['tracking_number'].fillna(TRACKING_NUMBER_UNKNOWN)
        
        return shipment_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning payment.csv | Missing required column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed cleaning payment.csv | Unexpected Error: {e}") from e