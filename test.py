# from feature_extractor import FeatureExtractor
# from pathlib import Path

# fe = FeatureExtractor()

# feature = fe.extract('tmp/cat.jpeg')
# print(feature)



# class Car:
#     # private static attribute
#     __instance = None
#     # static attribute
#     name = 'morning'

#     @classmethod
#     def instance(cls):
#         if(cls.__instance is None):
#             cls.__instance = cls()

#         return cls.__instance   

#     def __init__(self):
#         # instance attribute
#         self.name = 'mini'
#         self.owner = 'jimin'


# c1 = Car.instance()
# c2 = Car.instance()

# print(c1 is c2)     # True
# print(Car.name)     # morning
# print(c1.name)      # mini

# from opensearch_service import OpensearchService

# opensearch_service = OpensearchService.instance()

# print(opensearch_service.client.indices.exists(index='img_search'))

# if(opensearch_service.client.indices.exists(index='img_search')):
#     opensearch_service.delete_index()
# opensearch_service.create_index()

# doc_array = [{'img_vector': [1,2,3,4], 'url': 'https://naver.com'}, 
#              {'img_vector':[5,3,7,8], 'url': 'https://google.com'},
#              {'img_vector': [2,3,4,5], 'url': 'https://youtube.com'}]
# opensearch_service.bulk(doc_array)
# opensearch_service.query([2, 3, 5, 6])




# url -> 이미지 tmp에 저장 -> feature extract -> 인덱싱 -> 이미지 삭제


# import requests

# image_url = 'https://upload.wikimedia.org/wikipedia/ko/d/d4/%ED%8E%AD%EC%88%98.jpg'
# image_name = 'pengsoo'
# img_data = requests.get(image_url).content
# with open( f'tmp/{image_name}.jpeg', 'wb') as handler:
#     handler.write(img_data)

# import os
# os.unlink('tmp/pengsoo.jpeg')


# from feature_extractor import FeatureExtractor
# from image_service import ImageService
# from opensearch_service import OpensearchService

# fe = FeatureExtractor()
# img_service = ImageService()
# os_service = OpensearchService.instance()


# # img_search 인덱스 생성
# if(os_service.client.indices.exists(index='img_search')):
#     os_service.delete_index()
# os_service.create_index()

# # 이미지 임시 폴더에 다운로드
# url = 'https://upload.wikimedia.org/wikipedia/ko/d/d4/%ED%8E%AD%EC%88%98.jpg'
# img_path = img_service.download_img(url)
# print(img_path)

# # 벡터 추출
# feature = fe.extract(img_path)

# # 인덱싱
# document = {'img_vector': feature, 'url': url}
# os_service.create_doc(document)

# # 이미지 삭제
# img_service.delete_img(img_path)


# import glob
# from feature_extractor import FeatureExtractor
# fe = FeatureExtractor()

# img_paths = glob.glob('tmp/**/*.jpeg', recursive=True)
# fe.extract_multi(img_paths)

import urllib.parse

def encode_uri_component(text):
    return urllib.parse.quote(text.encode("utf-8"))

print(encode_uri_component('후드티'))

