import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt


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