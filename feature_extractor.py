from keras.models import Model
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
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
        img = tf.expand_dims(img, axis=0)
        img = preprocess_input(img)
        return img  

    def extract(self, img_path):
        img = self.__preprocess(img_path)
        feature = self.model.predict(img)[0]
        return feature