from keras.models import load_model

# load the model
model = load_model('model.h5')

# predict pose from image
import numpy as np
import cv2
import matplotlib.pyplot as plt

def predict_pose(img):
    # load the image
    img = cv2.resize(img, (150, 150))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    # use the model
    result = model.predict(img)

    # get max index
    max_index = np.argmax(result)

    #labels
    labels = ['downdog', 'goddess', 'plank', 'tree', 'warrior2']

    response = labels[max_index] + '-splitter-' + str(result[0][max_index])

    return str(response)