import tensorflow as tf
from tensorflow.keras.layers import Activation, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=(64, 64, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Dense(4))
model.add(Activation("softmax"))
model.summary()
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"])


train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    "model_data/train",
    target_size=(64, 64),
    batch_size=5)
validation_generator = validation_datagen.flow_from_directory(
    "model_data/validation",
    target_size=(64, 64),
    batch_size=5)
model.fit(
    train_generator,
    epochs=25,
    steps_per_epoch=9,
    validation_data=validation_generator,
    validation_steps=1)
model.save("model.h5")

import sys
from PIL import Image
from keras.models import load_model
import numpy as np

name = "model_data/testbox/test_thumbs_ori.jpg"
image = Image.open(name)
image = image.resize((64, 64))
image.show()
image = image.resize((64, 64))
image.show()
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