import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('movie.csv', 'w', encoding='utf-8', newline='\n')  # <---- Csv file creation
# file.write('Title,Year,Ranking,URL\n') # <---- we are trying to take it to the CSV file
f_obj = csv.writer(f)  # <--- take parameter of our file!
f_obj.writerow(['Title', 'Year', 'Ranking', 'URL'])

header = {'Accept-Language': 'en-US'}  # language we can check by spelling of print (value.headers)
# and we need to see 'Content-Language'
ind = 1
while ind < 5:
    url = 'https://www.imdb.com/search/title/?groups=top_250&start=' + str(ind)
    request = requests.get(url, headers=header)

    soup_all = BeautifulSoup(request.text, 'html.parser')  # we approve that this is html file
    soup = soup_all.find('div', class_='lister-list')
    all_movies = soup.find_all('div', class_='lister-item')
    for each in all_movies:
        url = each.img.attrs.get('loadlate')
        title = each.h3.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        # ranking = each.find('div', class_='inline-block ratings-imdb-rating').text #alternative way
        ranking = each.strong.text
        print(ranking)
        # file.write(title + ',' + year + ',' + ranking + ',' + url + '\n') #alternative way
        f_obj.writerow([title, year, ranking, url])
    ind += 50
    sleep(randint(3, 8))
