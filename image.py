import os
import cv2 as cv
import numpy as np


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


def save_image(image: np.ndarray, output_path: str) -> bool:
    """
    Saves an image to the specified path.
    :param image: Image to be saved, as a numpy ndarray.
    :param output_path: Path where the image will be saved.
    :return: True if image was saved successfully, False otherwise.
    """
    return cv.imwrite(output_path, image)


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
