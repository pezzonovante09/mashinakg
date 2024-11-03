# import requests
# from bs4 import BeautifulSoup as BS
# import csv
# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     cars = soup.find_all('div', class_='list-item list-label')
#     # print(cars)
#     for car in cars:
#         try:
#             title = car.find('div', class_='block title').text
#         except:
#             title = ''
#         try:
#             price = car.find('div', class_='block price').text
#         except:
#             price = ''
#         try:
#             image = car.find('img').get('src')
#         except:
#             image=''
#         try:
#             opisanie = car.find('div', class_='block info-wrapper item-inf').text
#         except:
#             opisanie=''
#         data = {
#             'title': title,
#             'price': price,
#             'photo': image,
#             'opisanie': opisanie
#         }
#         print(data)
#         write_csv(data)

# def write_csv(data):
#     with open('cars.csv', 'a') as csv_files:
#         names = ['title', 'price', 'image', 'opisanie']
#         writer = csv.DictWriter(csv_files, delimiter='|', fieldnames=names)
#         writer.writerow(data)


# def main():
#     url = 'https://www.mashina.kg/search/all/'
#     html = get_html(url)
#     data = get_data(html)



# main()

# import requests
# from bs4 import BeautifulSoup as BS
# import csv
# import os

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     cars = soup.find_all('div', class_='list-item list-label')
    
#     for car in cars:
#         try:
#             title = car.find('div', class_='block title').text.strip()
#         except AttributeError:
#             title = ''
#         try:
#             price = car.find('div', class_='block price').text.strip()
#         except AttributeError:
#             price = ''
#         try:
#             image = car.find('img').get('src')
#         except AttributeError:
#             image = ''
#         try:
#             opisanie = car.find('div', class_='block info-wrapper item-inf').text.strip()
#         except AttributeError:
#             opisanie = ''
        
#         data = {
#             'title': title,
#             'price': price,
#             'photo': image,
#             'opisanie': opisanie
#         }
#         print(data)
#         write_csv(data)

# def write_csv(data):
#     file_exists = os.path.isfile('cars.csv')
#     with open('cars.csv', 'a', newline='') as csv_files:
#         names = ['title', 'price', 'photo', 'opisanie']
#         writer = csv.DictWriter(csv_files, delimiter='|', fieldnames=names)
#         if not file_exists:
#             writer.writeheader()
#         writer.writerow(data)

# def main():
#     url = 'https://www.mashina.kg/search/all/'
#     html = get_html(url)
#     get_data(html)

# main()

# import requests
# from bs4 import BeautifulSoup as BS
# import csv
# import os

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BS(html, 'lxml')
#     cars = soup.find_all('div', class_='list-item list-label')
    
#     for car in cars:
#         try:
#             title = car.find('div', class_='block title').text.strip()
#         except AttributeError:
#             title = ''
#         try:
#             price = car.find('div', class_='block price').text.strip()
#         except AttributeError:
#             price = ''
#         try:
#             image = car.find('div',class_ ='image-wrap').find_all('img').get('src')
#             # image = f'https://mashina.kg{image}'
#         except AttributeError:
#             image = ''
#         try:
#             opisanie1 = car.find('div', class_='block info-wrapper item-inf').find('p', class_='year-miles').text
#             opisanie2 = car.find('div', class_='block info-wrapper item-inf').find('p', class_='body-type').text
#             opisanie3 = car.find('div', class_='block info-wrapper item-inf').find('p', class_='volume').text
#             print(opisanie1)
#             opisanie = opisanie1 + opisanie2 + opisanie3
#             print(f"Description: {opisanie}")
#         except AttributeError:
#             opisanie = ''
#         print(opisanie)
#         data = {
#             'title': title,
#             'price': price,
#             'photo': image,
#             'opisanie': opisanie
#         }
#         write_csv(data)

# def write_csv(data):
#     file_exists = os.path.isfile('cars.csv')
#     with open('cars.csv', 'a', newline='') as csv_files:
#         names = ['title', 'price', 'photo', 'opisanie']
#         writer = csv.DictWriter(csv_files, delimiter='|', fieldnames=names)
#         writer.writerow(data)

# def main():
#     url = 'https://www.mashina.kg/search/all/'
#     html = get_html(url)
#     get_data(html)

# main()

import requests
from bs4 import BeautifulSoup as BS
import csv
import os

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    cars = soup.find_all('div', class_='list-item list-label')
    
    for car in cars:
        try:
            title = car.find('div', class_='block title').text.strip()
        except AttributeError:
            title = ''
        
        try:
            price = car.find('div', class_='block price').text.strip()
        except AttributeError:
            price = ''
        
        try:
            image = car.find('img').get('src').strip()
            # image = f'https://mashina.kg{image}'  # Форматируем URL
            # print(image)
        except AttributeError:
            image = ''
        
        try:
            # opisanie1 = car.find('div', class_='block info-wrapper item-inf').find('p', class_='year-miles').text.strip()
            # opisanie2 = car.find('div', class_='block info-wrapper item-inf').find('p', class_='body-type').text.strip()
            # opisanie3 = car.find('div', class_='block info-wrapper item-inf').find('p', class_='volume').text.strip()
            opisanie = car.find('div', class_ ='block info-wrapper item-info-wrapper').text.strip()#f"{opisanie1}, {opisanie2}, {opisanie3}"
            print(opisanie)
        except AttributeError:
            opisanie = ''
        #print(f"Title: {title}, Price: {price}, Image: {image}, Description: {opisanie}")  # Отладочный вывод
        
        data = {
            'title': title,
            'price': price,
            'photo': image.strip(),
            'opisanie': opisanie.strip()
        }
        write_csv(data)
        print(car.find('div', class_ ='block info-wrapper item-info-wrapper').text.strip())
def write_csv(data):
    file_exists = os.path.isfile('cars.csv')
    with open('cars.csv', 'a', newline='') as csv_files:
        names = ['title', 'price', 'photo', 'opisanie']
        writer = csv.DictWriter(csv_files, delimiter='|', fieldnames=names)
        writer.writerow(data)

def main():
    url = 'https://www.mashina.kg/search/all/'
    html = get_html(url)
    data = get_data(html)
    for page in range(2, 1836):
        url = f"https://www.mashina.kg/search/all/?page={page}"
        html = get_html(url)
        data = get_data(html)


main()
