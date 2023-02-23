""""Моя тренировка парсингу"""
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
for n in range(1,2):
    sleep(3)
    url='https://scrapingclub.com/exercise/list_basic/?page={}'.format(n)

    html=requests.get(url)
    print(html)

    soup=BeautifulSoup(html.text, 'html.parser')

    date= soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    with open('CSV.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['name', 'price', 'foto', 'code', 'inf'])
    for i in date:
        name = i.find('h4', class_='card-title').text.replace('\n', '')
        price = i.find('h5').text
        foto = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
        code= 'https://scrapingclub.com'+i.find('a').get('href')
        html1=requests.get(code)
        soup1=BeautifulSoup(html1.text, 'html.parser')
        inf=soup1.find('p', class_='card-text').get_text(strip=True)
        print(name+'\n'+price+'\n'+foto+'\n'+code+'\n'+inf+'\n')
        with open('CSV.csv','a',newline='') as file:
            writer= csv.writer(file,delimiter=';')
            writer.writerow([name,price,foto,code,inf])