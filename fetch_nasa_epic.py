import requests
from datetime import datetime
from download_image import download_image
import os
from dotenv import load_dotenv

def nasa_epic(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": api_key, "count": 3}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_links = response.json()
    for epic_link in epic_links:
        date = epic_link['date']
        form_date = datetime.fromisoformat(date).strftime("%Y/%m/%d")
        name = epic_link['image']
        url_epic = f"https://api.nasa.gov/EPIC/archive/natural/{form_date}/png/{name}.png"
        download_image(url_epic, f'{name}.png', params)


def main():
    load_dotenv()
    api_key = os.environ['NASA_TOKEN']
    nasa_epic(api_key)


if __name__ == '__main__':
    main()
