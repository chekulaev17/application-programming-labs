from histogram import compute_histogram, plot_histogram
from image import display_images, load_image, binarize_image, save_image, display_image_info
from parser import parse_arguments


def main() -> None:
    args = parse_arguments()
    try:
        image = load_image(args.input_image_path)
        display_image_info(image)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return
    histogram = compute_histogram(image)
    plot_histogram(histogram)
    binary_image = binarize_image(image, args.threshold)
    display_images(image, binary_image)
    save_image(binary_image, args.output_image_path)


if __name__ == "__main__":
    main()
