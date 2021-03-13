import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
import re
import random
import seaborn as sns
import cv2 as cv
from PIL import Image
import pickle
import sys
sys.setrecursionlimit(1000000000)

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing import image_dataset_from_directory
# from tfhub import load_model_weights


model = tf.keras.applications.ResNet50(include_top=False, input_shape=(224,224,3), weights = None)

model2 = tf.keras.Sequential()
model2.add(model)
model2.add(tf.keras.layers.Flatten())
model2.add(tf.keras.layers.Dropout(0.2))
model2.add(Dense(512, activation = 'relu'))
model2.add(tf.keras.layers.Dropout(0.2))
model2.add(Dense(256, activation = 'relu'))
model2.add(tf.keras.layers.Dropout(0.2))
model2.add(Dense(128, activation = 'relu'))
model2.add(tf.keras.layers.Dropout(0.2))
model2.add(Dense(64, activation = 'relu'))
model2.add(tf.keras.layers.Dropout(0.2))
model2.add(tf.keras.layers.Dense(7, activation='softmax'))


model2.load_weights('./model/weights/waste_weights_heavy.h5')

## get a path to the folder with images
# path = os.path.join(os.getcwd(),"model/dataset-resized")

# train = tf.keras.preprocessing.image_dataset_from_directory(path, batch_size=16, image_size=(224,224), shuffle=True, label_mode='categorical', validation_split = 0.25, seed = 1, subset = 'training')
# valid = tf.keras.preprocessing.image_dataset_from_directory(path, batch_size=16, image_size=(224,224), shuffle=True, label_mode='categorical', validation_split = 0.25, seed = 1, subset = 'validation')
def get_output(path):

    temp = img_to_array(load_img(path, target_size=(224,224))).reshape(1,224,224,3)
    
    cache = np.argmax(model2.predict(temp))


    return cache

if __name__ == "__main__":
    # sys.argv[1]
    print(get_output(sys.argv[1]))

    

# temp = img_to_array(load_img('./model/dataset-resized/cardboard/cardboard100.jpg', target_size=(224,224))).reshape(1,224,224,3)
# np.argmax(model2.predict(temp))

