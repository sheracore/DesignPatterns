from abc import ABC, abstractmethod

# Template Base Class
class DataProcessor(ABC):
    """Defines the skeleton for data processing"""

    def process(self):
        """Template method defining the steps of the algorithm"""
        self.read_data()
        self.parse_data()
        self.save_data()

    def read_data(self):
        """Common step for all subclasses"""
        print("Reading data from source...")

    @abstractmethod
    def parse_data(self):
        """Abstract step to be implemented by subclasses"""
        pass

    def save_data(self):
        """Common step for all subclasses"""
        print("Saving processed data...\n")


# Concrete Subclasses
class CSVProcessor(DataProcessor):
    def parse_data(self):
        print("Parsing CSV data...")


class JSONProcessor(DataProcessor):
    def parse_data(self):
        print("Parsing JSON data...")


# Example Usage
csv_processor = CSVProcessor()
csv_processor.process()
# Output:
# Reading data from source...
# Parsing CSV data...
# Saving processed data...

json_processor = JSONProcessor()
json_processor.process()
# Output:
# Reading data from source...
# Parsing JSON data...
# Saving processed data...