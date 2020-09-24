from bs4 import BeautifulSoup
import pandas as pd
import items
import gspread_pandas

def read_urls(spread,sheet_name=None):
	"""
	Reads urls from a particular sheet under the column "Link"

	spread: a gspread object representing the entire Google Sheets spreadsheet (whereas 'sheet' is a tab on the spreadsheet)
	sheet_name: name of sheet being read

	returns list of urls
	"""

	sheet = spread.sheet_to_df(sheet=sheet_name,index=False)

	urls = sheet['Link'].values

	return urls

def write_data(df, spread):
	"""
	Writes data contained in 'df' to 'spread' spreadsheet

	df: pandas dataframe containing data
	spread: a gspread object representing the entire Google Sheets spreadsheet (whereas 'sheet' is a tab on the spreadsheet)
	"""


	for d in df:

		item = items.Item(d['Link'][0])

		dstbtr = item.get_distributor()

		spread.df_to_sheet(d,sheet=dstbtr,replace=True)
