from data_processor import DataProcessor

class BaseSolution:
    def __init__(self, input_data):
        if input_data == "s":
            # get short input data
            self.input_data = DataProcessor.process_data(self.get_file_name() + "small-input.txt")
        elif input_data == "l":
            # get long input data
            self.input_data = DataProcessor.process_data(self.get_file_name() + "large-input.txt")
        else:
            raise NotImplementedError("This is not a valid solution: " + str(input_data))
    
    def get_file_name(self):
        raise NotImplementedError("Subclasses should implement this!")

    def solve(self):
        raise NotImplementedError("Subclasses should implement this!")
