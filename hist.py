import pandas as pd
import matplotlib.pyplot as plt


def plot_area_histogram(df: pd.DataFrame) -> None:
    """
    Plots a histogram of image area distribution.
    :param df: DataFrame with an 'area' column.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['area'].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Image Areas')
    plt.xlabel('Area (pixels)')
    plt.ylabel('Number of Images')
    plt.grid(True)
    plt.show()
