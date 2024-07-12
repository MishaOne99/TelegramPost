'''Создаёт директорию в файловой системе и скачивает в неё фотографии (SpaceX, NASA_APOD, NASA_EPIC)'''


import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from space_x_img_service import fetch_spacex_last_launch
from nasa_img_service import download_images_apod, download_images_epic

DIRECTORY_NAME = 'images'


def runs_images_download(id: str, img_count: int, download_img_spacex: bool, download_img_apod: bool, download_img_epic: bool, token: str) -> None:
    '''
    Создаёт директорию в файловой системе, уточняет какие фотографии должны быть загруженные 
    в неё и скачивает эти фотографии .
    '''
    Path(DIRECTORY_NAME).mkdir(parents=True, exist_ok=True)

    if download_img_spacex:
        fetch_spacex_last_launch(id)
    if download_img_apod:
        download_images_apod(count=img_count, api_key=token)
    if download_img_epic:
        download_images_epic(count=img_count, api_key=token)


def main():
    '''
    Позволяет работать из командной строки
    '''
    load_dotenv()
    token = os.environ['API_NASA_KEY']

    parser = argparse.ArgumentParser(description='Downloads images of space')
    parser.add_argument('--SpaceX', action='store_true', help='Do you want to download images from SpaceX?')
    parser.add_argument('--APOD', action='store_true', help='Do you want to download images from APOD?')
    parser.add_argument('--EPIC', action='store_true', help='Do you want to download images from EPIC?')
    parser.add_argument('IMG_Count', type=int, nargs='?', default=1, help='Enter the number of photos to upload')
    parser.add_argument('ID', type=str, nargs='?', default='latest', help='Enter the post publication ID')
    args = parser.parse_args()
    
    runs_images_download(args.ID, args.IMG_Count, args.SpaceX, args.APOD, args.EPIC, token=token)

if __name__ == '__main__':
    main()
