# urls = 후드티 이미지 url 크롤링 
# urls foreach |url| do
#  이미지 다운로드 (tmp에 저장) -> feature extract -> 인덱싱 -> 이미지 삭제
# end

import asyncio
import time
from image_crawler import ImageCrawler
from image_service import ImageService
from opensearch_service import OpensearchService
from feature_extractor import FeatureExtractor

crawler = ImageCrawler()
img_service = ImageService()
search_service = OpensearchService.instance()
fe = FeatureExtractor()


img_urls = crawler.crawl('후드티', 3)

search_service.create_index()

start_time = time.time()

tasks = []
for url in img_urls:
    # async
    task = asyncio.create_task(img_service.download_img(url))
    tasks.append(task)

    img_path = img_service.download_img(url)

    feature = fe.extract(img_path)

    document = {'img_vector': feature, 'url': url}
    # async
    search_service.create_doc(document)

    img_service.delete_img(img_path)

duration = time.time() - start_time
print(f'sync took : {duration} sec')


async def process_one_image(img_url):
    img_path = await img_service.download_img(img_url)

    feature = fe.extract(img_path)

    print(img_path)

url = 'http://economychosun.com/query/upload/322/20191103221129_fgyjnwts.jpg'
asyncio.run(process_one_image(url))    