import argparse
import csv
import os


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.
    :return: Namespace with parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Analyze images based on annotations.")
    parser.add_argument("--annotation", required=True, help="Path to the annotation file (CSV).")
    parser.add_argument("--max_height", type=int, required=True, help="Maximum image height.")
    parser.add_argument("--max_width", type=int, required=True, help="Maximum image width.")
    return parser.parse_args()


def generate_annotation(images_dir: str, csv_file: str) -> None:
    """
    Creates a CSV file with annotations containing absolute and relative paths to images.
    :param images_dir: Path to the folder containing images.
    :param csv_file: Path to the output CSV file for annotations.
    """
    if not os.path.isdir(images_dir):
        raise FileNotFoundError(f"The specified directory does not exist: {images_dir}")

    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)

            # Headers must match the expected format of the main program
            csv_writer.writerow(['absolute_path', 'relative_path'])

            # Iterate through image files in the directory
            for image_file in filter(lambda f: f.lower().endswith(('.jpg', '.jpeg', '.png')), os.listdir(images_dir)):
                abs_path = os.path.abspath(os.path.join(images_dir, image_file))
                rel_path = os.path.relpath(abs_path, start=os.getcwd())  # Relative to the current working directory
                csv_writer.writerow([abs_path, rel_path])

        print(f"Annotation file created successfully at: {csv_file}")

    except Exception as e:
        print(f"An error occurred while creating the annotation file: {e}")

