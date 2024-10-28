import argparse


def parse_cli_args() -> argparse.Namespace:
    """
    Parser cmd arguments for get parameters.
    :return: cmd arguments
    """
    parser = argparse.ArgumentParser(description="Image downloader, annotator, and iterator.")
    parser.add_argument('search_keyword', type=str, help="Ключевое слово для поиска изображений")
    parser.add_argument('output_folder', type=str, help="Папка для сохранения изображений")
    parser.add_argument('csv_annotation', type=str, help="Файл CSV для аннотаций")
    parser.add_argument('image_count', type=int, choices=range(50, 1001), help="Количество изображений для загрузки (от 50 до 1000)")
    parser.add_argument('--from_csv', action='store_true', help="Использовать CSV файл как источник для итерации")
    return parser.parse_args()

