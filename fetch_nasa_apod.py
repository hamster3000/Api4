import requests
from urllib.parse import urlparse, unquote
import os
from download_image import download_image
from dotenv import load_dotenv


def get_ext_file(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    path, full_name = os.path.split(parsed_url.path)
    file_name, extention = os.path.splitext(full_name)
    return file_name, extention


def fetch_nasa_apod(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "count": 3}
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_links = response.json()
    for apod_link in apod_links:
        if apod_link.get('media_type') == 'image':
            nasa_link_image = apod_link['url'] or apod_link['hdurl']
        file_name, extention = get_ext_file(nasa_link_image)
        download_image(nasa_link_image, f'{file_name}{extention}')


def main():
    load_dotenv()
    api_key = os.environ['NASA_TOKEN']
    fetch_nasa_apod(api_key)


if __name__ == '__main__':
    main()
