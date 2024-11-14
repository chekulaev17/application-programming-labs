import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for image processing.
    :return: Namespace containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Image processing: binarization and histogram")
    parser.add_argument("input_image_path", type=str, help="Path to the input image")
    parser.add_argument("output_image_path", type=str, help="Path for saving the result")
    parser.add_argument("--threshold", type=int, default=128, help="Порог для бинаризации (по умолчанию 128)")
    return parser.parse_args()