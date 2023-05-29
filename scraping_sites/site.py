import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, site):
        self.site = site
        self.news = []
        self.browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240/198Safari / 537.36"}
        
    
    def get_news(self):
        if self.site.lower() == 'globo':
            url = 'http://www.globo.com'

            page = requests.get(url, headers=self.browsers)

            resposta = page.text
            tag_class = 'post__title'

            soup = BeautifulSoup(resposta, 'html.parser')

            all_news = soup.find_all('a')
            selected_news = []
            
            for news in all_news:
                if news.h2 != None and tag_class in news.h2.get('class'):
                    print(news.get('href'))
                    news_content = requests.get(news.get('href'), headers=self.browsers)
                    
                    select_news_content = BeautifulSoup(news_content.text, 'html.parser')
                    title = ''
                    subtitle = ''

                    for h1 in select_news_content.findAll('h1'):
                        if h1 != None and 'content-head__title' in h1.get('class'):
                            title = h1.getText()
                    
                    
                    for h2 in select_news_content.findAll('h2'):
                        fores = h2.get('class')
                        if fores != None and'content-head__subtitle' in fores:
                            subtitle = h2.getText()
                    
                    publication = select_news_content.find('div', {'class': 'content-publication-data__text'})
                    
                    news_page = {
                        'title': str(title),
                        'subtitle': str(subtitle),
                        'publication': str(publication)
                    }

                    if news_page.get('title'):
                        self.news.append(news_page)
                    
                    if len(self.news) == 10:
                        print(self.news)
                        break
                    

                    # selected_news.append(news)
        elif self.site.lower() == 'inteligencia_financeira':
            url = 'https://inteligenciafinanceira.com.br/saiba/economia/'

            page = requests.get(url, headers=self.browsers)

            resposta = page.text

            soup = BeautifulSoup(resposta, 'html.parser')

            most_read_news = soup.find_all('li', { 'class': 'list_mostviewed__item'})
            for news in most_read_news:
                current_news = news.find('a')
                tag = current_news.findNext('a')

                news_content = requests.get(current_news.get('href'), headers=self.browsers)
                select_news_content = BeautifulSoup(news_content.text, 'html.parser')

                content = ''

                for child in select_news_content.find('div', {'class': 'content-area-styles'}):
                    if child.name == 'p' or child.name == 'h2':
                        content += str(child)
                
                news_page = {
                    'title': str(current_news.getText()),
                    'subtitle': str(select_news_content.find('div', {'class': 'entry-content__excerpt'}).h2.getText()),
                    'content': content,
                    'link': str(current_news.get('href')),
                    'tag': {
                        'name': str(tag.getText()),
                        'link': str(tag.get('href'))
                    }
                }
                self.news.append(news_page)
            print(self.news)


self = Site('inteligencia_financeira')