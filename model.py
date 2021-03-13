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
import sys
from PIL import Image
import urllib.request

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing import image_dataset_from_directory
# from tfhub import load_model_weights


# model = tf.keras.applications.ResNet50(include_top=False, input_shape=(224,224,3))

# model.trainable = False
# model2 = tf.keras.Sequential()
# model2.add(model)
# model2.add(tf.keras.layers.Flatten())
# model2.add(tf.keras.layers.Dropout(0.2))
# model2.add(tf.keras.layers.Dense(6, activation='softmax'))

model2 = tf.keras.models.load_model('./model/model.h5')

## get a path to the folder with images
# path = os.path.join(os.getcwd(),"model/dataset-resized")

# train = tf.keras.preprocessing.image_dataset_from_directory(path, batch_size=16, image_size=(224,224), shuffle=True, label_mode='categorical', validation_split = 0.25, seed = 1, subset = 'training')
# valid = tf.keras.preprocessing.image_dataset_from_directory(path, batch_size=16, image_size=(224,224), shuffle=True, label_mode='categorical', validation_split = 0.25, seed = 1, subset = 'validation')

class_name = { 0:'Biodegradable:Reuseable Cardboard waste', 1:'Non-Biodegradable:Reuseable glass waste',
               2:'Non-Biodegradable:Reuseable metal waste', 3:'Biodegradable Organic waste', 
               4:'Biodegradable:Reuseable Paper waste', 5:'Non-Biodegradable:Reuseable Plastic waste' }

def get_names(cache):
    return class_name[cache]

def get_output(url):

    img = Image.open(urllib.request.urlopen(url))
    temp = img_to_array(img)
    # print(temp.shape)
    temp = tf.image.resize(temp, [224,224])
    # print(temp.shape)
    temp = tf.reshape(temp, [-1,224,224,3])
    cache = np.argmax(model2.predict(temp))
    prediction = get_names(cache)
    
    return prediction

if __name__ == "__main__":
    print(get_output(sys.argv[1]))

