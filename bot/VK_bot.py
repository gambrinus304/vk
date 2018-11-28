
# -*- coding: utf-8 -*-
import requests
import sys 
sys.path.append('..')
from settings import token
import random
#from time import sleep


# sender_id = 29465900
# r_message = 'hello, world'

sender_id = 0
text_message = 'Empty'

recommendation = ['Не кидай ментос в колу!', 'Не рисуй на пьяных девушках!',
 'Не садись по-большому за кустиком на лыжном курорте, не снимая лыж!', 
 'Не выбрасывай мусор, если в другой руке держишь ноут!', 'Не ковыряй в носу пальцем, которым размазывал васаби по сосиске!', 
 'Не выходи на улицу в гололёд при сильном расстройстве желудка!', 'Не пробуй суперклей на вкус!', 
 'Не открывай зелёнку зубами!', 'Не буди пьяного мужа, намазав лицо маской!', 
 'Не помещай в своё ректальное отверстие раскалённый утюг (не, ну а вдруг ¯\_(ツ)_/¯ )', 'Не смотрите на клаву, за которой жрал, в ультрафиолете!', 
 'Не позволяй удовлетворять себя орально людям, почистившим зубы ментоловой пастой!', 'Не ставь на скринсейвер показ слайдов, если неподалёку находится скрытая папка с поревом!', 
 'Не говори таможенникам, что у тебя в анусе пакет с наркотой!', 'Не отвечай "с трудом" на вопрос девушки "как ты находишь мою грудь?"', 
 'Не устанавливай Diablo незадолго до дедлайнов!', 'Не переноси комп на кухню / холодильник+чайник к компу!', 
 'Не встречайся с судмедэкспертами!', 'Не брей яйца кремом для эпиляции!', 'Не смейся над Чаком!', 'Не еби мозга!', 'В случае проблемы - накрась губы! (Как быть идеальной?)']

smile = ['&#128543;', '&#128556;', '&#128566;', '&#128554;', '&#128555;', '&#9786;', '&#128512;', '&#128549;', '&#128539;', '&#128534;', 
'&#128548;', '&#128547;', '&#128551;', '&#128529;', '&#128517;', '&#128558;', '&#128542;', '&#128537;', '&#128531;', '&#128513;', 
'&#128561;', '&#128520;', '&#128127;', '&#128169;', '&#128148;', '&#128568;', '&#128569;', '&#128572;', '&#128573;', '&#128574;', 
'&#128575;', '&#128571;', '&#128576;', '&#128570;', '&#127773;', '&#128543;', '&#128556;', '&#128566;', '&#128554;', '&#128555;', 
'&#9786;', '&#128512;', '&#128549;', '&#128539;', '&#128534;', '&#128548;', '&#128547;', '&#128551;', '&#128529;', '&#128517;', 
'&#128558;', '&#128542;', '&#128537;', '&#128531;', '&#128513;', '&#128561;', '&#128520;', '&#128127;', '&#128169;', '&#128148;', 
'&#128568;', '&#128569;', '&#128572;', '&#128573;', '&#128574;', '&#128575;', '&#128571;', '&#128576;', '&#128570;', '&#127773;', 
]

history = ['vk.com/@gambrinus-pohod', 'vk.com/@gambrinus-zhidkii-azot', 'vk.com/@gambrinus-semper-fi', 'vk.com/@gambrinus-lekarstvo-ot-lunatizma', 'vk.com/@gambrinus-zolotaya-rybka', 'vk.com/@gambrinus-zakrytaya-informaciya', 'vk.com/@gambrinus-kot', 'vk.com/@gambrinus-istinnaya-lubov', 'vk.com/@gambrinus-malchik-yasha', 'vk.com/@gambrinus-blagodarnost']




#print (sys.version)

def get_update():
    connect_lpserver = requests.get('https://api.vk.com/method/messages.getLongPollServer', params={'access_token': token, 'v': 5.60}).json()['response']
    #print(connect_lpserver)
    updates = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=2' .format (server = connect_lpserver['server'], key = connect_lpserver['key'], ts = connect_lpserver['ts'])).json()
    return updates


def get_message(updates):
    for update in updates:
        action_code = update[0]
        if action_code == 4:
            message = update
            print('get message test')
            return message
        # except:
        #     sleep(1)
        #     continue
            


