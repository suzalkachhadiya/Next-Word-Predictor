from NWPproject.config.configuration import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_data(self)-> bool:
        try:
            validation_status = None
            # file_path = os.path.join('DataFile', 'xyz.txt')
            with open(self.config.Data_path, 'r') as f:
                content = f.readlines()
            
            if len(content)<50:
                print("no. of lines in data",len(content))
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
            else:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e