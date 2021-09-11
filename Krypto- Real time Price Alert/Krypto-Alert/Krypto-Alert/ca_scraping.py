from bs4 import BeautifulSoup
import re
import requests
import pandas
import json
import time
import random


def get_price(url):
    price = 0
    coinmarketcap = requests.get(url)
    soup = BeautifulSoup(coinmarketcap.content, 'html.parser')
    line = soup.find('div', {'class' : 'priceValue'}).text

    price = line[1:]

    try:
        test = float(price.replace(",",""))

        if test <= 0:
            return ""
    except:
        return ""
    
    return price

def scrape_crypto_names(update_screen, update_status, update_message, go_button, close_button):
    go_button.config(bg = "light grey", state = "disabled")
    close_button.config(bg = "light grey", state = "disabled")
    update_status.config(text = "Working on it...")
    update_message.config(text = "Starting up...")
    update_screen.update()

    headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
    cryptos = {} 
    sorted_cryptos = {} 
    file = 'cryptos.csv' 

    try:
        time.sleep(1)
        coinmarketcap = requests.get('https://coinmarketcap.com/')
        soup = BeautifulSoup(coinmarketcap.content, 'html.parser')
        pages = calculate_pages(soup) 

        #scrape data from pages
        for i in range (1, pages + 1):
            time.sleep(0.5 + float(random.randrange(0, 1) / 2))
            update_message.config(text = "Loading " + str(i) + " of " + str(pages) + "...")
            update_screen.update()

            url = 'https://coinmarketcap.com/?page=' + str(i) 
            site = requests.get(url, headers = headers, timeout = 5)
            soup = BeautifulSoup(site.content, 'html.parser')
            
            data = soup.find('script', id = "__NEXT_DATA__", type = "application/json")
            crypto_data = json.loads(data.contents[0])
            listings = crypto_data['props']['initialState']['cryptocurrency']['listingLatest']['data']

           
            for i in listings:
                cryptos[str(i['name'])] = str(i['symbol']), "https://coinmarketcap.com/currencies/" + str(i['slug'])

     
        for key in sorted(cryptos):
            sorted_cryptos[key] = cryptos[key]
        #print to file
        print_to_csv(sorted_cryptos, file)

        update_status.config(text = "Done!")
        update_message.config(text = "Coin list has been updated successfully!")
        go_button.config(bg = "green", state = "normal")
        close_button.config(bg = "#004ac2", state = "normal")
    
    except Exception as e:
        update_status.config(text = "Oops!")
        update_message.config(text = "Something went wrong. The update task could not be completed, possibly due to an issue with the site. Please try again later.")
        go_button.config(bg = "green", state = "normal")
        close_button.config(bg = "#004ac2", state = "normal")
        return


def calculate_pages(soup):
    text = soup.findAll('p', string = re.compile("Showing")) 
    text_numbers = re.findall(r'\d+',str(text)) 

    items_total = int(text_numbers[len(text_numbers) - 1]) 
    items_per_page = int(text_numbers[len(text_numbers) - 2]) 
    pages = round(items_total / items_per_page) 

    return pages


def print_to_csv(cryptos, file):
    crypto_names = []
    crypto_symbols = []
    crypto_urls = []

    for key in cryptos:
        crypto_names.append(str(key))
        crypto_symbols.append(str(cryptos[key][0]))
        crypto_urls.append(str(cryptos[key][1]))

    dataframe = pandas.DataFrame(columns = ['name', 'symbol', 'url'])

    dataframe['name'] = crypto_names
    dataframe['symbol'] = crypto_symbols
    dataframe['url'] = crypto_urls
    
    dataframe.to_csv(file, index = False)