from requests import get
from download_and_checks_image import download_image

SPACE_X_API = 'https://api.spacexdata.com/v5/launches'
SPACE_X_PATH = 'images/space_x_'
JPG_FORMAT = '.jpg'


def fetch_spacex_last_launch(id: str) -> None:

    response = get(f'{SPACE_X_API}/{id}')
    response.raise_for_status()
    
    space_x_images = response.json()['links']['flickr']['original']
    numbered_images = enumerate(space_x_images)

    if numbered_images:
        for num, link in numbered_images:
            download_image(link, f'{SPACE_X_PATH}{num}{JPG_FORMAT}')
    print('Not a single photo was recorded from this flight.')
