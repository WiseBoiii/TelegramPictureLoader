import requests
import json
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telegram
import random
from time import sleep

load_dotenv()
API_KEY = os.environ.get('API_KEY')
space_pic_dirs = ['images/nasa_epic_images', 'images/nasa_images', 'images/spacex_images']
nasa_epic_data_url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={API_KEY}'
spacex_launch_data_url = 'https://api.spacexdata.com/v3/launches/64'
nasa_apod_data_url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&count=50'


def load_spacex_pictures(spacex_launch_data_url):
    response = requests.get(spacex_launch_data_url)
    response.raise_for_status
    launch_data = response.json()
    flickr_links = launch_data['links']['flickr_images'][:]
    for iteration_index, picture_link in enumerate(flickr_links):
        response = requests.get(picture_link)
        response.raise_for_status()
        spacex_picture_extension = get_picture_extension(picture_link)
        filename = f'images/spacex_images/spacex_image_{iteration_index}{spacex_picture_extension}'
        out = open(filename, "wb")
        out.write(response.content)
        out.close()

def load_nasa_apod_pictures(nasa_apod_data_url):
    response = requests.get(nasa_apod_data_url)
    nasa_apod_data = response.json()
    response.raise_for_status()
    for iteration_index, nasa_apod_data in enumerate(nasa_apod_data):
        nasa_picture_url = nasa_apod_data['url']
        response = requests.get(nasa_picture_url)
        response.raise_for_status()
        picture_extension = get_picture_extension(nasa_picture_url)
        filename = f'images/nasa_images/nasa_apod_image_{iteration_index}{picture_extension}'
        out = open(filename, "wb")
        out.write(response.content)
        out.close()

def load_nasa_epic_pictures(nasa_epic_data_url):
    response = requests.get(nasa_epic_data_url)
    nasa_epic_picture_data = response.json()
    response.raise_for_status()
    for iteration_index, nasa_epic_launch_data in enumerate(nasa_epic_picture_data):
        launch_date = nasa_epic_launch_data['date'].split(' ')[0].replace('-', '/')
        image_name = nasa_epic_launch_data['image']
        nasa_epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{launch_date}/png/{image_name}.png?api_key={API_KEY}'
        response = requests.get(nasa_epic_url)
        response.raise_for_status()
        filename = f'images/nasa_epic_images/nasa_epic_image_{iteration_index}.png'
        out = open(filename, "wb")
        out.write(response.content)
        out.close()


def choose_picture(space_pic_dirs):
    random_dir = random.choice(space_pic_dirs)
    random_pic = random.choice(os.listdir(random_dir))
    return f'{random_dir}/{random_pic}'



def get_picture_extension(picture_link):
    _, extension = os.path.splitext(picture_link)
    return extension



if __name__ == '__main__':
    load_spacex_pictures(spacex_launch_data_url)
    load_nasa_apod_pictures(nasa_apod_data_url)
    load_nasa_epic_pictures(nasa_epic_data_url)
    TOKEN = os.getenv('TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')
    bot = telegram.Bot(token=TOKEN)
    while True:
        bot.send_message(text='Here`s your daily space picture dose!', chat_id='@bruhmomentcertified')
        random_picture_for_posting = choose_picture(space_pic_dirs)
        bot.send_document(chat_id=CHAT_ID, document=open(random_picture_for_posting, 'rb'))
        sleep(3600)