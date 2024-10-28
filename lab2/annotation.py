import csv
import os


def generate_annotation(images_dir: str, csv_file: str) -> None:
    """
    Function for creating CSV-file with annotations with absolute and relative path to image.
    :param images_dir: Path to folder with images.
    :param csv_file: Path to csv file annotation.
    """
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Absolute Path', 'Relative Path'])
        for image_file in filter(lambda f: f.lower().endswith(('.jpg', '.jpeg', '.png')), os.listdir(images_dir)):
            abs_path = os.path.abspath(os.path.join(images_dir, image_file))
            rel_path = os.path.relpath(abs_path, start=images_dir)
            csv_writer.writerow([abs_path, rel_path])

