from os.path import basename, splitext
from urllib.parse import urlsplit, unquote
from requests import get


def download_image(url: str, file_name: str) -> None:
    response = get(url)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)
    file.closed


def checks_format(url_img: str) -> str:
    name_image = unquote(basename(urlsplit(url_img).path))
    format_image = splitext(name_image)[1]

    return format_image
