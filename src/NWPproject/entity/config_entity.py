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
    num_classes: int