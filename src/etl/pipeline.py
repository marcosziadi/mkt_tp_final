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

    extract = CSVExtractor()
    load = CSVLoader()

    # ==== EXTRACT ====
    raw_data = extract.read_all_csv_files(RAW_PATH)
    
    # ==== STAGING ====
    clean_tables = {
        'address': tr.clean_address(address_raw=raw_data['address']),
        'channel': tr.clean_channel(channel_raw=raw_data['channel']),
        'customer': tr.clean_customer(customer_raw=raw_data['customer']),
        'nps_response': tr.clean_nps_response(nps_response_raw=raw_data['nps_response']),
        'payment': tr.clean_payment(payment_raw=raw_data['payment']),
        'product_category': tr.clean_product_category(product_category_raw=raw_data['product_category']),
        'product': tr.clean_product(product_raw=raw_data['product']),
        'province': tr.clean_province(province_raw=raw_data['province']),
        'sales_order_item': tr.clean_sales_order_item(sales_order_item_raw=raw_data['sales_order_item']),
        'sales_order': tr.clean_sales_order(sales_order_raw=raw_data['sales_order']),
        'shipment': tr.clean_shipment(shipment_raw=raw_data['shipment']),
        'store': tr.clean_store(store_raw=raw_data['store']),
        'web_session': tr.clean_web_session(web_session_raw=raw_data['web_session'])
    }

    for table in clean_tables:
        load.save_dataframe(STAGING_PATH, clean_tables[table], f"clean_{table}")

    # ==== TRANSFORM ====
    clean_data = extract.read_all_csv_files(STAGING_PATH)

    dim_tables = {
        'calendar': tr.build_dim_calendar(),
        'source': tr.build_dim_source(web_session_clean=clean_data['clean_web_session']),
        'device': tr.build_dim_device(web_session_clean=clean_data['clean_web_session']),
        'customer': tr.build_dim_customer(customer_clean=clean_data['clean_customer']),
        'product': tr.build_dim_product(product_clean=clean_data['clean_product'],
                                        product_category_clean=clean_data['clean_product_category']),
        'channel': tr.build_dim_channel(channel_clean=clean_data['clean_channel']),
        'address': tr.build_dim_address(address_clean=clean_data['clean_address'],
                                        province_clean=clean_data['clean_province']),
        'store': tr.build_dim_store(store_clean=clean_data['clean_store'],
                                    address_clean=clean_data['clean_address'],
                                    province_clean=clean_data['clean_province'])}

    fact_tables = {
        'web_session': tr.build_fact_web_session(clean_web_session=clean_data['clean_web_session'],
                                                 dim_customer=dim_tables['customer'],
                                                 dim_device=dim_tables['device'],
                                                 dim_source=dim_tables['source'],
                                                 dim_calendar=dim_tables['calendar']),
        'nps_response': tr.build_fact_nps_response(clean_nps_response=clean_data['clean_nps_response'],
                                                   dim_customer=dim_tables['customer'],
                                                   dim_channel=dim_tables['channel'],
                                                   dim_calendar=dim_tables['calendar']),
        'sales_order': tr.build_fact_sales_order(clean_sales_order=clean_data['clean_sales_order'],
                                                 dim_channel=dim_tables['channel'],
                                                 dim_customer=dim_tables['customer'],
                                                 dim_address=dim_tables['address'],
                                                 dim_store=dim_tables['store'],
                                                 dim_calendar=dim_tables['calendar']),
        'sales_order_item': tr.build_fact_sales_order_item(clean_sales_order_item=clean_data['clean_sales_order_item'],
                                                           clean_sales_order=clean_data['clean_sales_order'],
                                                           dim_channel=dim_tables['channel'],
                                                           dim_product=dim_tables['product'],
                                                           dim_customer=dim_tables['customer'],
                                                           dim_address=dim_tables['address'],
                                                           dim_store=dim_tables['store'],
                                                           dim_calendar=dim_tables['calendar']),
        'payment': tr.build_fact_payment(payment_clean=clean_data['clean_payment'],
                                         sales_order_clean=clean_data['clean_sales_order'],
                                         dim_channel=dim_tables['channel'],
                                         dim_customer=dim_tables['customer'],
                                         dim_address=dim_tables['address'],
                                         dim_store=dim_tables['store'],
                                         dim_calendar=dim_tables['calendar']),
        'shipment': tr.build_fact_shipment(shipment_clean=clean_data['clean_shipment'],
                                           sales_order_clean=clean_data['clean_sales_order'],
                                           dim_channel=dim_tables['channel'],
                                           dim_customer=dim_tables['customer'],
                                           dim_address=dim_tables['address'],
                                           dim_store=dim_tables['store'],
                                           dim_calendar=dim_tables['calendar'])}

    # ==== LOAD ====
    for dim in dim_tables:
        if dim == 'calendar':
            dim_tables[dim].to_parquet(WAREHOUSE_PATH / f"dim_{dim}.parquet", compression="snappy")
        else:
            load.save_dataframe(WAREHOUSE_PATH, dim_tables[dim], f"dim_{dim}")

    for fact in fact_tables:
        load.save_dataframe(WAREHOUSE_PATH, fact_tables[fact], f"fact_{fact}")

if __name__ == "__main__":
    run_etl_pipeline()