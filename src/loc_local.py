import os
import time
import json
import argparse
import requests
from pprint import pprint
from flatten_json import flatten
from bs4 import BeautifulSoup

OUTPUT_DIR = "output"
TRACKING_FILE = "last_page.txt"

class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)
    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

class search_results_page:
    def __init__(self, base_url="https://www.loc.gov/collections",
                 collection="united-states-reports",
                 json_parameter="fo=json",
                 results_per_page="c=70",
                 query_param="?", page_param="sp=", page_num=1):

        print(f"Initializing page {page_num}")
        self.page_num = page_num
        self.search_url = self.create_search_url(base_url, collection, json_parameter, results_per_page, query_param, page_param, page_num)
        self.response = self.request_data()
        self.response_json = self.response_to_json()
        self.next_url = self.get_next_url()

    def request_data(self):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept-Encoding': 'identity'
        }
        return requests.get(self.search_url, headers=headers)

    def response_to_json(self):
        return self.response.json()

    def get_next_url(self):
        return self.response_json.get('pagination', {}).get('next', None)

    def create_search_url(self, base_url, collection, json_parameter,
                          results_per_page, query_param, page_param, page_num):
        page_query = f"{page_param}{page_num}"
        query = f"{query_param}{json_parameter}&{results_per_page}&{page_query}"
        return f"{base_url}/{collection}/{query}"

def search_result_generator(start_page=1, end_page=None):
    page_num = start_page
    while True:
        if end_page is not None and page_num > end_page:
            break
        time.sleep(1)
        obj = create_search_results_page_object(page_num=page_num)
        yield obj
        if not obj.next_url:
            break
        page_num += 1


def create_search_results_page_object(**kwargs):
    return search_results_page(**kwargs)

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def write_last_page_num(page_num):
    with open(TRACKING_FILE, 'w') as f:
        f.write(str(page_num))

def read_last_page_num():
    if not os.path.exists(TRACKING_FILE):
        return 1
    with open(TRACKING_FILE, 'r') as f:
        return int(f.read().strip())

def save_page_to_local_file(page_json, page_num):
    file_name = f"result-{page_num}.json"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    with open(file_path, "w") as f:
        json.dump(page_json, f, indent=2)
    print(f"Saved: {file_path}")

def parse_args():
    parser = argparse.ArgumentParser(description="Library of Congress Scraper (Local)")
    parser.add_argument(
        "--start-page", type=int, default=None,
        help="Page number to start scraping from (overrides last_page.txt)"
    )
    parser.add_argument(
        "--end-page", type=int, default=None,
        help="Optional page number to stop scraping after"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    ensure_output_dir()

    # Determine starting point
    start_page = args.start_page if args.start_page else read_last_page_num()
    end_page = args.end_page

    print(f"Scraping from page {start_page}" + (f" to {end_page}" if end_page else ""))

    for obj in search_result_generator(start_page=start_page, end_page=end_page):
        page_num = obj.page_num
        print(f"Processing page: {page_num}")
        save_page_to_local_file(obj.response_json, page_num)
        write_last_page_num(page_num)
        print(f"Completed page: {page_num}\n")


if __name__ == "__main__":
    main()
