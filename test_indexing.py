# urls = 후드티 이미지 url 크롤링 
# urls foreach |url| do
#  이미지 다운로드 (tmp에 저장) -> feature extract -> 인덱싱 -> 이미지 삭제
# end

from image_crawler import ImageCrawler
from image_service import ImageService
from opensearch_service import OpensearchService
from feature_extractor import FeatureExtractor

crawler = ImageCrawler()
img_service = ImageService()
search_service = OpensearchService()
fe = FeatureExtractor()


img_urls = crawler.crawl('후드티', 1)

search_service.create_index()

for url in img_urls:
    # async
    img_path = img_service.download_img(url)

    feature = fe.extract(img_path)

    document = {'img_vector': feature, 'url': url}
    # async
    search_service.create_doc(document)

    img_service.delete_img(img_path)

