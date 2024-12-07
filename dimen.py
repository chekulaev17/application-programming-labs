import pandas as pd


def calculate_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates descriptive statistics for 'height', 'width', and 'depth' columns.
    :param df: DataFrame containing image dimensions.
    :return: DataFrame with descriptive statistics.
    """
    return df[['height', 'width', 'depth']].describe()


def filter_by_dimensions(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    Filters the DataFrame by maximum image height and width.
    :param df: Original DataFrame.
    :param max_height: Maximum image height.
    :param max_width: Maximum image width.
    :return: Filtered DataFrame.
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]