import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, site):
        self.site = site
        self.news = []
    
    def get_news(self):
        if self.site.lower() == 'globo':
            url = 'http://www.globo.com'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240/198Safari / 537.36"}

            page = requests.get(url, headers=browsers)

            resposta = page.text
            tag_class = 'post__title'

            soup = BeautifulSoup(resposta, 'html.parser')

            all_news = soup.find_all('a')
            selected_news = []
            
            for news in all_news:
                if news.h2 != None and tag_class in news.h2.get('class'):
                    print(news.get('href'))
                    news_content = requests.get(news.get('href'), headers=browsers)
                    
                    select_news_content = BeautifulSoup(news_content.text, 'html.parser')
                    title = ''
                    subtitle = ''

                    for h1 in select_news_content.findAll('h1'):
                        if h1 != None and 'content-head__title' in h1.get('class'):
                            title = h1.getText()
                    
                    print(select_news_content.findAll('h2'))
                    
                    for h2 in select_news_content.findAll('h2'):
                        fores = h2.get('class')
                        print(fores)
                        if fores != None and'content-head__subtitle' in fores:
                            subtitle = h2.getText()
                    
                    publication = select_news_content.find('div', {'class': 'content-publication-data__text'})
                    
                    news_page = {
                        'title': str(title),
                        'subtitle': str(subtitle),
                        'publication': str(publication)
                    }
                    print(news_page)
                    if news_page.get('title'):
                        self.news.append(news_page)
                    
                    if len(self.news) == 50:
                        print
                        break

                    # selected_news.append(news)


self = Site('globo')