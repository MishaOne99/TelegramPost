'''Создаёт директорию в файловой системе и скачивает в неё фотографии (SpaceX, NASA_APOD, NASA_EPIC)'''


import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from space_x_img_service import fetch_spacex_last_launch
from nasa_img_service import download_img_apod, download_img_epic

DIRECTORY_NAME = 'images'
TOKEN = 'API_NASA_KEY'
NEED_TO_FETCH_SPACE_X = 'Do you want to download images from SpaceX? (y/n): '
NEED_TO_FETCH_NASA = 'Do you want to download images from NASA? (y/n): '
NEED_TO_FETCH_EPIC = 'Do you want to download images from EPIC? (y/n): '
ANSWER = 'y'

ID = {'ID_NAME': 'ID', 'ID_TYPE': str, 'ID_DEFAULT': 'latest', 'ID_HELP_MSG': 'Enter the post publication ID'}
COUNT = {'COUNT_NAME': 'Count_img', 'COUNT_TYPE': int, 'COUNT_DEFAULT': 1, 'COUNT_HELP_MSG': 'Enter the number of photos to upload'}


def main_loop(id: str, count_img: int) -> None:
    '''
    Создаёт директорию в файловой системе, уточняет какие фотографии должны быть загруженные 
    в неё и скачивает эти фотографии .
    '''
    Path(DIRECTORY_NAME).mkdir(parents=True, exist_ok=True)
    load_dotenv()
    token = os.environ[TOKEN]

    answer_img_spacex = input(NEED_TO_FETCH_SPACE_X).lower()
    answer_img_apod = input(NEED_TO_FETCH_NASA).lower()
    answer_img_epic = input(NEED_TO_FETCH_EPIC).lower()

    if answer_img_spacex == ANSWER:
        fetch_spacex_last_launch(id)
    if answer_img_apod == ANSWER:
        download_img_apod(count=count_img, api_key=token)
    if answer_img_epic == ANSWER:
        download_img_epic(count=count_img, api_key=token)


def main():
    '''
    Позволяет работать из командной строки
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(COUNT['COUNT_NAME'], type=COUNT['COUNT_TYPE'], nargs='?', default=COUNT['COUNT_DEFAULT'], help=COUNT['COUNT_HELP_MSG'])
    parser.add_argument(ID['ID_NAME'], type=ID['ID_TYPE'], nargs='?', default=ID['ID_DEFAULT'], help=ID['ID_HELP_MSG'])
    args = parser.parse_args()
    main_loop(args.ID, args.Count_img)

if __name__ == '__main__':
    main()
