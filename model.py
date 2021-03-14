import urllib.request

import tensorflow as tf

model2 = tf.keras.models.load_model('./model/model.h5')

class_name = { 0:'Biodegradable:Reuseable Cardboard waste', 1:'Non-Biodegradable:Reuseable glass waste',
               2:'Non-Biodegradable:Reuseable metal waste', 3:'Biodegradable Organic waste', 
               4:'Biodegradable:Reuseable Paper waste', 5:'Non-Biodegradable:Reuseable Plastic waste' }

def get_names(cache):
    return class_name[cache]

def get_output(url):

    img = urllib.request.urlopen(url).read()
    temp = tf.io.decode_jpeg(img, channels = 3)
    # temp = img_to_array(img)
    temp = tf.image.resize(temp, [224,224])
    temp = tf.reshape(temp, [-1,224,224,3])
    cache = tf.keras.backend.eval(tf.math.argmax(model2.predict(temp), axis = -1))[0]
    prediction = get_names(cache)
    
    return prediction

if __name__ == "__main__":
    print(get_output(sys.argv[1]))

