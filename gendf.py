import os

import pandas as pd


def generate_dataframe(annotation_path: str) -> pd.DataFrame:
    """
    Creates a DataFrame with absolute and relative paths to images.
    :param annotation_path: Path to the annotation file (CSV).
    :return: DataFrame with 'absolute_path' and 'relative_path' columns.
    """
    if not os.path.isfile(annotation_path):
        raise FileNotFoundError(f"Annotation file {annotation_path} not found.")
    df = pd.read_csv(annotation_path)
    df.columns = ['absolute_path', 'relative_path']
    return df