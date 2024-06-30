import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from NWPproject.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def data_transformation(self):
        with open(self.config.Data_path, 'r') as f:
            data = f.read()

        tokenizer=Tokenizer()

        tokenizer.fit_on_texts([data])

        input_seq=[]
        for sentence in data.split("\n"):
            tokenized_sentence=tokenizer.texts_to_sequences([sentence])[0]
            for i in range(1,len(tokenized_sentence)):
                n_gram=tokenized_sentence[:i+1]
                input_seq.append(n_gram)

        max_len=max([len(i) for i in input_seq])

        padded_input_seq=pad_sequences(input_seq,maxlen=max_len,padding=self.config.padding)

        X=padded_input_seq[:,:-1]
        Y=padded_input_seq[:,-1]

        # print(X.shape)
        # print(Y.shape)

        y=to_categorical(Y,num_classes=self.config.num_classes)

        # print(type(X))
        # print(type(y))

        file_path=os.path.join(self.config.root_dir,"arrays.npz")
        np.savez(file_path, arr1=X, arr2=y, arr3=Y)
        