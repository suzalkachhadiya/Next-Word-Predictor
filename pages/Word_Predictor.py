import streamlit as st
from NWPproject.pipline import prediction_pipeline
from NWPproject.config.configuration import ConfigurationManager
from NWPproject.components.prediction import PredictionPipeline

st.set_page_config(
    page_title="Word Predictor", 
    page_icon="⌨️",
    layout="wide"
)
# st.title(":shield: :blue[Phishing Catcher]")

st.markdown("""
    <style>
    .title-center {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #3498db;
    }
    .rainbow-divider {
        height: 2px;
        background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
        margin-top: 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-center">⌨️ Word Predictor ⌨️</h1>', unsafe_allow_html=True)
st.write("\n")
st.markdown('<div class="rainbow-divider"></div>', unsafe_allow_html=True)

st.write("\n")

user_input = st.text_input(" Type Two / More Words",placeholder="Type Here")
st.write(user_input)
st.write("\n")

# print(type(user_input))

if user_input:    
    config = ConfigurationManager()
    prediction_config = config.get_prediction_config()
    prediction= PredictionPipeline(config=prediction_config)
    predicted_words=prediction.predict(user_input)

    print(predicted_words)

    # st.header("", divider="rainbow")

    st.markdown('<div class="rainbow-divider"></div>', unsafe_allow_html=True)

    st.write(predicted_words[0])
    st.write(predicted_words[1])