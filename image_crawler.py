from bs4 import BeautifulSoup
import requests
import urllib.parse

class Crawler:
    def __encode_uri_component(self, text):
        return urllib.parse.quote(text.encode("utf-8"))


    def crawl(self, keyword):
        search_text = self.__encode_uri_component(keyword)
        page = 1
        url = f'https://www.musinsa.com/search/musinsa/goods?q={search_text}&page={page}'
        print(url)

        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        
        for img in soup.select('#searchList li img.lazyload.lazy'):
            print('??')
            print(img.get('src'))


if __name__ == "__main__":
    crawler = Crawler()
    crawler.crawl('후드티')


    




