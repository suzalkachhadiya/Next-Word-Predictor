from tensorflow.keras.losses import sparse_categorical_crossentropy
import numpy as np
from pathlib import Path
import joblib
from NWPproject.utils.common import save_json_file
from NWPproject.config.configuration import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, model, X, y, Y):
        loss = sparse_categorical_crossentropy(Y,model.predict(X))
        perplexity = np.exp(np.mean(loss))

        _, accuracy = model.evaluate(X, y, verbose=0)

        return perplexity, accuracy

    
    def save_results(self):

        model = joblib.load(self.config.model_path)

        loaded_arrays = np.load(self.config.array_path)

        loaded_array1 = loaded_arrays['arr1']
        loaded_array2 = loaded_arrays['arr2']
        loaded_array3 = loaded_arrays['arr3']
        

        (perplexity, accuracy) = self.eval_metrics(model,loaded_array1,loaded_array2, loaded_array3)
        
        # Saving metrics as local
        scores = {"perplexity": float(perplexity), "accuracy": float(accuracy)}
        print(scores)
        print(type(scores))
        save_json_file(file_path=Path(self.config.metric_file_name), data=scores)