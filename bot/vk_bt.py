# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import requests
import random
from settings import token
from wit import Wit
#from time import sleep





def get_update():
    params = requests.get('https://api.vk.com/method/messages.getLongPollServer', params={'access_token': token, 'v': 5.60}).json()['response']
    # ts = params['ts']
    # print('ts in get_update function: ', ts)
    # get params (key, server, ts) for use in requests
    # есть подозрение, что сервак пролюбливает часть TS. надо будет попробовать передавать значения через TS+1, но проблема в ключе. Сукааааа
    updates = requests.get('https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode=2&version=2' .format (server = params['server'], key = params['key'], ts = params['ts'])).json()
    # print(updates, 'get update')
    return updates


def get_history(updates):
    ts = updates['ts']
    r = requests.get('https://api.vk.com/method/messages.getLongPollHistory', params={'access_token': token, 'ts': ts, 'v': 5.60}).json()
    print(r, 'get_hist')





    # ts = updates['ts']
    # user_id = updates['updates'][0][3]
    # r= requests.get('https://api.vk.com/method/messages.getHistory', params={'access_token': token, 'offset': 0, 'count': 5, 'user_id': user_id, 'peer_id': user_id, 'start_message_id': -1, 'v': 5.85})




updates = get_update()
print(updates)
ts = updates['ts']
old_ts = ts
print('fiasko')


while True:
    updates = get_update()


    print('__________')
    print(updates, 'test updates')
    # for update in updates:



    ts = updates['ts']
    print('new ts: ', ts)
    # print(updates, 'test')



    if ts == old_ts:
        print('ravno',old_ts, ts)
        print(updates)


    elif ts == old_ts + 1:
        print('oneplus', old_ts, ts)
        print(updates)

        action_code = updates['updates'][0][0]
        print(action_code, 'action_code')

        if action_code == 4:
            message_upd = get_messages(updates)
            message = updates[5]
            print(message)
        else:
            print('other updates')


    else:
        print('ebash!', old_ts, ts)
        print(updates)

        update = updates['updates']





    
    old_ts = ts
    print('old ts: ', old_ts)






# while True:
    
#     print(updates)
#     message = updates[updates']

#     try:
#         action_code = mesage[0]
#         print(action_code)

#         for update in updates:
#             if action_code == 4:
#                 print('code 4')
#             else:
#                 print(message, '!')



#     except:
#         print('other')

