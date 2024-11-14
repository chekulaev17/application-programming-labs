import argparse
import cv2 as cv
import numpy as np
import os

from matplotlib import pyplot as plt


def load_image(path: str) -> np.ndarray:
    """
    Loads an image from the specified path.
    :param path: Path to the image file.
    :return: Image as a numpy ndarray.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")
    image = cv.imread(path)
    if image is None:
        raise ValueError("Image loading error: the file format may not be supported.")
    return image


def display_image_info(image: np.ndarray) -> None:
    """
    Displays the dimensions and number of channels of an image.
    :param image: Image as a numpy ndarray.
    :return: None.
    """
    height, width, channels = image.shape
    print(f"Image size: {width}x{height} (width x height), channels: {channels}")


def compute_histogram(image: np.ndarray) -> dict:
    """
    Computes the histogram for each color channel (blue, green, red) of an image.
    :param image: Image as a numpy ndarray.
    :return: Dictionary containing histograms for each color channel.
    """
    histogram = {}
    for i, color in enumerate(('blue', 'green', 'red')):
        histogram[color] = cv.calcHist([image], [i], None, [256], [0, 256])
    return histogram


def plot_histogram(histogram: dict) -> None:
    """
    Displays the histogram for each color channel of the image.
    :param histogram: Dictionary containing histograms for each color channel.
    :return: None.
    """
    plt.figure(figsize=(10, 5))
    plt.title("Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Pixel Count")
    for color, hist in histogram.items():
        plt.plot(hist, color=color, label=f'{color.capitalize()} channel')
    plt.legend()
    plt.grid()
    plt.show()


def binarize_image(image: np.ndarray, threshold: int = 128) -> np.ndarray:
    """
    Converts an image to a binary image using a specified threshold.
    :param image: Image as a numpy ndarray.
    :param threshold: Threshold value for binarization (default is 128).
    :return: Binary image as a numpy ndarray.
    """
    grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(grayscale, threshold, 255, cv.THRESH_BINARY)
    return binary_image


def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Saves an image to the specified path.
    :param image: Image to be saved, as a numpy ndarray.
    :param output_path: Path where the image will be saved.
    :return: None. Prints success or error message upon saving.
    """
    success = cv.imwrite(output_path, image)
    if success:
        print(f"Image successfully saved to: {output_path}")
    else:
        print(f"Error saving image to: {output_path}")


def display_images(original: np.ndarray, transformed: np.ndarray) -> None:
    """
    Displays the original and transformed (binary) images side by side.
    :param original: Original image as a numpy ndarray.
    :param transformed: Transformed (binary) image as a numpy ndarray.
    :return: None.
    """
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv.cvtColor(original, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title("Binary Image")
    plt.imshow(transformed, cmap='gray')
    plt.axis('off')
    plt.show()


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for image processing.
    :return: Namespace containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Image processing: binarization and histogram")
    parser.add_argument("input_image_path", type=str, help="Path to the input image")
    parser.add_argument("output_image_path", type=str, help="Path for saving the result")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    try:
        image = load_image(args.input_image_path)
        display_image_info(image)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return
    histogram = compute_histogram(image)
    plot_histogram(histogram)
    binary_image = binarize_image(image, args.threshold)
    display_images(image, binary_image)
    save_image(binary_image, args.output_image_path)


if __name__ == "__main__":
    main()
