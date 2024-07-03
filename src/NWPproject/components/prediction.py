import joblib
from NWPproject.entity.config_entity import PredictionConfig
from NWPproject.logging import logger
import numpy as np
from NWPproject.constants import *
from tensorflow.keras.preprocessing.sequence import pad_sequences


class PredictionPipeline:
    def __init__(self,config:PredictionConfig):
        self.config = config
        self.model = joblib.load(TRAINED_MODEL_PATH)
        self.token = joblib.load(TOKEN_PATH)

    def predict(self, data):        
        res=[]

        print(data)

        for i in range(len(data.split(" "))):
            token_text=self.token.texts_to_sequences([data])[0]

            print(token_text)

            padded_token_text=pad_sequences([token_text],maxlen=self.config.input_length,padding="pre")

            idx=np.argmax(self.model.predict(padded_token_text))

            for word,index in self.token.word_index.items():
                if index==idx:
                    data=data+" "+ word
                    res.append( data)

        # prediction = int(self.model.predict(data))
        logger.info(f"Predicted Word: {res}")
        return res