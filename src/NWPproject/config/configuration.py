from NWPproject.constants import *
from NWPproject.utils.common import read_yaml_file, create_directories
from NWPproject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, PredictionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        # schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)
        # self.schema = read_yaml_file(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            destination_folder=config.destination_folder
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            Data_path=config.Data_path,
            STATUS_FILE=config.STATUS_FILE
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        padding_params=self.params.pad_sequences

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            Data_path=config.Data_path,
            padding=padding_params.padding,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        units_lstm_params = self.params.LSTM
        units_dense_params = self.params.Dense
        activation_params = self.params.Dense
        input_dim_params = self.params.Embedding
        output_dim_params = self.params.Embedding
        input_length_params = self.params.Embedding
        loss_params = self.params.compile
        optimizer_params = self.params.compile
        metrics_params = self.params.compile
        epoch_params = self.params.fit

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            array_path=config.array_path,
            model_name=config.model_name,
            units_lstm= units_lstm_params.units_lstm,
            units_dense = units_dense_params.units_dense,
            activation = activation_params.activation,
            input_dim = input_dim_params.input_dim,
            output_dim = output_dim_params.output_dim,
            input_length = input_length_params.input_length,
            loss = loss_params.loss,
            optimizer = optimizer_params.optimizer,
            metrics = metrics_params.metrics,
            epoch = epoch_params.epoch
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_path = config.model_path,
            array_path=config.array_path,
            metric_file_name = config.metric_file_name,           
        )

        return model_evaluation_config
    
    def get_prediction_config(self) -> PredictionConfig:
        # config = self.config.prediction
        input_length_params = self.params.Embedding

        prediction_config = PredictionConfig(
            input_length = input_length_params.input_length  
        )

        return prediction_config