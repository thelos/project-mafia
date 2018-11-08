import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType


def function(stre):
    sda = list()
    for i in range(len(stre)):
        sda.append(stre[i])
    random.shuffle(sda)
    return sda


def main():
    login, password = 'telnov.fe@yandex.ru', 'seroneverwinter'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    ms = '))' * 1000
    vk.messages.send(user_id=180776381, message=ms)


if __name__ == '__main__':
    main()