import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import items
import file_io as fio


def get_distributer(url):

    return url.split('.')[1]

# --- Structures for supported distributors --- #

unsupported_items = {
                    'Unsupported Distributors':[]
}

digikey_items = {
                'Link':[],
                'Part':[],
                'Price':[],
                'Description':[],
                'Detailed Description':[]
}

# --- Load in links --- #

filename = 'items.xlsx'

urls = fio.read_urls(filename)

# --- Get distributors --- #

data = list() # Final list of all dataframes

for url in urls:

    dstbtr = get_distributer(url)

    if(dstbtr == 'digikey'):

        digi_item = items.DigiKeyItem(url)

        digikey_items['Link'].append(url)
        digikey_items['Part'].append(digi_item.get_part_name())
        digikey_items['Price'].append(digi_item.get_price())
        digikey_items['Description'].append(digi_item.get_descriptions()[0])
        digikey_items['Detailed Description'].append(digi_item.get_descriptions()[1])

    else:

        # Distributor not supported
        unsupported_items['Link'].append(url)
        print("Distributor not supported.")

# --- Save data --- #

data.append(pd.DataFrame(digikey_items))

fio.write_data(filename, data)

