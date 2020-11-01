[![time tracker](https://wakatime.com/badge/github/chauhannaman98/IMDb-API.svg)](https://wakatime.com/badge/github/chauhannaman98/IMDb-API) 

![GitHub](https://img.shields.io/github/license/chauhannaman98/IMDb-API) ![Lines of code](https://img.shields.io/tokei/lines/github/chauhannaman98/IMDb-API) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/chauhannaman98/IMDb-API/flask)

![GitHub pull requests](https://img.shields.io/github/issues-pr/chauhannaman98/IMDb-API) ![GitHub issues](https://img.shields.io/github/issues-raw/chauhannaman98/IMDb-API?color=red) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/chauhannaman98/IMDb-API)

# IMDb-API

A REST-API for IMDb based on Flask and BeautifulSoup using Python3. This API is deployed on Heroku's server on non-production dynos. Thus, the first call to the API may take longer time than expected. The following calls will be fast comparatively.

# Features

1. [Home](#Home)
2. [Search](#Search)
3. [TV Shows](#TV-Shows)

# Home

**URL:** https://imdbapi.herokuapp.com/

**Description:** This API will give a simple JSON response regarding the services currently available along with
date when API has been called, status and GitHub repository URL.

**Response:**

```json
{
    "api-services-available": {
        "Search by title": "https://imdbapi.herokuapp.com/search?q=TitleHere",
        "Top25 TV Shows": "https://imdbapi.herokuapp.com/tv-shows/top250"
    },
    "date": "Oct-31-2020",
    "source": "https://github.com/chauhannaman98/IMDb-API",
    "status": true
}
```

# Search

1. [Search by title](#Search-by-title)

## 1. Search by title

**URL:** https://imdbapi.herokuapp.com/search

**Params:**
1. `q` = query or the title to be searched

**Description:** This API will give a JSON response with a list of search results on the basis of the
title you sent as the param(`q`). List contains dictionaries where each dictionary consists of 2 
key-value pairs, `title` and `url`.

**Response:**

```json
{
    "date": "Nov-01-2020",
    "search-results": [
        {
            "title": "Crown",
            "url": "https://www.imdb.com/title/tt3432862/"
        },
    ],
    "status": true
}
```

# TV Shows

1. [Top 250](#Top-250)

## 1. Top 250

**URL:** https://imdbapi.herokuapp.com/tv-shows/top250

**Description:** This API will give a JSON response having top 250 TV shows in the ranked according to 
their ratings on [IMDb](https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250). In short, it gives the
top rates 250 shows from IMDb in a JSON format. Key `top250` here has a list of 250 dictonaries. Each
dictionary of key-value pairs that have details of TV Shows including `rank`, `rating`, `starcast`, `title`,
`url` and `year-of-release`.

**Response:**

```json
{
    "date": "Oct-31-2020",
    "status": true,
    "top250": [
        {
            "rank": 1,
            "rating": "9.5",
            "starcast": "David Attenborough",
            "title": "Planet Earth II",
            "url": "https://www.imdb.com/title/tt5491994/",
            "year-of-release": "2016"
        },
    ]
}
```
