import requests
from bs4 import BeautifulSoup
from scraputils import *


def test_extract_next_page() -> None:
    url = "https://news.ycombinator.com/"
    for i in range(2, 5):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        next_url = extract_next_page(soup)
        assert next_url == "news?p=" + str(i)
        url = "https://news.ycombinator.com/" + next_url


def test_extract_news() -> None:
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    current_news = extract_news(soup)
    news_keys = {"author", "points", "title", "url"}
    assert set(current_news[0].keys()) == news_keys


def test_get_news() -> None:
    news = []
    url = "https://news.ycombinator.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    current_news = extract_news(soup)
    next_url = extract_next_page(soup)
    url = "https://news.ycombinator.com/" + next_url
    news.extend(current_news)

    assert get_news("https://news.ycombinator.com/") == news
