# Скачивание картинок в Telegram канал с помощью бота

**TelegramPictureLoader** это скрипт, благодаря которому можно сделать бота для скачивания картинок из космоса с Nasa, а также SpaceX и постить их в Вашем Telegram канале с выбранной Вами периодичностью.

### Как установить

С установкой все просто. Вам достаточно склонировать себе репозиторий с кодом и можно начинать работу, однако перед этим стоит убедиться, что:

+ Python 3.9 должен быть уже установлен. 	
+ Нужен chat_id вашего Telegram канала, для получения которого важно чтобы ваш канал был публичным. 
+ Вы создали файл ```.env``` в папке репозитория, который выглядит **ПРИМЕРНО** так:
```
API_KEY=pjRZouSxbe48eWrCIsQNqnpjLbYHIggOOMhIwUuH
TOKEN=2049864829:AAEgK-iQ0zLtWhHwq5h9x7Llwd95wp_UgxY
CHAT_ID=@bruhmomentcertified
```
+ Ваш API_KEY можно получить [***здесь***](https://api.nasa.gov/) в разделе Generate API Key.
+ Про получение токена можно узнать [***здесь***](https://way23.ru/регистрация-бота-в-telegram.html)
+ О том, как получить chat id можно узнать [***здесь***](https://it-stories.ru/blog/web-dev/kak-uznat-chat-id-dlja-kanala-gruppy-telegram/)

### Нужные вам команды

```cd C:\Path to repository``` - Вы перейдете в папку с репозиторием
```pip install virtualenv``` - Вы скачаете библиотеку для установки виртуального окружения
```python -m venv name of venv``` - С помощью этого вы создадите свое виртуальное окружение
```pip install -r requirements.txt``` - С помощью этого вы установите нужные вам библиотеки
```python main.py``` - Это запустит код и покажет вам возможные аргументы для запуска


В течение минуты после запуска вы увидите в своем Telegram канале сообщение с картинкой

![alt text](https://github.com/WiseBoiii/TelegramPictureLoader/blob/main/Script%20work%20example.png)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

+ ![alt text](https://github.com/WiseBoiii/TelegramPictureLoader/blob/main/nice.gif)

