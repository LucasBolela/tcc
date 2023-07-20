from bs4 import BeautifulSoup
import requests


def get_if(self, url="https://inteligenciafinanceira.com.br/saiba/empresas/"):
    page = requests.get(url, headers=self.browsers)

    resposta = page.text

    soup = BeautifulSoup(resposta, "html.parser")

    most_read_news = soup.find_all("div", {"class": "main-feed__list-item"})

    for news in most_read_news:
        news = news.find("div", {"class": "main-feed__title-area"})
        current_news = news.find("a")
        tag = news.find("ul", {"class": "main-feed__tags"}).find("a")

        news_content = requests.get(current_news.get("href"), headers=self.browsers)
        select_news_content = BeautifulSoup(news_content.text, "html.parser")

        content = ""

        for child in select_news_content.find("div", {"class": "content-area-styles"}):
            if child.name == "p" or child.name == "h2":
                content += str(child)

        news_page = {
            "title": str(current_news.getText()).replace("\n", "").strip(),
            "subtitle": str(
                select_news_content.find("div", {"class": "entry-content__excerpt"})
                .h2.getText()
                .replace("\n", " ")
                .strip()
            ),
            "content": content.replace("\n", " ").strip(),
            "link": str(current_news.get("href")),
            "tag": {
                "name": str(tag.getText()).replace("\n", " ").strip(),
                "link": str(tag.get("href")),
            },
            "fonte": self.site.lower(),
        }

        self.news.append(news_page)
