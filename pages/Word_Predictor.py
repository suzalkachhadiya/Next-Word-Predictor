import streamlit as st
from NWPproject.pipline import prediction_pipeline
from NWPproject.config.configuration import ConfigurationManager
from NWPproject.components.prediction import PredictionPipeline

user_input = st.text_input("Type something:",placeholder="Type Here")
st.write(user_input)

# print(type(user_input))

if user_input:    
    config = ConfigurationManager()
    prediction_config = config.get_prediction_config()
    prediction= PredictionPipeline(config=prediction_config)
    predicted_words=prediction.predict(user_input)

    print(predicted_words)

    st.write(predicted_words[0])
    st.write(predicted_words[1])