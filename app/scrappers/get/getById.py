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
        url = BASE_URL+'title/'+title_id
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
        summary_text = soup.find(
            'div', class_='summary_text').get_text().rstrip().lstrip()

        # Storyline section
        storyline_dict = {}
        storyline = soup.find('div', {'id': 'titleStoryLine'})

        storyline_summary = storyline.find('div', class_='inline canwrap')
        storyline_summary = storyline_summary.find(
            'span').text.rstrip().lstrip()
        plot_soup = storyline.findAll('div', 'see-more inline canwrap')[0]
        keywords_soup = plot_soup.find_all('span')
        keywords = []
        for keyword in keywords_soup:
            if keyword.get_text() != '|':
                keywords.append(keyword.get_text())
        tagline_soup = storyline.find('div', class_='txt-block')
        tagline_soup.span.decompose()
        tagline_soup.h4.decompose()
        tagline = tagline_soup.get_text().lstrip().rstrip()
        genres_soup = storyline.findAll('div', 'see-more inline canwrap')[1]
        genres_soup = genres_soup.findAll('a')
        genres = []
        for gen in genres_soup:
            genres.append(gen.get_text().lstrip().rstrip())

        # Storing storyline data in dictionary
        storyline_dict['plot'] = storyline_summary
        storyline_dict['plot_keywords'] = keywords
        storyline_dict['tagline'] = tagline
        storyline_dict['genres'] = genres

        # Title detail section
        title_detail_soup = soup.find('div', {'id': 'titleDetails'})
        headings_soup = title_detail_soup.find_all(['h2', 'h3'])
        details_soup = title_detail_soup.find_all('div', class_='txt-block')
        detail_list = ['Official Sites:', 'Country:', 'Language:',
                       'Release Date:', 'Also Known As:', 'Filming Locations:']
        details = {}
        for detail in details_soup:
            try:
                head = detail.find('h4')
                if head.get_text() in detail_list:
                    if head.get_text() == 'Official Sites:':
                        official_site = {}
                        detail.h4.decompose()
                        a_tags = detail.find_all('a')
                        for a_tag in a_tags:
                            if a_tag.get_text() != 'See more':
                                data = url+a_tag['href']
                                official_site[a_tag.get_text()] = data
                        details['official-site'] = official_site
            except Exception as e:
                print(e)

        # print(details)

        # storing results in dictionary
        response['rating'] = rating
        response['rating_count'] = rating_count
        response['release_year'] = release_year
        response['title'] = title
        response['running_time'] = running_time
        response['summary_text'] = summary_text
        response['storyline'] = storyline_dict
        response['deails']: details

        return response


class GetNameById:
    def getById(self):
        response = {'name': 'name'}
        return response


def main():
    title_id = 'tt0816692'
    get_title = GetTitleById()
    results = get_title.getById(title_id)
    # print(results)
    # name_id = 'intersteller'
    # get_name = GetNameById()
    # results = get_name.getById()
    # print(results)


if __name__ == '__main__':
    main()