def send_message(sender_id, r_message):
    params = {'access_token': token, 'v': 5.60, 'user_ids': sender_id, 'message': r_message}
    r = requests.get('https://api.vk.com/method/messages.send', params=params)


def send_photo(sender_id, attach):
    params = {'access_token': token, 'v': 5.60, 'user_ids': sender_id, 'attachment': attach}
    r = requests.get('https://api.vk.com/method/messages.send', params=params)


# while True:
#     


# photo29465900_456240348

# резерв, рабочий
def get_message(updates):
    for update in updates:
        action_code = update[0]
        if action_code == 4:
            sender_id = update[3]
            sender_name = requests.get('https://api.vk.com/method/users.get', params={'access_token': token, 'v': 5.60, 'user_ids': sender_id}).json()['response'][0]
            f_name = sender_name['first_name']
            l_name = sender_name['last_name']
            text_message = update[5]
            print(f_name, l_name, 'прислал сообщение:', text_message)
            message = json.dump(sender_id, sender_name, text_message)
            return message






while True:
    result = get_update()
    updates = result['updates']
    ts = result['ts']
    sh_ts = len(updates)
    print(ts)
    # print(sh_ts, 'show ts')
    print(sh_ts + ts, 'next')
    for update in updates:
        try:
            action_code = update[0]
            if action_code == 4:
                sender_id = update[3]
                sender_name = requests.get('https://api.vk.com/method/users.get', params={'access_token': token, 'v': 5.60, 'user_ids': sender_id}).json()['response'][0]
                f_name = sender_name['first_name']
                l_name = sender_name['last_name']
                text_message = update[5]
                print('Новое сообщение в чате с', f_name, l_name, ':', text_message)
                
                if text_message == 'Вася дай совет':
                    send_message(sender_id, random.choice(recommendation))
                elif text_message == '🤔':
                    send_message(sender_id, random.choice(smile))
                elif text_message == 'Как быть идеальной?':
                    message = 'vk.com/@gambrinus-z'
                    send_message(sender_id, message)
                elif text_message == 'Вася расскажи историю':
                    send_message(sender_id, random.choice(history))
                elif text_message == 'Любви тебе до гроба':
                    message = 'Хуевь тебе пачку!'
                    send_message(sender_id, message)
                else:
                    pass
                    # print ('пропуск совета')
                    
        except TypeError:
            print('TupeError message:', message)
        

        # elif action_code == 80:
        #     new_mess_mark = update[1]
        #     if new_mess_mark == 0:
        #         print('Новых сообщений нет')
        #     else:
        #         pass
        else:
            pass
    






# дешифратор
# while True:

#     updates = get_update()
#     print(updates)

    

#     for update in updates:
#         action_code = update[0]
#         if action_code == 4:
#             sender_id = update[3]
#             sender_name = requests.get('https://api.vk.com/method/users.get', params={'access_token': token, 'v': 5.60, 'user_ids': sender_id}).json()['response'][0]
#             f_name = sender_name['first_name']
#             l_name = sender_name['last_name']
#             text_message = update[5]
#             print('Новое сообщение в чате с', f_name, l_name, ':', text_message)
#         elif action_code == 8:
#             friend_id = update[1] * -1
#             friend_name = requests.get('https://api.vk.com/method/users.get', params={'access_token': token, 'v': 5.60, 'user_ids': friend_id}).json()['response'][0]
#             #print(friend_name)
#             f_name = friend_name['first_name']
#             l_name = friend_name['last_name']
#             # print(f_name, l_name, 'снова online')
            
#         elif action_code == 9:
#             friend_id = update[1] * -1
#             friend_name = requests.get('https://api.vk.com/method/users.get', params={'access_token': token, 'v': 5.60, 'user_ids': friend_id}).json()['response'][0]
#             #print(friend_name)
#             f_name = friend_name['first_name']
#             l_name = friend_name['last_name']
#             # print(f_name, l_name, 'вышел в offline')
#         elif action_code == 80:
#             new_mess_mark = update[1]
#             if new_mess_mark == 0:
#                 print('Новых сообщений нет')
#             else:
#                 pass
#         else:
#             pass
    
#     if action_code == 4:
#         print('test', sender_id, text_message)

    

# print(sender_id, text_message)

# vk_api.messages.getLongPollHistory()
#test = vk_api.account.getProfileInfo(user_id=29465900)
#print(test)

#vk_api.messages.send(user_id=29465900, message='Hi, this is test message from my new VK bot')





