import os

from icrawler.builtin import GoogleImageCrawler


def fetch_images(search_term: str, quantity: int, save_path: str) -> None:
    """
    Function for download the image by important word.
    :param search_term: Important word for search image.
    :param quantity: Number of image for download. (50-1000)
    :param save_path: Folder for saving images.
    """
    os.makedirs(save_path, exist_ok=True)
    crawler = GoogleImageCrawler(storage={'root_dir': save_path})
    crawler.crawl(keyword=search_term, max_num=quantity)
