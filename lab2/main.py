from annotation import generate_annotation
from crawler import fetch_images
from iterator import ImageAnnotationIterator
from parser import parse_cli_args


def main():
    try:
        args = parse_cli_args()
        fetch_images(args.search_keyword, args.image_count, args.output_folder)
        generate_annotation(args.output_folder, args.csv_annotation)
        print("Iterating over images:")
        iterator = ImageAnnotationIterator(
            args.csv_annotation if args.from_csv else args.output_folder, from_csv=args.from_csv
        )
        for annotation in iterator:
            if args.from_csv:
                print(f"Absolute Path: {annotation[0]}, Relative Path: {annotation[1]}")
            else:
                print(f"Image Path: {annotation}")
    except Exception as e:
        print(f"Error in the main function: {e}")


if __name__ == "__main__":
    main()

