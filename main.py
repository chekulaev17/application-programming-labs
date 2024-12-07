from addcol import add_image_dimensions
from area import add_image_area, sort_by_area
from dimen import calculate_statistics, filter_by_dimensions
from func import parse_arguments
from gendf import generate_dataframe
from hist import plot_area_histogram


def main() -> None:
    """
    Main process for annotation and image analysis.
    """
    try:
        args = parse_arguments()
        df = generate_dataframe(args.annotation)
        add_image_dimensions(df)
        print("Statistics for image dimensions:")
        print(calculate_statistics(df))
        filtered_df = filter_by_dimensions(df, args.max_height, args.max_width)
        print("Filtered data:")
        print(filtered_df)
        add_image_area(df)
        df = sort_by_area(df)
        print("Data after sorting by area:")
        print(df)
        plot_area_histogram(df)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
