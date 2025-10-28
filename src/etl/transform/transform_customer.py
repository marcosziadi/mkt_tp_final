import pandas as pd

def clean_customer(customer_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning of customer.csv
    """

    customer_clean = customer_raw.copy()

    try:
        customer_clean['created_at'] = pd.to_datetime(customer_clean['created_at']).dt.floor("min")
        return customer_clean
    except KeyError as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'customer' | Missing column: {e}") from e
    except Exception as e:
        raise RuntimeError(f"ERROR: Failed cleaning 'customer' | Unexpected Error: {e}") from e