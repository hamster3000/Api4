import telegram
import time
import os
import random
from dotenv import load_dotenv

def auto_post(bot,chat_id):
    while True:
        folder = 'images'
        files = os.listdir(folder)
        random.shuffle(files)
        for file in files:
            path = os.path.join(folder, file)
            with open(path, 'rb') as f:
                bot.send_photo(chat_id=chat_id, photo=f)
            time.sleep(14400)


def main():
    load_dotenv()
    chat_id = os.environ['TG_CHATID']
    token = os.environ['TGBOT_TOKEN']
    bot = telegram.Bot(token=token)
    auto_post(bot,chat_id)


if __name__ == '__main__':
    main()
