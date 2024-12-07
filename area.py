import pandas as pd


def add_image_area(df: pd.DataFrame) -> None:
    """
    Adds a column 'area' containing the image area.
    :param df: DataFrame with image dimensions.
    :return: DataFrame with an added 'area' column.
    """
    df['area'] = df['height'] * df['width']


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the DataFrame by image area.
    :param df: DataFrame with an 'area' column.
    :return: Sorted DataFrame.
    """
    return df.sort_values(by='area').reset_index(drop=True)