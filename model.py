import numpy as np
import os
import shutil
import re
import random
from PIL import Image
import sys
from PIL import Image
import urllib.request

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing import image_dataset_from_directory


model2 = tf.keras.models.load_model('./model/model.h5')

class_name = { 0:'Biodegradable:Reuseable Cardboard waste', 1:'Non-Biodegradable:Reuseable glass waste',
               2:'Non-Biodegradable:Reuseable metal waste', 3:'Biodegradable Organic waste', 
               4:'Biodegradable:Reuseable Paper waste', 5:'Non-Biodegradable:Reuseable Plastic waste' }

def get_names(cache):
    return class_name[cache]

def get_output(url):

    img = Image.open(urllib.request.urlopen(url))
    temp = img_to_array(img)
    temp = tf.image.resize(temp, [224,224])
    temp = tf.reshape(temp, [-1,224,224,3])
    cache = np.argmax(model2.predict(temp))
    prediction = get_names(cache)
    
    return prediction

if __name__ == "__main__":
    print(get_output(sys.argv[1]))

