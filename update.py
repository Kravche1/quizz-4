import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('notebook.csv', 'w', encoding='utf-8', newline='\n')
f_obj = csv.writer(f)
f_obj.writerow(['Title', 'Price'])

ind = 1

while ind < 5:

    url = "https://ultra.ge/index.php?route=product/category&path=20&page= " + str(ind)
    requset = requests.get(url)

    soup_all = BeautifulSoup(requset.text, 'html.parser')
    soup = soup_all.find('div', class_='row category-row')
    all_notebook = soup.find_all('div', 'thumb-description clearfix')

    for each in all_notebook:
        title = each.h4.a.text
        price = each.find('p', class_='price').text
        price = price.replace(' ', '')
        f_obj.writerow([title, price])

    ind += 24
    sleep(randint(3, 8))



