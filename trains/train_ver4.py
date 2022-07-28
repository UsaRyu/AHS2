import tensorflow as tf
from tensorflow.keras.layers import Activation, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping

model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=(64, 64, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3)))
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
    batch_size=4)
validation_generator = validation_datagen.flow_from_directory(
    "model_data/validation",
    target_size=(64, 64),
    batch_size=4)
# EaelyStoppingの設定
early_stopping =  EarlyStopping(
                            monitor='val_loss',
                            min_delta=0.0,
                            patience=2,
)
model.fit(
    train_generator,
    epochs=30,
    steps_per_epoch=45,
    validation_data=validation_generator,
    validation_steps=9,
    callbacks=[early_stopping])
model.save("model.h5")

import sys
from PIL import Image
from keras.models import load_model
import numpy as np

name = "model_data/testbox/test_thumbs2.jpg"
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
'''
predicts = model.predict(x_test).argmax(axis=1)
labels = np.array([y.argmax() for y in y_test])
cl_report = metrics.classification_report(labels, predicts)
print(cl_report)
'''
