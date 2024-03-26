import argparse
import logging
import multiprocessing
import threading

import requests

from app_async import main_async

url = "https://media.geeksforgeeks.org/wp-content/uploads/20221014220743/karma.png"

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


def download_image(url):
    data = requests.get(url).content
    return data


def write_data(data, filename):
    with open(filename, "wb") as f:
        f.write(data)


def process(url, filename_prefix):
    data = download_image(url)
    filename = f"{filename_prefix}.png"
    write_data(data, filename)


def main(urls):
    for i, url in enumerate(urls):
        process(url, str(i))


def main_thread(urls):
    threads = []
    for i, v in enumerate(urls):
        t = threading.Thread(target=process, args=(v, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    logger.info("All threads exited")


def main_proc(urls):
    processes = []
    for i, v in enumerate(urls):
        t = multiprocessing.Process(target=process, args=(v, i))
        processes.append(t)
        t.start()
    for t in processes:
        t.join()
    logger.info("All processes exited")


CONCURRENCY_TYPES = {
    "single": main,
    "thread": main_thread,
    "proc": main_proc,
    "async": main_async,
}


def concurrency_type_factory(concurrency_type_identifier):
    return CONCURRENCY_TYPES.get(concurrency_type_identifier)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Image download", description="Download images from the web"
    )
    parser.add_argument("urls", metavar="u", type=str, nargs="*")
    parser.add_argument(
        "-c",
        "--concurrency",
        metavar="c",
        choices=CONCURRENCY_TYPES.keys(),
        default="single",
    )
    args = parser.parse_args()

    if args.urls:
        if f := concurrency_type_factory(args.concurrency):
            logger.info(f"concurrency type {args.concurrency}")
            f(args.urls)
    else:
        print("Urls was not provided")
