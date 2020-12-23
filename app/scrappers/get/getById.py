try:
    from bs4 import BeautifulSoup
    import requests
    import bs4
    import locale
    import re
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

BASE_URL = "https://www.imdb.com/"
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class GetTitleById:
    def getById(self, title_id):
        response = {}
        url = BASE_URL+'title/'+title_id+'/'
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        title_bar = soup.find('div', class_='title_bar_wrapper')

        rating = float(title_bar.find(itemprop='ratingValue').get_text())
        rating_count = title_bar.find(itemprop='ratingCount').get_text()
        rating_count = locale.atoi(rating_count)
        release_year = title_bar.find(id='titleYear').get_text()
        release_year = re.findall('([0-9]{4,4})', release_year)[0]
        title_bar1 = title_bar.find('h1', class_='')
        title_bar1.span.decompose()
        title = title_bar1.get_text().rstrip()
        running_time = title_bar.find('time').get_text().lstrip().rstrip()

        print(running_time)

        # storing results in dictionary
        response['rating'] = rating
        response['rating_count'] = rating_count
        response['release_year'] = release_year
        response['title'] = title
        response['running_time'] = running_time

        return response


class GetNameById:
    def getById(self):
        response = {'name': 'name'}
        return response


def main():
    title_id = 'tt0816692'
    get_title = GetTitleById()
    results = get_title.getById(title_id)
    print(results)
    name_id = 'intersteller'
    get_name = GetNameById()
    results = get_name.getById()
    print(results)


if __name__ == '__main__':
    main()
