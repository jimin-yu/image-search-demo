from feature_extractor import FeatureExtractor
from pathlib import Path

fe = FeatureExtractor()

feature = fe.extract('tmp/cat.jpeg')
