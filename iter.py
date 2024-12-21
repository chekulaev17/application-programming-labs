import csv
import os


class PigsIterator:
    def __init__(self, path_to_csv: str):
        self.path_to_csv = path_to_csv
        if not os.path.exists(self.path_to_csv):
            raise FileNotFoundError(f"The specified file does not exist: {self.path_to_csv}")


    def __iter__(self):
        """Initialize the iterator."""
        self.file = open(self.path_to_csv, 'r')
        self.csvreader = csv.reader(self.file)
        try:
            header = next(self.csvreader) 
            if not header:
                raise ValueError("CSV file is empty or missing a header.")
        except StopIteration:
            self.file.close()
            raise ValueError("CSV file is empty.")
        return self


    def __next__(self):
        """Return the next image path."""
        try:
            return next(self.csvreader)[0]  
        except StopIteration:
            self.file.close()
            raise StopIteration
