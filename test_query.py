import asyncio
from image_crawler import ImageCrawler
from image_service import ImageService
from opensearch_service import OpensearchService
from feature_extractor import FeatureExtractor

crawler = ImageCrawler()
img_service = ImageService()
search_service = OpensearchService.instance()
fe = FeatureExtractor()

img_url = 'https://img.ssfshop.com/cmd/LB_500x660/src/https://img.ssfshop.com/goods/8SBR/22/02/08/GM0022020816455_1_ORGINL_20220211103711358.jpg'

async def main():
    img_path = await img_service.download_img(img_url)
    feature = fe.extract(img_path)
    img_service.delete_img(img_path)
    search_service.query(feature)

asyncio.run(main())




