from pathlib import Path

from extract import CSVExtractor
from load import CSVLoader
import transform as tr

RAW_PATH = Path("data/raw")
STAGING_PATH = Path("data/staging")
WAREHOUSE_PATH = Path("data/warehouse")

def run_etl_pipeline():
    """
    Run entire ETL pipeline modularly.
    """

    try:
        # ==== EXTRACT ====
        extract = CSVExtractor()
        raw_data = extract.read_all_csv_files(RAW_PATH)
        
        # ==== STAGING ====
        clean_tables = {
            # 'address': tr.clean_address(),
            # 'channel': tr.clean_channel(),
            'customer': tr.clean_customer(raw_data['customer']),
            # 'nps_response': tr.clean_nps_response(),
            # 'payment': tr.clean_payment(),
            # 'product_category': tr.clean_product_category(),
            # 'product': tr.clean_product(),
            # 'province': tr.clean_province(),
            # 'sales_order_item': tr.clean_sales_order_item(),
            # 'sales_order': tr.clean_sales_order(),
            # 'shipment': tr.clean_shipment(),
            # 'store': tr.clean_store(),
            'web_session': tr.clean_web_session(raw_data['web_session'])
        }

        # ==== TRANSFORM ====
        dim_tables = {
            'calendar': tr.build_dim_calendar(),
            'source':   tr.build_dim_source(clean_tables['web_session']),
            'device':   tr.build_dim_device(clean_tables['web_session']),
            'customer': tr.build_dim_customer(clean_tables['customer'])}

        fact_tables = {
            'web_session': tr.build_fact_web_session(clean_tables['web_session'],
                                                     dim_tables['customer'],
                                                     dim_tables['device'],
                                                     dim_tables['source'],
                                                     dim_tables['calendar'])}

        # ==== LOAD ====
        load = CSVLoader()

        for dim in dim_tables:
            if dim == 'calendar':
                dim_tables[dim].to_parquet(WAREHOUSE_PATH / f"dim_{dim}.parquet", compression="snappy")
            else:
                load.save_dataframe(WAREHOUSE_PATH, dim_tables[dim], f"dim_{dim}")

        for fact in fact_tables:
            load.save_dataframe(WAREHOUSE_PATH, fact_tables[fact], f"fact_{fact}")

    except Exception as e:
        raise e

if __name__ == "__main__":
    run_etl_pipeline()