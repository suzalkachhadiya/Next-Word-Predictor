from NWPproject.constants import *
from NWPproject.utils.common import read_yaml_file, create_directories
from NWPproject.entity.config_entity import DataIngestionConfig, DataValidationConfig

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