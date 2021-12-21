# Написати програму, яка буде робити наступне:
# 1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
# 2. Запропонувати обрати користувача (ввести ID)
# 3. Розробити наступну менюшку (із вкладеними пунктами):
#    1. Повна інформація про користувача
#    2. Пости:
#       - перелік постів користувача (ID та заголовок)
#       - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
#    3. ТУДУшка:
#       - список невиконаних задач
#       - список виконаних задач
#    4. Вивести URL рандомної картинки
import requests
import json
import random

print("1 - full information, 2 - posts, 3 - TO DO, 4 - random url, 5 - exit")


def menu():
    id_us = int(input("Write id which you want to choose in users' tables: "))
    while True:
        command = int(input('Write your command: '))
        if command == 1:
            info(id_us)
        elif command == 2:
            posts(id_us)
        elif command == 3:
            to_do(id_us)
        elif command == 4:
            random_url()
        else:
            break


def info(id_user):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    with open('users.json', 'w') as user:
        user.write(response.text)
    with open('users.json', 'rb') as read:
        data = json.load(read)
        for i in data:
            if i['id'] == id_user:
                print(f"""ID :{id_user}\nName: {i['name']}\nUsername: {i['username']}\nEmail: {i['email']}\nAddress: {i['address']}\nPhone: {i['phone']}\nWebsite: {i['website']}\nCompany: {i['company']}""")
            break


def posts(id_post):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    with open('post_comment.json', 'w') as user:
        user.write(response.text)
    with open('post_comment.json', 'rb') as read:
        data = json.load(read)
        for i in data:
            if i['id'] == id_post:
                title = i['title']
                body = i['body']
                print(f"ID: {id_post} \nTitle: {title} \nBody: {body}")
                break
    response2 = requests.get('https://jsonplaceholder.typicode.com/comments')
    with open('post.json', 'w') as user:
        user.write(response2.text)
    with open('post.json', 'rb') as read:
        data = json.load(read)
        id = 0
        for i in data:
            if i['postId'] == id_post:
                id += 1
                name = i['name']
                id_comments = i['id']
                print(f"Name: {name} \nID comments: {id_comments}")
        print(f"Sum of id: {id}")


def to_do(id_user):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    with open('to_do.json', 'w') as f:
        f.write(response.text)
    with open('to_do.json', 'rb') as f:
        data = json.load(f)
        for i in data:
            if i['userId'] == id_user:
                title = i['title']
                if i['completed'] == False:
                    print("Doesn't complete tasks:")
                    print(f"Title:{title}")
                elif i['completed'] == True:
                    print("Complete tasks:")
                    print(f"Title: {title}")


def random_url():
    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    with open('random_url', 'w') as f:
        f.write(response.text)
    with open('random_url', 'rb') as f:
        data = json.load(f)
        rand = random.randint(1, 5000)
        for i in data:
            if i['id'] == rand:
                url = i['url']
                print(f"Random URL: {url}")
                break


menu()
