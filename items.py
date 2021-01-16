import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class Item:

    def __init__(self, url):
        
        self.url = url

        html_response = requests.get(self.url)

        self.page = BeautifulSoup(html_response.text,'html.parser')

    def get_url(self):
        return self.url

    def get_distributor(self):
        return self.url.split('.')[1]

class DigiKeyItem(Item):

    def __init__(self, url):

        super(DigiKeyItem,self).__init__(url)

        self.data = {'Link':url,
            'Part':"",
            'Stock':"",
            'Price':"",
            'Description':"",
            'Detailed Description':"",
        }

        self.url = url

    def get_part_name(self):

        try:

            name_box = self.page.find('h1',attrs={'itemprop':'model'})

            name = name_box.text.strip()

        except Exception as e:

            print(e)

            name = "N/A"

        return name

    def get_stock(self):

        try:

            stock = self.page.find('span',attrs={'id':'dkQty'})

        except Exception as e:

            print(e)

            stock = "N/A"

        return stock.text

    def get_price(self):

        price_breaks = list()
        found = 0
        quantity=1

        table = self.page.find('table',attrs={'class':'product-dollars'})

        for row in table.findAll("tr"):
            
            cells = row.findAll("td")

            if(len(cells)>1):

                price_break = cells[0].text.strip().replace(',',"")

                unit_price = cells[1].text.strip()

                price_breaks.append((price_break,unit_price))
        
        price_breaks.reverse()

        if(quantity == 0):

            price = 0

        else:

            for i in range(len(price_breaks)):

                if(quantity >= int(price_breaks[i][0])):

                    price = price_breaks[i][1]

                    found = 1

                    break

            if(not found):

                price = "N/A"

        return price

    def get_descriptions(self):

        try:

            table = self.page.find('table',attrs={'id':'product-overview'})

            rows = table.findAll("tr")

            try:

                des = self.page.find('td',attrs={'itemprop':'description'}).text.strip()
    
            except Exception as e:

                print(e)
                
                des = "N/A"

            try:

                detailed_des = self.page.find('h3',attrs={'itemprop':'description'}).text.strip()

            except Exception as e:

                print(e)

                detailed_des = "N/A"

        except Exception as e:

            print(e)

            des = "N/A"

            detailed_des = "N/A"

        return des, detailed_des

    def get_data_as_dict(self):

        part_name = self.get_part_name()

        stock = self.get_stock()

        price = self.get_price()

        descriptions = self.get_descriptions()

        self.data['Part'] = part_name
        self.data['Stock'] = stock
        self.data['Price'] = price
        self.data['Description'] = descriptions[0]
        self.data['Detailed Description'] = descriptions[1]

        return self.data

    def get_data_as_tuple(self):

        part_name = self.get_part_name()

        stock = self.get_stock()

        price = self.get_price()

        descriptions = self.get_descriptions()

        return (part_name,stock,price,descriptions[0],descriptions[1])