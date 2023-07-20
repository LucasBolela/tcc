from bs4 import BeautifulSoup
import requests


def get_infomoney(self, url="https://www.infomoney.com.br/economia/"):
    page = requests.get(url, headers=self.browsers)

    resposta = page.text

    soup = BeautifulSoup(resposta, "html.parser")

    all_news = soup.find_all("div", {"class": "article-card__content"})

    for news in all_news:
        current_news = news.find("a")

        news_content = requests.get(current_news.get("href"), headers=self.browsers)
        select_news_content = BeautifulSoup(news_content.text, "html.parser")

        content = ""
        for child in (
            select_news_content.find("div", {"class": "single__content"})
            .find("div", {"class": "element-border--bottom"})
            .find_all("p")
        ):
            if child.name == "p" and child.name != "div":
                content += str(child.getText())

        news_page = {
            "title": str(current_news.getText()).replace("\n", "").strip(),
            "subtitle": str(
                select_news_content.find("div", {"class": "single__excerpt"})
                .p.getText()
                .replace("\n", " ")
                .strip()
            ),
            "content": content.replace("\n", " ").strip(),
            "link": str(current_news.get("href")),
            "tag": {
                "name": "Economia",
                "link": url,
            },
            "fonte": self.site.lower(),
        }
        self.news.append(news_page)
