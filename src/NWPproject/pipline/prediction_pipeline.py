from NWPproject.config.configuration import ConfigurationManager
from NWPproject.components.prediction import PredictionPipeline

try:
    config = ConfigurationManager()
    prediction_config = config.get_prediction_config()
    prediction= PredictionPipeline(config=prediction_config)
    PW=prediction.predict("big story")
except Exception as e:
    raise e