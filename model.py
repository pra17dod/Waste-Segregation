import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed
import urllib.request
import sys
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

model2 = tf.keras.models.load_model('./model/model_final.h5')

class_name = { 0:'Biodegradable:Reuseable Cardboard waste', 1:'Non-Biodegradable:Reuseable glass waste',
               2:'Non-Biodegradable:Reuseable metal waste', 3:'Biodegradable Organic waste', 
               4:'Biodegradable:Reuseable Paper waste', 5:'Non-Biodegradable:Reuseable Plastic waste' }

def get_names(cache):
    return class_name[cache]

def get_output(url):

    img = urllib.request.urlopen(url).read()
    temp = tf.io.decode_jpeg(img, channels = 3)
    temp = tf.image.resize(temp, [224,224])
    temp = tf.reshape(temp, [-1,224,224,3])
    cache = tf.keras.backend.eval(tf.math.argmax(model2.predict(temp), axis = -1))[0]
    prediction = get_names(cache)
    
    return prediction

if __name__ == "__main__":
    print(get_output(sys.argv[1]))

