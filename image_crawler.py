from bs4 import BeautifulSoup
import requests
import urllib.parse
import asyncio
import time
import aiohttp

class ImageCrawler:
    def __init__(self):
        self.img_urls = []

    
    def __url(self, keyword, page):
        search_text = urllib.parse.quote(keyword.encode("utf-8"))
        url = f'https://www.musinsa.com/search/musinsa/goods?q={search_text}&page={page}'
        return url

    def __postprocess(self, html):
        soup = BeautifulSoup(html, "html.parser")
        new_img_urls = [img.get('data-original') for img in soup.select('#searchList li img.lazyload.lazy')]
        self.img_urls.extend(new_img_urls)
         

    def one_page_sync(self, keyword, page):        
        url = self.__url(keyword, page)
        html = requests.get(url).content
        self.__postprocess(html)
 

    def all_pages_sync(self, keyword):
        for i in range(20):
            self.one_page_sync(keyword, i+1)    


    async def one_page_coroutine(self, session, keyword, page):
        url = self.__url(keyword, page)

        async with session.get(url) as response:
            html = await response.text()
            self.__postprocess(html)
  
        
    async def all_pages_coroutine(self, keyword, pages):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(pages):
                task = asyncio.create_task(self.one_page_coroutine(session, keyword, i+1))
                tasks.append(task)
                
            await asyncio.gather(*tasks, return_exceptions=True) 


    def crawl(self, keyword, pages):
        event_loop = asyncio.get_event_loop()  
        event_loop.run_until_complete(self.all_pages_coroutine(keyword, pages)) 
        return self.img_urls   



    
if __name__ == "__main__":
    crawler = ImageCrawler()
    print("===== sychronous version =====")
    start_time = time.time()
    crawler.all_pages_sync('후드티')
    duration = time.time() - start_time
    print(f'걸린시간 : {duration} 결과 : {len(crawler.img_urls)}')
    
    print("===== coroutine version ====")
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(crawler.all_pages_coroutine('후드티', 20))
    duration = time.time() - start_time
    print(f'걸린시간 : {duration} 결과 : {len(crawler.img_urls)}')


    




