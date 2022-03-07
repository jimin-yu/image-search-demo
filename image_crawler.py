from bs4 import BeautifulSoup
import urllib.parse
import asyncio
import aiohttp

class ImageCrawler:
    def __init__(self):
        self.img_urls = []
    
    def __url(self, keyword, page):
        search_text = urllib.parse.quote(keyword.encode("utf-8"))
        url = f'https://www.musinsa.com/search/musinsa/goods?q={search_text}&page={page}'
        return url

    def __parse_img_url(self, html):
        soup = BeautifulSoup(html, "html.parser")
        new_img_urls = [img.get('data-original') for img in soup.select('#searchList li img.lazyload.lazy')]
        self.img_urls.extend(new_img_urls)
        

    async def get_one_page(self, session, keyword, page):
        url = self.__url(keyword, page)

        async with session.get(url) as response:
            html = await response.text()
            self.__parse_img_url(html)
  
        
    async def get_all_pages(self, keyword, pages):
        async with aiohttp.ClientSession() as session:
            tasks = [ asyncio.create_task(self.get_one_page(session, keyword, i)) for i in range(1, pages+1)]    
            await asyncio.gather(*tasks, return_exceptions=True) 

    def crawl(self, keyword, pages):
        asyncio.run(self.get_all_pages(keyword, pages))
        return self.img_urls   

    




