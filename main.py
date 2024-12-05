import argparse
import csv
import cv2
import os

import pandas as pd
import matplotlib.pyplot as plt


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
            csv_writer.writerow(['absolute_path', 'relative_path'])
            for image_file in filter(lambda f: f.lower().endswith(('.jpg', '.jpeg', '.png')), os.listdir(images_dir)):
                abs_path = os.path.abspath(os.path.join(images_dir, image_file))
                rel_path = os.path.relpath(abs_path, start=os.getcwd()) 
                csv_writer.writerow([abs_path, rel_path])
        print(f"Annotation file created successfully at: {csv_file}")
    except Exception as e:
        print(f"An error occurred while creating the annotation file: {e}")


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


def add_image_dimensions(df: pd.DataFrame) -> pd.DataFrame:
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
    return df


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


def add_image_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a column 'area' containing the image area.
    :param df: DataFrame with image dimensions.
    :return: DataFrame with an added 'area' column.
    """
    df['area'] = df['height'] * df['width']
    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the DataFrame by image area.
    :param df: DataFrame with an 'area' column.
    :return: Sorted DataFrame.
    """
    return df.sort_values(by='area').reset_index(drop=True)


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


def main() -> None:
    """
    Main process for annotation and image analysis.
    """
    try:
        args = parse_arguments()
        df = generate_dataframe(args.annotation)
        df = add_image_dimensions(df)
        print("Statistics for image dimensions:")
        print(calculate_statistics(df))
        filtered_df = filter_by_dimensions(df, args.max_height, args.max_width)
        print("Filtered data:")
        print(filtered_df)
        df = add_image_area(df)
        df = sort_by_area(df)
        print("Data after sorting by area:")
        print(df)
        plot_area_histogram(df)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
