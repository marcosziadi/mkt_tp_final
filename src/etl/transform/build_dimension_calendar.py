import pandas as pd

def build_dim_calendar() -> pd.DataFrame:
    """
    DESCRIPTION
    """
    # '2023-05-06 03:11:24' -> '2025-10-12 20:26:52'
    date_range = pd.date_range(start='2023-05-01 00:00:00', end='2025-11-01 00:00:00', freq="min")

    dim_time = pd.DataFrame({
        "time_key": range(1, len(date_range) + 1),
        "datetime_id": date_range.strftime("%Y%m%d%H%M").astype(int),
        "date": date_range.date,
        "time": date_range.time,
        "year": date_range.year,
        "month": date_range.month,
        "month_name": date_range.strftime("%B"),
        "day": date_range.day,
        "day_of_week": date_range.dayofweek + 1,
        "day_name": date_range.strftime("%A"),
        "hour": date_range.hour,
        "minute": date_range.minute,
        "is_weekend": date_range.dayofweek >= 5
    })
    
    return dim_time