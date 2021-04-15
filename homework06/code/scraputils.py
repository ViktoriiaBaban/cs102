import typing as tp

import requests
from bs4 import BeautifulSoup


def extract_news(parser: BeautifulSoup) -> tp.List[tp.Dict[str, tp.Union[int, str]]]:
    """ Extract news from a given web page """

    news_list = []

    titles = parser.findAll("tr", attrs={"class": "athing"})
    subtext = parser.findAll("td", attrs={"class": "subtext"})

    for i in range(len(titles)):
        a = titles[i].findAll("td", attrs={"class": "title"})[1].find("a")
        title = a.get_text()
        url = a["href"]

        author = subtext[i].find("a", attrs={"class": "hnuser"})
        if author:
            author = author.get_text()

        point = subtext[i].find("span", attrs={"class": "score"})
        if point:
            point = point.get_text()

        news_list.append({"author": author, "points": point, "title": title, "url": url})

    return news_list


def extract_next_page(parser: BeautifulSoup) -> str:
    """ Extract next page URL """
    link = parser.select(".morelink")[0]["href"]
    return str(link)


def get_news(url: str, n_pages: int = 1) -> tp.List[tp.Dict[str, tp.Union[int, str]]]:
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news


if __name__ == "__main__":
    n = get_news(url="https://news.ycombinator.com/newest/", n_pages=3)
    print(len(n))
    print(n[1])
    print(n[18])
