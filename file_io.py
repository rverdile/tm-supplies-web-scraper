import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import items

def read_urls(filename):

    file = pd.read_excel(filename)

    urls = file['Link'].values

    return urls

def write_data(filename, data):

    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    for d in data:

        item = items.Item(d['Link'][0])

        dstbtr = item.get_distributor()

        d.to_excel(writer, sheet_name = dstbtr)

    writer.save()
