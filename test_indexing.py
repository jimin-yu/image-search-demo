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

async def bulk(img_urls):
    # 이미지 다운로드
    tasks = [ asyncio.create_task(img_service.download_img(url)) for url in img_urls ]
    img_paths = await asyncio.gather(*tasks, return_exceptions=True)
    
    # feature 추출
    features = fe.extract_multi(img_paths)

    # 이미지 삭제
    for path in img_paths:
        img_service.delete_img(path)

    # bulk 인덱싱
    document_array = [ {'img_vector': feature, 'url': url} for feature, url in zip(features, img_urls) ]
    search_service.bulk(document_array)


def main():
    batch_size = 100

    img_urls = crawler.crawl('원피스', 50)
    search_service.create_index()
    
    print("indexing...")
    start = time.time()

    for urls in each_slice(img_urls, batch_size):
        asyncio.run(bulk(urls))

    print(f'time : {time.time() - start}')

main()












  
