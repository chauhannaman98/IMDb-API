try:
    from bs4 import BeautifulSoup
    import requests
    import bs4
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

BASE_URL = "https://www.imdb.com/"


class GetTitleById:
    def getById(self):
        response = {'title': 'title'}
        return response


class GetNameById:
    def getById(self):
        response = {'name': 'name'}
        return response


def main():
    title_id = 'intersteller'
    get_title = GetTitleById()
    results = get_title.getById()
    print(results)
    name_id = 'intersteller'
    get_name = GetNameById()
    results = get_name.getById()
    print(results)


if __name__ == '__main__':
    main()
