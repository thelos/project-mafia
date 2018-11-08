import vk_api


def getfullandsecondname(token):
    vk_session = vk_api.VkApi(token=token)
    temporary = vk_session.method(method='users.get', values={
        'fields': ['nickname']
    })[0]
    return temporary['first_name'] + ' ' + temporary['last_name']


if __name__ == '__main__':
    print(getfullandsecondname(input()))
