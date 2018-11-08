import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import http.client
from my_functions import SendATokenToSave
import random
slay = dict()
riffle = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']


def main():
    login, password = 'telnov.fe@yandex.ru', 'seroneverwinter'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    f = open('UserId_Key.txt', 'r')
    for line in f:
        line_t = line.strip()
        s = line_t.split(' - ')
        slay[s[0]] = s[1]
    f.close()
    print(slay)
    temp_list = []
    for i in slay.items():
        temp_list.append(i[1])
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and event.to_me and event.text=='!register':
            if event.user_id in slay:
                continue
            while True:
                seq = random.sample(riffle, 16)
                random.shuffle(seq)
                seq = ''.join(seq)
                if seq not in temp_list:
                    slay[event.user_id] = seq
                    break
            temp_list.append(seq)
            SendATokenToSave(event.user_id, seq)
            slay[event.user_id] = seq
            vk.messages.send(user_id=event.user_id, message='Твой код: ' + seq + '  -- Удачной игры!')
            print('id{}: "{}"'.format(event.user_id, seq), end=' ')
            f = open('UserId_Key.txt', 'a')
            f.write(str(event.user_id) + ' - ' + seq + '\n')
            f.close()


if __name__ == '__main__':
    main()