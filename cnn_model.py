import os
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

base_dir = 'D:/EVENT/BANGKIT 2023/Dataset Capstone/Pedaging'

bahan_dir = os.path.join(base_dir, 'Bahan')
train_dir = os.path.join(base_dir, 'latih')
valid_dir = os.path.join(base_dir, 'validasi')

starter_dir = os.path.join(bahan_dir, 'Starter/')
finisher_dir = os.path.join(bahan_dir, 'Finisher/')

#print("jumlah data train tiap kelas")
#print("jumlah gambar ayam fase starter :", len(os.listdir(starter_dir)))
#print("jumlah gambar ayam fase finisher :", len(os.listdir(finisher_dir)))

#direktori isi train
train_starter = os.path.join(train_dir, 'Starter/')
train_finisher = os.path.join(train_dir, 'Finisher/')

#direktori isi validasi
validation_starter = os.path.join(valid_dir, 'Starter/')
validation_finisher = os.path.join(valid_dir, 'Finisher/')


##definisikan data
import random
from shutil import copyfile

def train_val_split(source, train, val, train_rato):
    total_size = len(os.listdir(source))
    train_size = int(train_ratio*total_size)
    val_size = total_size - train_size
    
    randomized = random.sample(os.listdir(source), total_size)
    train_files = randomized[0:train_size]
    val_files = randomized[train_size:total_size]
    
    for i in train_files:
        i_file = source + i
        destination = train + i
        copyfile(i_file, destination)
    
    for i in val_files:
        i_file = source + i
        destination = val + i
        copyfile(i_file, destination)
        
# jmlh pembagian data train dan test
train_ratio = 0.9

#pembagian training dan validasi
#training
source_00 = starter_dir
train_00 = train_starter
val_00 = validation_starter
train_val_split(source_00, train_00, val_00, train_ratio)

#validasi
source_01 = starter_dir
train_01 = train_finisher
val_01 = validation_finisher
train_val_split(source_01, train_01, val_01, train_ratio)

#print('jumlah semua yang starter :', len(os.listdir(starter_dir)))
#print('jumlah train starter :', len(os.listdir(train_starter)))
#print('jumlah val starter :', len(os.listdir(validation_starter)))

## PRE PROCESSING
train_datagen = ImageDataGenerator(
                rescale = 1./255,
                rotation_range = 30,
                horizontal_flip = True,
                shear_range = 0.3,
                fill_mode = 'nearest',
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                zoom_range = 0.1)

val_datagen = ImageDataGenerator(
                rescale = 1./255,
                rotation_range = 30,
                horizontal_flip = True,
                shear_range = 0.3,
                fill_mode = 'nearest',
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                zoom_range = 0.1)


train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size = (150, 150),
    batch_size = 10,
    class_mode = 'categorical')

val_generator = val_datagen.flow_from_directory(
    valid_dir,
    target_size = (150, 150),
    batch_size = 10,
    class_mode = 'categorical')

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs = {}):
        if(logs.get('accuracy') > 0.99):
            print('\nAkurasi mencapai 99%')
            self.model.stop_training = True
            
callbacks = myCallback()

## MODEL CNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation = 'relu', input_shape = (150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(200, activation = 'relu'),
    tf.keras.layers.Dropout(0.3, seed=112),
    tf.keras.layers.Dense(500, activation = 'relu'),
    tf.keras.layers.Dropout(0.5, seed=112),
    tf.keras.layers.Dense(2, activation = 'sigmoid')
])

model.summary()
model.compile(loss = 'categorical_crossentropy',
             optimizer = 'Adam',
             metrics = ['accuracy'])

history = model.fit(
            train_generator,
            steps_per_epoch = 2,
            epochs = 20,
            validation_data = val_generator,
            validation_steps = 1,
            verbose = 1,
            callbacks = [callbacks]
)
