from file_reader import FileReader

class DataProcessor:

    @staticmethod
    def process_data(file_path):
        lines = FileReader.read_lines(file_path)
        return lines