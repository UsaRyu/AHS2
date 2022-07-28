import sys
import keras
from PIL import Image
from keras.models import load_model
import numpy as np

model = load_model("model.h5")
name = "processed_testdata/test_corna.jpg"
image = Image.open(name)
image = image.resize((64, 64))
#image.show()
image = image.resize((64, 64))
#image.show()
np_image = np.array(image)
np_image = np_image / 255
#np_image = np_image[np.newaxis, :]
np_image = np_image[np.newaxis, np.newaxis, :, :]
#np_image = np_image[np.newaxis, :, :, :, :]
result = model.predict(np_image)
print(np_image.shape)
print(result)

if result[0][0] > result[0][1] and result[0][0] > result[0][2] and result[0][0] > result[0][3]:
    print("corna")
elif result[0][1] > result[0][0] and result[0][1] > result[0][2] and result[0][1] > result[0][3]:
    print("peace")
elif result[0][2] > result[0][0] and result[0][2] > result[0][1] and result[0][2] > result[0][3]:
    print("shaka_hang")
else:
    print("thumbs_up")


'''
predicts = model.predict(x_test).argmax(axis=1)
labels = np.array([y.argmax() for y in y_test])
cl_report = metrics.classification_report(labels, predicts)
print(cl_report)
'''
