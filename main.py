import random
from time import sleep
from urllib.parse import urlparse
import os

import requests
from dotenv import load_dotenv
import telegram




def load_spacex_pictures():
    spacex_launch_url = 'https://api.spacexdata.com/v3/launches/64'
    response = requests.get(spacex_launch_url)
    response.raise_for_status()
    spacex_launch = response.json()
    flickr_links = spacex_launch['links']['flickr_images'][:]
    for iteration_index, picture_link in enumerate(flickr_links):
        picture_name = f'spacex_image_{iteration_index}'
        picture_directory = 'images/spacex_images'
        download_picture(picture_link, picture_name, picture_directory)


def load_nasa_apod_pictures(nasa_api_key):
    payload = {'api_key': nasa_api_key, 'count': 50}
    nasa_apod_url = f'https://api.nasa.gov/planetary/apod'
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    nasa_apod = response.json()
    print(nasa_apod)
    for iteration_index, nasa_apod in enumerate(nasa_apod):
        nasa_apod_url = nasa_apod['url']
        print(nasa_apod_url)
        picture_url_test(nasa_apod_url, iteration_index)


def picture_url_test(failed_picture_urls, nasa_apod_url, iteration_index=''):
    url_error_test = urlparse(nasa_apod_url)
    if 'youtube' in url_error_test.netloc:
        failed_picture_urls.append(nasa_apod_url)
    else:
        picture_name = f'nasa_apod_image_{iteration_index}'
        picture_directory = 'images/nasa_apod_images'
        download_picture(nasa_apod_url, picture_name, picture_directory)
    return failed_picture_urls


def load_nasa_epic_pictures(nasa_api_key):
    payload = {'api_key': nasa_api_key}
    nasa_epic_url = f'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    nasa_epic_picture = response.json()
    for iteration_index, nasa_epic_launch in enumerate(nasa_epic_picture):
        launch_date = nasa_epic_launch['date'].split(' ')[0].replace('-', '/')
        image_name = nasa_epic_launch['image']
        nasa_epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{launch_date}/png/{image_name}.png'
        picture_name = f'nasa_epic_image_{iteration_index}'
        picture_directory = 'images/nasa_epic_images'
        download_picture(nasa_epic_url, picture_name, picture_directory, payload)


def download_picture(picture_link, picture_name, picture_directory, payload=''):
    response = requests.get(picture_link, params=payload)
    response.raise_for_status()
    picture_extension = get_picture_extension(picture_link)
    filename = f'{picture_directory}/{picture_name}{picture_extension}'
    with open(filename, 'wb') as filename:
        filename.write(response.content)


def choose_random_picture_or_url(space_pic_dirs, video_urls):
    random_video_url = random.choice(video_urls)
    random_picture_dir = random.choice(space_pic_dirs)
    random_pic = random.choice(os.listdir(random_picture_dir))
    chosen_random_picture = f'{random_picture_dir}/{random_pic}'
    random_post = random.choice(chosen_random_picture, random_video_url)
    return random_post


def get_picture_extension(picture_link):
    urlparsed_picture_link = urlparse(picture_link)
    _, extension = os.path.splitext(urlparsed_picture_link.path)
    return extension


def upload_post_to_chat(telegram_chat_id, space_pic_dirs):
    get_random_post = choose_random_picture_or_url(space_pic_dirs, video_urls)
    if type(get_random_post) == str:
        bot.send_message(text="Today we have a video about space for you to see!", chat_id=telegram_chat_id)
        bot.send_message(text=get_random_post, chat_id=telegram_chat_id)
    else:
        with open(get_random_post) as document:
            bot.send_message(text="Today we have a space picture for you to see!", chat_id=telegram_chat_id)
            bot.send_document('rb', chat_id=telegram_chat_id, document=document)


if __name__ == '__main__':
    failed_picture_urls = []
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    space_pic_dirs = ['images/nasa_epic_images', 'images/nasa_apod_images', 'images/spacex_images']
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)
    while True:
        load_spacex_pictures()
        video_urls = load_nasa_apod_pictures(nasa_api_key)
        load_nasa_epic_pictures(nasa_api_key)
        upload_post_to_chat(telegram_chat_id, space_pic_dirs)
        sleep(86400)
