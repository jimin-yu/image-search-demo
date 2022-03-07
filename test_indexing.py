import time
import asyncio
from image_crawler import ImageCrawler
from image_service import ImageService
from opensearch_service import OpensearchService
from feature_extractor import FeatureExtractor
from lib.each_slice import each_slice

crawler = ImageCrawler()
img_service = ImageService()
search_service = OpensearchService.instance()
fe = FeatureExtractor()


# TODO: 에러 핸들링
async def download_img_and_extract_feature(url):
    img_path = await img_service.download_img(url)
    feature = fe.extract(img_path)
    img_service.delete_img(img_path)
    return {'img_vector': feature, 'url': url}


async def bulk(img_urls):
    tasks = [ asyncio.create_task(download_img_and_extract_feature(url)) for url in img_urls ]
    document_array = await asyncio.gather(*tasks, return_exceptions=True)
    search_service.bulk(document_array)


def main():
    batch_size = 100

    img_urls = crawler.crawl('후드티', 100)
    search_service.create_index()
    
    print("|start| indexing...")
    start = time.time()

    for urls in each_slice(img_urls, batch_size):
        asyncio.run(bulk(urls))

    print(f'|fin| batch-size : {batch_size}, time : {time.time() - start}')


main()












  
