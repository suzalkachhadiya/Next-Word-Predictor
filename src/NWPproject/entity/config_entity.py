from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    destination_folder: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    Data_path: Path
    STATUS_FILE: str

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    Data_path: Path
    padding: str
    tokenizer_name: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    array_path: Path
    model_name: str
    units_lstm: int
    units_dense: int
    activation: str
    input_dim: int
    output_dim: int
    input_length:int
    loss: str
    optimizer: str
    metrics: list
    epoch: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    array_path: Path
    metric_file_name: Path

@dataclass(frozen=True)
class PredictionConfig:
    input_length:int