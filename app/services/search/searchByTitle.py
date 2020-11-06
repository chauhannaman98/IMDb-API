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


class SearchByTitle:
    titles = []
    year_of_release = []
    urls = []
    details = []
    search_results = []


    def create_result_list(self, number_of_results):
        self.search_results.clear()

        for i in range(number_of_results):
            item_dict = {}
            item_dict['title'] = self.titles[i]
            item_dict['url'] = self.urls[i]
            item_dict['year-of-release'] = self.year_of_release[i]
            item_dict['details'] = self.details[i]

            self.search_results.append(item_dict)

        return self.search_results


    def searchByTitle(self, title):
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

            self.titles.append(_title)
            self.urls.append(_url)
            self.year_of_release.append(_year)
            self.details.append(_details)

        self.search_results = self.create_result_list(number_of_results)

        return self.search_results


def main():
    title = 'intersteller'
    obj = SearchByTitle()
    results = obj.searchByTitle(title)
    print(results)


if __name__ == '__main__':
    main()
