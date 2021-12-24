# Скачивание картинок в Telegram канал с помощью бота

**TelegramPictureLoader** это скрипт, благодаря которому можно сделать бота для скачивания картинок из космоса с Nasa, а также SpaceX и постить их в Вашем Telegram канале с выбранной Вами периодичностью.

### Как установить

С установкой все просто. Вам достаточно склонировать себе репозиторий с кодом и можно начинать работу, однако перед этим стоит убедиться, что:

+ Python 3.9 должен быть уже установлен. 	
+ Нужен chat_id вашего Telegram канала, для получения которого важно чтобы ваш канал был публичным. 
+ Вы создали файл ```.env``` в папке репозитория, который выглядит **ПРИМЕРНО** так:
```
NASA_API_KEY=WbLQBfUN01G85Adhr4GLCWruKdU3nznGuHtcXzfB
TELEGRAM_BOT_TOKEN=2049864829:AAEgK-iQ0zLtWhHwq5h9x7Llwd95wp_UgxY
TELEGRAM_CHAT_ID=@bruhmomentcertified
```
+ Ваш API_KEY можно получить [***здесь***](https://api.nasa.gov/) в разделе Generate API Key.
+ Про получение токена можно узнать [***здесь***](https://way23.ru/регистрация-бота-в-telegram.html)
+ О том, как получить chat id можно узнать [***здесь***](https://it-stories.ru/blog/web-dev/kak-uznat-chat-id-dlja-kanala-gruppy-telegram/)

### Нужные вам команды

1) Вы перейдете в папку с репозиторием
```
cd C:\Path to repository
``` 
2) С помощью этого вы установите нужные вам библиотеки
```
pip install -r requirements.txt
``` 
3) Это запустит код и покажет вам возможные аргументы для запуска
```
python main.py
```


В течение минуты после запуска вы увидите в своем Telegram канале сообщение с картинкой

![alt text](https://github.com/WiseBoiii/TelegramPictureLoader/blob/main/Script%20work%20example.png)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

+ ![alt text](https://github.com/WiseBoiii/TelegramPictureLoader/blob/main/nice.gif)

