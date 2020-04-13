import requests


def main():
    # Using Mathias' Ego's bot token
    res = requests.get('https://discordapp.com/api/v6/channels/361939927644241922/messages', params={'limit': 100}, headers={'Authorization': 'Bot Njk5MjY0MDk4Mjk4NDk1MDY3.XpR3jA.2tZwK9Fz8tFaSK846_Xp0yiVwK8'})
    if (res.status_code != 200): 
        print(res.json())
        return 

    with open('corpus/arno.txt', 'w') as file:
        for message in res.json():
            if message["author"]['id'] == '153947383804329984':
                file.write(message['content'] + '\n')
    print('done')


if __name__ == '__main__':
    main()
