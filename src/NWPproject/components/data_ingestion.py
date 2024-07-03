import tkinter as tk
import os
from tkinter import filedialog
import shutil
from NWPproject.entity.config_entity import DataIngestionConfig, DataValidationConfig
from NWPproject.constants import *
from NWPproject.utils.common import update_nested_yaml

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def upload_and_save_text_file(self):
        files_in_folder = os.listdir(SAVED_FILE_PATH)
        first_file = files_in_folder[0]
        print("first_file:",first_file)
        file_path = os.path.join(SAVED_FILE_PATH, first_file)

        os.makedirs(self.config.destination_folder, exist_ok=True)
            
        # Define the destination path
        destination_path = os.path.join(self.config.destination_folder, first_file)

        update_nested_yaml(CONFIG_FILE_PATH, ['data_validation', 'Data_path'],destination_path)
        update_nested_yaml(CONFIG_FILE_PATH, ['data_transformation', 'Data_path'],destination_path)

        try:
                # Copy the file to the destination folder
                shutil.copy2(file_path, destination_path)
                print(f"File saved to: {destination_path}")
                
                # Read the content of the file
                with open(destination_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                
                return #{file_name: file_content}
        except Exception as e:
                print(f"Error: Unable to save or read {first_file}. {str(e)}")
                return #{}
        else:
            print("No file selected")
            return #{}