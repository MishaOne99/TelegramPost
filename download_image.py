'''Создаёт директорию в файловой системе и скачивает в неё фотографии (SpaceX, NASA_APOD, NASA_EPIC)'''


import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from space_x_img_service import fetch_spacex_last_launch
from nasa_img_service import download_images_apod, download_images_epic

DIRECTORY_NAME = 'images'
ANSWER = 'y'


def runs_images_download(id: str, img_count: int, download_img_spacex: str, download_img_apod: str, download_img_epic:str) -> None:
    '''
    Создаёт директорию в файловой системе, уточняет какие фотографии должны быть загруженные 
    в неё и скачивает эти фотографии .
    '''
    Path(DIRECTORY_NAME).mkdir(parents=True, exist_ok=True)
    load_dotenv()
    token = os.environ['API_NASA_KEY']

    if download_img_spacex.lower() == ANSWER:
        fetch_spacex_last_launch(id)
    if download_img_apod.lower() == ANSWER:
        download_images_apod(count=img_count, api_key=token)
    if download_img_epic.lower() == ANSWER:
        download_images_epic(count=img_count, api_key=token)


def main():
    '''
    Позволяет работать из командной строки
    '''
    parser = argparse.ArgumentParser(description='Downloads images of space')
    parser.add_argument('Download_img_SpaceX', type=str, nargs='?', default='n', help='Do you want to download images from SpaceX? (y/n)')
    parser.add_argument('Download_img_APOD', type=str, nargs='?', default='n', help='Do you want to download images from APOD? (y/n)')
    parser.add_argument('Download_img_EPIC', type=str, nargs='?', default='n', help='Do you want to download images from EPIC? (y/n)')
    parser.add_argument('IMG_Count', type=int, nargs='?', default=1, help='Enter the number of photos to upload')
    parser.add_argument('ID', type=str, nargs='?', default='latest', help='Enter the post publication ID')
    args = parser.parse_args()
    runs_images_download(args.ID, args.IMG_Count, args.Download_img_SpaceX, args.Download_img_APOD, args.Download_img_EPIC)

if __name__ == '__main__':
    main()
