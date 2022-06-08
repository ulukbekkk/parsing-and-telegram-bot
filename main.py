import requests
from bs4 import BeautifulSoup as BS
import json
url = 'https://kaktus.media/?lable=8&date=2022-03-28&order=time'

def get_soup(url):
    response = requests.get(url).text
    soup = BS(response, 'html.parser')
    return soup

def get_all_news_link():
    soup = get_soup(url)
    link = soup.find('div', attrs={"data-stat":"articles"})
    one_link_page = link.find_all('a', 'ArticleItem--name')
    res = [x.get('href') for x in one_link_page ]
    return res


def get_all_news_title():
    soup = get_soup(url)
    title = soup.find('div', attrs={"data-stat":"articles"})
    one_title_page = title.find_all('a', 'ArticleItem--name')
    all_title = [z.text.lstrip('\n') for z in one_title_page]

    return  all_title



def get_all_image():
    soup = get_soup(url)
    imgs = soup.find_all('img', 'ArticleItem--image-img')
    res = [y.get('src') for y in imgs]
    return res


def get_text():
    urls = get_all_news_link()
    list_ = []
    count = 0
    for url in urls:
        soup = get_soup(url)
        texts = soup.find('div', attrs={"class":"BbCode"}).get_text(strip='\n')
        count += 1
        print(count)
        list_.append(texts)
    return list_


def main():
    titles = get_all_news_title()
    images = get_all_image()
    textes = get_text()
    count = 0
    list_ = []
    for title in titles:
        dict_ = {'title':titles[count], 'image': images[count], 'text' : textes[count]}
        count += 1
        list_.append(dict_)
    return list_

def get_json():
    data = main()
    with open('bd.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent = 1)
    print('Все закончилось')

