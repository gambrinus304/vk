import requests
import json
import csv
import sys 
sys.path.append('..')
from settings import token
from time import sleep


def write_json(data):
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def to_json(post_dict):
    try:
        data = json.load(open('posts_data.json'))
    except:
        data = []

    data.append(post_dict)

    with open ('posts_data.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def write_csv(data):
    with open('posts_data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow([data['id'],
                         data['text'],
                         data['likes'],
                         data['reposts'],
                         data['comments']
        ])



def get_data(post):
    try:
        post_id = post['id']
    except:
        post_id = 0

    try:
        text = post['text']
    except:
        text = 'empty'

    try:
        likes = post['likes']['count']
    except:
        likes = 'empty'
    
    try:
        comments = post['comments']['count']
    except:
        comments = 'empty'

    try:
        reposts = post['reposts']['count']
    except:
        reposts = 'empty'

    data = {
         'id': post_id,
         'text': text,
         'likes': likes,
         'reposts': reposts,
         'comments': comments,
    }
    

    return data


def main():
    
    user_id = '29465900'
    offset = 0
    date_x = 1499641856

    all_posts = []

    while True:
        sleep(1)
        r = requests.get('https://api.vk.com/method/wall.get', params={'owner_id': user_id, 'v': 5.60, 'count': 30, 'offset': offset, 'access_token': token})
        posts = r.json()['response']['items']

        all_posts.extend(posts)
        

        oldest_post_date = posts[-1]['date']
        
        offset += 30
        print(offset)

        if oldest_post_date < date_x:
            break
        
    data_posts = []
    

    for post in all_posts:
        post_data = get_data(post)
        # sorted(post_data.items(), key=lambda data: data[2])
        write_csv(post_data)


if __name__ == '__main__':
    main()


