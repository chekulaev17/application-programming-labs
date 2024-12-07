import cv2

import pandas as pd


def add_image_dimensions(df: pd.DataFrame) -> None:
    """
    Adds columns for image dimensions: height, width, depth.
    :param df: DataFrame with image paths.
    :return: DataFrame with added 'height', 'width', 'depth' columns.
    """
    heights, widths, depths = [], [], []
    for path in df['absolute_path']:
        img = cv2.imread(path)
        if img is None:
            heights.append(None)
            widths.append(None)
            depths.append(None)
        else:
            heights.append(img.shape[0])
            widths.append(img.shape[1])
            depths.append(img.shape[2])
    df['height'], df['width'], df['depth'] = heights, widths, depths
