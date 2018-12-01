#importing the Keras libraries and packages
import h5py
from keras import optimizers
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator

slClassifer = Sequential()

slClassifer.add(Conv2D(32, (7, 7), strides=2, input_shape = (64, 64, 3), activation = 'relu'))
slClassifer.add(MaxPooling2D(pool_size=(3, 3), strides=2))
slClassifer.add(BatchNormalization(axis=3, scale=False))

slClassifer.add(Conv2D(80, (1, 1), padding='valid', activation='relu'))
slClassifer.add(Conv2D(192, (3, 3), padding='valid', activation='relu'))
slClassifer.add(BatchNormalization(axis=3, scale=False))
slClassifer.add(MaxPooling2D(pool_size=(3, 3), strides=2))

slClassifer.add(Conv2D(80, (1, 1), padding='valid', activation='relu'))
slClassifer.add(Conv2D(192, (3, 3), padding='valid', activation='relu'))
slClassifer.add(BatchNormalization(axis=3, scale=False))
slClassifer.add(MaxPooling2D(pool_size=(3, 3), strides=2))

slClassifier.add(Flatten())

slClassifier.add(Dense(256, activation = 'relu'))
slClassifier.add(Dropout(0.5))
slClassifier.add(Dense(26, activation = 'softmax'))

slClassifier.compile(optimzers.SGD(lr = 0.01), loss = 'categorical_crossentropy', metrics = ['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'mydata/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

test_set = test_datagen.flow_from_directory(
        'mydata/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

model = classifier.fit_generator(
        training_set,
        steps_per_epoch=800,
        epochs=25,
        validation_data = test_set,
        validation_steps = 6500
      )

#Saving the model
classifier.save('ASL_Model.h5')

print(model.history.keys())

# summarize history for accuracy
plt.plot(model.history['acc'])
plt.plot(model.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss

plt.plot(model.history['loss'])
plt.plot(model.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
