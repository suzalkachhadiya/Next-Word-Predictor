import os
import numpy as np
from NWPproject.logging import logger
from NWPproject.config.configuration import ModelTrainerConfig
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        loaded_arrays = np.load(self.config.array_path)

        loaded_array1 = loaded_arrays['arr1']
        loaded_array2 = loaded_arrays['arr2']
        # loaded_array2=loaded_array2.flatten()

        print("Loaded array1:", type(loaded_array1))
        print("Loaded array2:", type(loaded_array2))

        print(loaded_array1.shape)
        print(loaded_array2.shape)

        model=Sequential()
        model.add(Embedding(self.config.input_dim,self.config.output_dim,input_length=self.config.input_length))
        model.add(LSTM(self.config.units_lstm))
        model.add(Dense(self.config.units_dense,activation=self.config.activation))

        model.compile(loss=self.config.loss,optimizer=self.config.optimizer,metrics=self.config.metrics)
        print(model.summary())

        model.fit(loaded_array1,loaded_array2,epochs=self.config.epoch)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))