import csv
import os
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QSizePolicy, QMessageBox
)


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
            header = next(self.csvreader)  # Skip header
            if not header:
                raise ValueError("CSV file is empty or missing a header.")
        except StopIteration:
            self.file.close()
            raise ValueError("CSV file is empty.")
        return self


    def __next__(self):
        """Return the next image path."""
        try:
            return next(self.csvreader)[0]  # Image path is in the first column
        except StopIteration:
            self.file.close()
            raise StopIteration


class ImageViewer(QMainWindow):


    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setFixedSize(QSize(1280, 700))

        self.dataset_iterator = None
        self.current_image_path = None

        self.setup_ui()


    def setup_ui(self) -> None:
        """
        Set up the user interface.
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.image_label)
        self.load_dataset_button = QPushButton("Load Dataset")
        self.load_dataset_button.setFixedSize(1000, 50)
        self.load_dataset_button.clicked.connect(self.load_dataset)
        layout.addWidget(self.load_dataset_button)
        self.next_image_button = QPushButton("Next Image")
        self.next_image_button.setFixedSize(1000, 50)
        self.next_image_button.clicked.connect(self.show_next_image)
        self.next_image_button.setEnabled(False)
        layout.addWidget(self.next_image_button)


    def load_dataset(self) -> None:
        """
        Open a CSV file and initialize the dataset iterator.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Dataset Annotation File", "", "CSV Files (*.csv)"
        )
        if file_path:
            try:
                self.dataset_iterator = iter(PigsIterator(file_path))  # Initialize the iterator
                self.next_image_button.setEnabled(True)
                self.show_next_image()  # Show the first image
            except (FileNotFoundError, ValueError) as e:
                QMessageBox.critical(self, "Error", str(e))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Unexpected error: {e}")


    def show_next_image(self) -> None:
        """
        Show the next image from the dataset iterator.
        """
        if self.dataset_iterator:
            try:
                self.current_image_path = next(self.dataset_iterator)  # Get the next image path
                if os.path.exists(self.current_image_path):
                    self.display_image(self.current_image_path)
                else:
                    raise FileNotFoundError(f"Image not found: {self.current_image_path}")
            except StopIteration:
                QMessageBox.information(self, "End of Dataset", "No more images in the dataset.")
                self.next_image_button.setEnabled(False)
            except FileNotFoundError as e:
                QMessageBox.warning(self, "File Not Found", str(e))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Unexpected error: {e}")


    def display_image(self, image_path: str) -> None:
        """
        Display the image in QLabel.

        :param image_path: Path to the image file.
        """
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                raise ValueError("Invalid image file.")

            self.image_label.setPixmap(pixmap.scaled(
                self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error displaying image: {e}")


def main():
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

