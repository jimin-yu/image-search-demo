from feature_extractor import FeatureExtractor
from pathlib import Path

fe = FeatureExtractor()

img_path = Path('./tmp/dog.jpg')
feature = fe.extract(img_path)
print(feature[0])
