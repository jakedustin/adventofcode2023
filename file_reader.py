class FileReader:
    
    @staticmethod
    def read_lines(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except IOError as e:
            print(f"An error occurred: {e}")
            return []