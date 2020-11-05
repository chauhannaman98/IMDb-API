try:
    from bs4 import BeautifulSoup
    import requests
    import re
    import bs4
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

BASE_URL = 'https://www.imdb.com/find?s=tt&q='
YEAR_PATTERN = r'\(\d{4,4}\)'
DETAIL_PATTERN = r'\((?!I+)([a-zA-Z-\s]+)\)'

titles = []
year_of_release = []
urls = []
details = []


def create_result_list(number_of_results):
    search_results = []
    search_results.clear()

    for i in range(number_of_results):
        item_dict = {}
        item_dict['title'] = titles[i]
        item_dict['url'] = urls[i]
        item_dict['year-of-release'] = year_of_release[i]
        item_dict['details'] = details[i]

        search_results.append(item_dict)

    return search_results


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
        _url = 'https://www.imdb.com'+td.find('a')['href']

        try:
            result = re.findall(YEAR_PATTERN, td.get_text())
            _year = int(result[0].strip('(').strip(')'))
        except Exception as e:
            _year = None

        try:
            text = []
            for x in td:
                if isinstance(x, bs4.element.NavigableString):
                    text.append(x.strip())
            txt = " ".join(text)
            _details = re.findall(DETAIL_PATTERN, txt)
        except Exception as e:
            _details = None

        titles.append(_title)
        urls.append(_url)
        year_of_release.append(_year)
        details.append(_details)

    search_results = create_result_list(number_of_results)

    return search_results


def main():
    title = 'intersteller'
    results = searchByTitle(title)
    print(results)


if __name__ == '__main__':
    main()
