import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def main():
    login, password = 'telnov.fe@yandex.ru', 'seroneverwinter'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.from_user and event.to_me:
            f = open('logs.txt', 'a')
            name = vk.users.get(user_ids=[event.user_id], fields=['nickname'])
            print(name[0]['first_name'], name[0]['last_name'], '-', event.text, file=f)
            f.close()
            print(event.attachments)
            if event.attachments != []:
                vk.messages.send(user_id=444025494, attachments=event.attachments)


if __name__ == '__main__':
    main()