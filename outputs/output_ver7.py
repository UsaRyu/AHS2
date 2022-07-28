import sys
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np

def predict(input_filename):
    model = load_model("model.h5")
    name = input_filename
    image = Image.open(name)
    image = image.resize((64, 64))
    #image.show()
    image = image.resize((64, 64))
    #image.show()
    np_image = np.array(image)
    np_image = np_image / 255
    np_image = np_image[np.newaxis, :, :, :]
    result = model.predict(np_image)
    print(result)

    if result[0][0] > result[0][1] and result[0][0] > result[0][2] and result[0][0] > result[0][3]:
        ans = "corna"
        score = result[0][0]
        print("corna")
        return ans, score
    elif result[0][1] > result[0][0] and result[0][1] > result[0][2] and result[0][1] > result[0][3]:
        ans = "peace"
        score = result[0][1]
        print("peace")
        return ans, score
    elif result[0][2] > result[0][0] and result[0][2] > result[0][1] and result[0][2] > result[0][3]:
        ans = "shaka_hang"
        score = result[0][2]
        print("shaka_hang")
        return ans, score
    else:
        ans = "thumbs_up"
        score = result[0][3]
        print("thumbs_up")
        return ans, score