import requests
def download_image(url, file_name, params=None):
    file_path = f'images/{file_name}'

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def main():
    download_image(url, file_name, params=None)
if __name__ == '__main__':
    main()