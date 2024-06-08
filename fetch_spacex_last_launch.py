import requests
from download_image import download_image


def fetch_spacex_last_launch(id):
    urlspx = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(urlspx)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for link_number, link in enumerate(links):
        download_image(link, f'spacex{link_number}.jpeg')


def main():
    id = '5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(id)


if __name__ == '__main__':
    main()
