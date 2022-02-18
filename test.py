# from feature_extractor import FeatureExtractor
# from pathlib import Path

# fe = FeatureExtractor()

# feature = fe.extract('tmp/cat.jpeg')



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

from opensearch_service import OpensearchService

opensearch_service = OpensearchService.instance()

# opensearch_service.create_index()
opensearch_service.delete_index()





