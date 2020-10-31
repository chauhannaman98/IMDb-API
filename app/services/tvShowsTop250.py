try:
    from bs4 import BeautifulSoup
    import requests
    import json
except e:
    print('Caught exception while importing: {}'.format(e))


URL = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')

show_ranks = []
show_title = []
year_of_release = []
show_url = []
show_ratings = []
show_starcast = []
output_dict = {}


def save_to_dict():
    output_dict.update(data=True)


def get_data():
    main_div = soup.find('div', class_='lister')
    tbody = main_div.find('tbody', class_='lister-list')
    trs = tbody.find_all('tr')
    i = 1

    for tr in trs:
        title = tr.find('td', class_='titleColumn').find('a')
        title = tr.find('td', class_='titleColumn').find('a')
        year = tr.find(
            'td', class_='titleColumn').find('span').get_text()
        rating = tr.find('td', class_='ratingColumn imdbRating').find(
            'strong').get_text()
        url = 'https://www.imdb.com'+title['href']

        # Store data to lists
        show_ranks.append(i)
        show_title.append(title.get_text())
        year_of_release.append(year.strip('(').strip(')'))
        show_url.append(url)
        show_ratings.append(rating)
        show_starcast.append(title['title'])

        i += 1


def getTop250Shows():
    get_data()
    save_to_dict()
    return output_dict


def main():
    result = getTop250Shows()
    print(result)


if __name__ == '__main__':
    main()
