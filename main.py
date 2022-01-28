import random
from time import sleep
from urllib.parse import urlparse
import os

import requests
from dotenv import load_dotenv
import telegram




def load_spacex_pictures(main_image_directory, spacex_pic_name, launch_number):
    spacex_launch_url = f'https://api.spacexdata.com/v3/launches/{launch_number}'
    response = requests.get(spacex_launch_url)
    response.raise_for_status()
    spacex_launch = response.json()
    flickr_links = spacex_launch['links']['flickr_images']
    for iteration_index, picture_link in enumerate(flickr_links):
        picture_name = f'spacex_image_{iteration_index}'
        picture_directory = f'{main_image_directory}/{spacex_pic_name}'
        download_picture(picture_link, picture_name, picture_directory)


def load_nasa_apod_picture_urls(nasa_api_key, picture_amount):
    payload = {'api_key': nasa_api_key, 'count': picture_amount}
    nasa_apod_url = f'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    nasa_apod = response.json()
    urls = []
    for iteration_index, nasa_apod in enumerate(nasa_apod):
        try:
            urls.append(nasa_apod['url'])
        except KeyError:
            pass
    return urls


def load_nasa_epic_pictures(nasa_api_key, main_image_directory, nasa_epic_pic_name):
    payload = {'api_key': nasa_api_key}
    nasa_epic_url = f'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    nasa_epic_pictures = response.json()
    for iteration_index, nasa_epic_launch in enumerate(nasa_epic_pictures):
        launch_date = nasa_epic_launch['date'].split(' ')[0].replace('-', '/')
        image_name = nasa_epic_launch['image']
        nasa_epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{launch_date}/png/{image_name}.png'
        picture_name = f'nasa_epic_image_{iteration_index}'
        picture_directory = f'{main_image_directory}/{nasa_epic_pic_name}'
        download_picture(nasa_epic_url, picture_name, picture_directory, payload)


def download_picture(picture_link, picture_name, picture_directory, payload=''):
    response = requests.get(picture_link, params=payload)
    response.raise_for_status()
    picture_extension = get_picture_extension(picture_link)
    filename = f'{picture_directory}/{picture_name}{picture_extension}'
    with open(filename, 'wb') as filename:
        filename.write(response.content)


def load_apod_urls(urls, main_image_directory, nasa_apod_dir_name):
    for iteration_index, nasa_apod_url in enumerate(urls):
        url_error_test = urlparse(nasa_apod_url)
        if 'youtube' not in url_error_test.netloc:
            if 'vimeo' not in url_error_test.netloc:
                apod_picture_name = f'nasa_apod_image_{iteration_index}'
                picture_directory = f'{main_image_directory}/{nasa_apod_dir_name}'
                download_picture(nasa_apod_url, apod_picture_name, picture_directory)


def choose_random_picture(main_image_directory, space_pic_dirs):
    random_picture_dir = random.choice(space_pic_dirs)
    random_pic = random.choice(os.listdir(f'{main_image_directory}/{random_picture_dir}'))
    chosen_random_picture = f'{main_image_directory}/{random_picture_dir}/{random_pic}'
    return chosen_random_picture


def get_picture_extension(picture_link):
    urlparsed_picture_link = urlparse(picture_link)
    _, extension = os.path.splitext(urlparsed_picture_link.path)
    return extension


def upload_post_to_chat(main_image_directory, telegram_chat_id, space_pic_dirs, bot):
    random_post = choose_random_picture(main_image_directory, space_pic_dirs)
    with open(random_post) as document:
        bot.send_message(text="Today we have a space picture for you to see!", chat_id=telegram_chat_id)
        bot.send_document('rb', chat_id=telegram_chat_id, document=document)


if __name__ == '__main__':
    load_dotenv()
    main_image_directory = 'images'
    spacex_dir_name = 'spacex_images'
    nasa_apod_dir_name = 'nasa_apod_images'
    nasa_epic_dir_name = 'nasa_epic_images'
    nasa_api_key = os.getenv('NASA_API_KEY')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)
    space_pic_dirs = [nasa_epic_dir_name, nasa_apod_dir_name, spacex_dir_name]
    while True:
        load_spacex_pictures(main_image_directory, spacex_dir_name, 64)
        apod_urls = load_nasa_apod_picture_urls(nasa_api_key, 50)
        load_nasa_epic_pictures(nasa_api_key, main_image_directory, nasa_epic_dir_name)
        load_apod_urls(apod_urls, main_image_directory, nasa_apod_dir_name)
        upload_post_to_chat(main_image_directory, telegram_chat_id, space_pic_dirs, bot)
        sleep(20)
