import tkinter as tk
import os
from tkinter import filedialog
import shutil
from NWPproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def upload_and_save_text_file(self):

        root = tk.Tk()
        # root.withdraw()  # Hide the main window

        # Select the source file
        source_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if source_path:
            file_name = os.path.basename(source_path)
            print(f"Selected file: {file_name}")
            
            # Create the destination folder if it doesn't exist
            os.makedirs(self.config.destination_folder, exist_ok=True)
            
            # Define the destination path
            destination_path = os.path.join(self.config.destination_folder, file_name)
            
            try:
                # Copy the file to the destination folder
                shutil.copy2(source_path, destination_path)
                print(f"File saved to: {destination_path}")
                
                # Read the content of the file
                with open(destination_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                
                return #{file_name: file_content}
            except Exception as e:
                print(f"Error: Unable to save or read {file_name}. {str(e)}")
                return #{}
        else:
            print("No file selected")
            return #{}