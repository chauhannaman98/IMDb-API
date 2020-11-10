try:
    from bs4 import BeautifulSoup
    import requests
    import re
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

BASE_URL = 'https://www.imdb.com/find?s=nm&q='
DETAILS_PATTERN = r'\(([a-zA-Z\s]+)\,'


class SearchByName:
    def searchByName(self, name):
        search_results = []
        names = []
        urls = []
        occupation = []
        url = BASE_URL + name
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        main_div = soup.find('div', class_='article')
        table = soup.find('table', class_='findList')
        trs = soup.find_all('tr')
        tds = soup.find_all('td', class_='result_text')

        header = soup.find('h1', class_='findHeader')
        number_of_results = int(header.get_text().split(' ')[1])

        for td in tds:
            _name = td.find('a').get_text()
            _url = 'https://www.imdb.com'+td.find('a')['href']

            try:
                detail = td.find('small').text
                _detail = re.findall(DETAILS_PATTERN, detail)[0]
            except:
                _detail = None

            names.append(_name)
            urls.append(_url)
            occupation.append(_detail)

        for i in range(number_of_results):
            item_dict = {}
            item_dict['name'] = names[i]
            item_dict['url'] = urls[i]
            item_dict['occupation'] = occupation[i]

            search_results.append(item_dict)

        return search_results


def main():
    name = 'amitabh'
    obj = SearchByName()
    results = obj.searchByName(name)
    print(results)


if __name__ == '__main__':
    main()
