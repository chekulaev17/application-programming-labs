import os
import csv


class ImageAnnotationIterator:
    """
    iterator passing for csv annotation with path to images or for images in specified folder.
    """
    def __init__(self, source: str, from_csv: bool = True):
        """
        :param source: Path to csv file with annotation or folder with images.
        :param from_csv: If True, source — CSV file, if False — folder
        """
        self.source = source
        self.from_csv = from_csv


    def __iter__(self):
        """
        Preparing iterator for sorting images.
        :return: self - for iteration by image.
        """
        if self.from_csv:
            self.file = open(self.source, mode='r', encoding='utf-8')
            self.reader = csv.reader(self.file)
            next(self.reader)
        else:
            self.images = iter(
                [os.path.join(self.source, img) for img in os.listdir(self.source)
                 if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
            )
        return self


    def __next__(self):
        """
         Returns the next element from the image source.
         :return: The next path to the image (absolute and relative paths when using CSV).
         :raises StopIteration: If the end of the source (CSV file or list of images) is reached.
        """
        if self.from_csv:
            try:
                return next(self.reader)
            except StopIteration:
                self.file.close()
                raise
        else:
            return next(self.images)
