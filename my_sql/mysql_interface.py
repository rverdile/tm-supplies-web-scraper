from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_products(products):
    """
    Inserts one or multiple rows of product into the products table of the tm_purchase_orders database.

    :param products: list of tuples. In each tuple is the values of the records (to be inserted) as follows: 

                        url,distributor,name,description,detailed_description
    """

    query = "INSERT INTO products(url,distributor,name,description,detailed_description) " \
            "VALUES(%s,%s,%s,%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, products)

        conn.commit()

    except Error as e:
        print('Error', e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':

    test_entry_1 = ("https://www.digikey.com/en/products/detail/koa-speer-electronics-inc/SR73" \
                        "1ETTPR200F/12748012?s=N4IgTCBcDaIMoCUDsBmAjAUQCpYAoLAAZCAxEAXQF8g", # URL
                    "Digi-Key", # Distributor
                    "SR731ETTPR200F", # Name
                    "CURRENT SENSE RESISTOR", # Description
                    "200 mOhms ±1% 0.167W, 1/6W Chip Resistor 0402 (1005 Metric) Automotive AEC-Q200," \
                        "Current Sense, Moisture Resistant Thick Film" # Detailed Description
                )

    test_entry_2 = ("https://www.digikey.com/en/products/detail/sunon-fans/MF40100V1-1000U-A99/6198732", # URL
                    "Digi-Key", # Distributor
                    "MF40100V1-1000U-A99", # Name
                    "40X40X10 5VDC VAPO 7CFM", # Description
                    "Fan Tubeaxial 5VDC Square - 40mm L x 40mm H Vapo-Bearing™ 8.0 CFM (0.224m³/min) 2 Wire Leads" # Detailed Description
                )

    test_entry_3 = ("https://www.digikey.com/en/products/detail/texas-instruments/DAC082S085CIMM-NOPB/1206385", # URL
                    "Digi-Key", # Distributor
                    "DAC082S085CIMM", # Name
                    "IC DAC 8BIT V-OUT 10VSSOP", # Description
                    "8 Bit Digital to Analog Converter 2 10-VSSOP" # Detailed Description
                )

    test_entry_4 = ("https://www.digikey.com/en/products/detail/keystone-electronics/1029C/303554", # URL
                    "Digi-Key", # Distributor
                    "1029C", # Name
                    "COVER RETAINING FOR 1029 HOLDER", # Description
                    None # Detailed Description
                )

    test_products = [test_entry_1,test_entry_2,test_entry_3,test_entry_4]

    insert_products(test_products)