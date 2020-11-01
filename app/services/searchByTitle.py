try:
    from bs4 import BeautifulSoup
    import requests
except e:
    print('Caught exception while importing: {}'.format(e))

BASE_URL = 'https://www.imdb.com/find?s=tt&q='

search_results = []
titles = []
year_of_release = []
urls = []
details = []


def create_result_list(number_of_results):
    search_results.clear()

    for i in range(number_of_results):
        item_dict = {}
        item_dict['title'] = titles[i]
        item_dict['url'] = urls[i]

        search_results.append(item_dict)


def searchByTitle(title):
    url = BASE_URL + title
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    main_div = soup.find('div', class_='article')
    table = soup.find('table', class_='findList')
    trs = soup.find_all('tr')
    tds = soup.find_all('td', class_='result_text')

    header = soup.find('h1', class_='findHeader')
    number_of_results = int(header.get_text().split(' ')[1])

    for td in tds:
        _title = td.find('a').get_text()
        _url = 'https://www.imdb.com/'+td.find('a')['href']

        titles.append(_title)
        urls.append(_url)

    create_result_list(number_of_results)

    return search_results


def main():
    title = 'tarzan'
    results = searchByTitle(title)
    print(results)


if __name__ == '__main__':
    main()
