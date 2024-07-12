from download_and_checks_image import download_image, outputs_image_format
from requests import get
from urllib.parse import urlparse, ParseResult

DEMO_KEY = 'DEMO_KEY'
NASA_APOD_API = 'https://api.nasa.gov/planetary/apod'
NASA_EPIC_API = 'https://api.nasa.gov/EPIC/api/natural/images'
EPIC_ARCHIVE = 'https://api.nasa.gov/EPIC/archive/natural'
JPG_FORMAT = '.jpg'
PNG_FORMAT = '.png'
APOD_PATH = 'images/apod_'
EPIC_PATH = 'images/epic_'


def download_images_apod(count: int, api_key: str = DEMO_KEY) -> None :
    payload = {'api_key': api_key, 'count': count}

    response = get(NASA_APOD_API, params=payload)
    response.raise_for_status()

    for num, link in enumerate(response.json()):
        if outputs_image_format(link['url']) != JPG_FORMAT:
            continue
        download_image(link['url'], f'{APOD_PATH}{num}{JPG_FORMAT}')


def download_images_epic(count: int, api_key: str = DEMO_KEY) -> None:
    payload = {'api_key': api_key}
    epic_images = {}

    response = get(NASA_EPIC_API, params=payload)
    response.raise_for_status()

    for num, date_and_image in enumerate(response.json()):
        epic_images[num] = {
            'date': date_and_image['date'][:10],
            'image': date_and_image['image']
        }

    for num in range(count):
        date_image = epic_images[num]['date']
        image_id = epic_images[num]['image']

        year, month, day = str(date_image).split('-')
        
        image_url = f'{EPIC_ARCHIVE}/{year}/{month}/{day}/png/{image_id}{PNG_FORMAT}'

        download_image(image_url, f'{EPIC_PATH}{num}{PNG_FORMAT}', payload)
