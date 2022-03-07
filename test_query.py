import asyncio
from image_crawler import ImageCrawler
from image_service import ImageService
from opensearch_service import OpensearchService
from feature_extractor import FeatureExtractor

crawler = ImageCrawler()
img_service = ImageService()
search_service = OpensearchService.instance()
fe = FeatureExtractor()

img_url = 'https://image.msscdn.net/images/goods_img/20150901/242972/242972_11_500.jpg'

async def main():
    img_path = await img_service.download_img(img_url)
    feature = fe.extract(img_path)
    img_service.delete_img(img_path)
    search_service.query(feature)

asyncio.run(main())




