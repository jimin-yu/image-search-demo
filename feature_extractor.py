from keras.models import Model
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
import numpy as np
import tensorflow as tf
import keras.layers as layers

class FeatureExtractor:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        base = MobileNetV2(input_shape=self.input_shape,
                                             include_top=False,
                                             weights='imagenet')
        base.trainable = False
        self.model = Model(inputs=base.input, outputs=layers.GlobalAveragePooling2D()(base.output))

    def __preprocess(self, img_path):  
        img = tf.io.read_file(img_path)
        img = tf.image.decode_jpeg(img, channels=self.input_shape[2])
        img = tf.image.resize(img, self.input_shape[:2])
        img = preprocess_input(img)
        return img  

    def extract(self, img_path):
        img = self.__preprocess(img_path)
        img = tf.expand_dims(img, axis=0)
        feature = self.model.predict(img)[0]
        # normalized_feature = feature / np.linalg.norm(feature)
        return feature

    def extract_multi(self, img_paths):
        batch_size = 100
        features = []
        list_ds = tf.data.Dataset.from_tensor_slices(img_paths)
        ds = list_ds.map(lambda x: self.__preprocess(x), num_parallel_calls=-1)
        dataset = ds.batch(batch_size).prefetch(-1)

        for batch in dataset:
            x = self.model.predict(batch)
            features.extend(x)

        return features