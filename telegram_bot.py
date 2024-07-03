'''Подключается к боту и публикует фотографии из выбранной директории, в Телеграм канал, с заданной частотой'''

import os
import argparse
from telegram import Bot, InputMediaPhoto
from random import shuffle
from time import sleep


TOKEN = 'API_TELEGRAM_TOKEN'
CHAT_ID = 'CHAT_ID_TELEGRAM'
IMG_PATH = 'images/'

ARGS_INFO = 'Publishes posts in telegram chat'
TIME = {'TIME_NAME': 'time', 'TIME_TYPE': int, 'TIME_DEFAULT': 14400, 'TIME_HELP_MSG': 'Введите время публикации поста'}
DIRECTORY = {'DIRECTORY_NAME': 'directory', 'DIRECTORY_TYPE': str, 'DIRECTORY_DEFAULT': 'images', 'DIRECTORY_HELP_MSG': 'Введите имя директории, где хранятся фотографии'}


def publish_post(bot: dict, chat_id: str, images: list, cycles_count: int, time: int) -> None:
    '''
    Публикует фотографии в телеграм
        Параметры:
            bot (dict): Информация о боте
            chat_id (str): ID чата
            images (list): Фотографии для публикаций
            cycles_count (int): Количество пройденных циклов
            time (int): Частота публикации постов
    '''
    link_photo = f'{IMG_PATH}{str(images[cycles_count])}'

    media_img = InputMediaPhoto(media = open(link_photo, 'rb'))

    bot.send_media_group(media=[media_img], chat_id=chat_id)

    sleep(time)


def prepares_images(time: int, directory: str, token: str, chat_id: str) -> None:
    '''
    Предоставляет доступ к боту и подготавливает фотографии для публикации
        Параметры:
            time (int): Частота публикации постов
            directory (str): Путь к файлу, где хранятся фото для публикации
    '''
    chat_id = chat_id
    bot = Bot(token)

    images = os.listdir(directory)
    shuffle(images)

    count_img = len(images)
    cycles_count = 0

    while True:
        if cycles_count == count_img:
            shuffle(images)
            cycles_count = 0

        publish_post(bot=bot, chat_id=chat_id, images=images, cycles_count=cycles_count, time=time)
        cycles_count += 1


def main():
    '''
    Позволяет работать из командной строки
    '''

    token = os.environ[TOKEN]
    chat_id = os.environ[CHAT_ID]

    parser = argparse.ArgumentParser(description=ARGS_INFO)
    parser.add_argument(TIME['TIME_NAME'], type=TIME['TIME_TYPE'], nargs='?', default=TIME['TIME_DEFAULT'], help=TIME['TIME_HELP_MSG'])
    parser.add_argument(DIRECTORY['DIRECTORY_NAME'], type=DIRECTORY['DIRECTORY_TYPE'], nargs='?', 
                        default=DIRECTORY['DIRECTORY_DEFAULT'], help=DIRECTORY['DIRECTORY_HELP_MSG'])
    args = parser.parse_args()
    prepares_images(args.time, args.directory, token=token, chat_id=chat_id)


if __name__ == '__main__':
    main()
