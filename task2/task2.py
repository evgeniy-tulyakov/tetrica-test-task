from bs4 import BeautifulSoup
import requests



BASE_URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
HOST = 'https://ru.wikipedia.org/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/83.0.4103.116 Chrome/83.0.4103.116 Safari/537.36'
}


def get_next_page(url):
    html = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(html.content, 'html.parser')
    element = soup.find_all('a', {'title': 'Категория:Животные по алфавиту', })
    for element_part in element:
        if element_part.text == 'Следующая страница':
            next_page = HOST + element_part.attrs['href']
            return next_page


def get_list_pages(url):
    yield url
    prev_page_url = url
    while True:
        next_page = get_next_page(prev_page_url)
        if not next_page: break
        print(next_page)
        yield next_page
        prev_page_url = next_page


def get_dict_with_all_animals(page_list):
    dict_animal = {}
    for page in page_list:
        print(page)
        html = requests.get(page, headers=HEADERS)
        soup = BeautifulSoup(html.content, 'html.parser')
        element = soup.select('#mw-pages > div > div > div > ul > li > a')
        if element == []:
            element = soup.select('#mw-pages > div > ul > li > a')

        for element_part in element:
            name_animal = element_part.attrs["title"]
            first_symbol = name_animal[0]
            if first_symbol not in dict_animal.keys():
                dict_animal[first_symbol] = []
            dict_animal[first_symbol].append(name_animal)

    return dict_animal


# Algorithm:
print('Starting:')
print('Getting pages...')
page_list = get_list_pages(BASE_URL)
print('\nMake list of animals...')
content = get_dict_with_all_animals(page_list)
print('\nTotal:')
for key, value in content.items():
    print(f'{key}: {len(value)}')
