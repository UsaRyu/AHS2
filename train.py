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
    "processed_hand_data/train",
    target_size=(64, 64),
    batch_size=4)
validation_generator = validation_datagen.flow_from_directory(
    "processed_hand_data/validation",
    target_size=(64, 64),
    batch_size=4)
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