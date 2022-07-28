import sys
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np

model = load_model("model.h5")
name = "processed_testdata/test_thumbs.jpg"
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
    print("corna")
elif result[0][1] > result[0][0] and result[0][1] > result[0][2] and result[0][1] > result[0][3]:
    print("peace")
elif result[0][2] > result[0][0] and result[0][2] > result[0][1] and result[0][2] > result[0][3]:
    print("shaka_hang")
else:
    print("thumbs_up")