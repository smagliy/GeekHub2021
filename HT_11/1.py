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

print("1 - full information, 2 - posts, 3 - comments post  4 - TO DO, 5 - random url, 6 - exit")


def menu():
    id_us = int(input("Write id which you want to choose: "))
    while True:
        command = int(input('Write your command: '))
        if command == 1:
            info(id_us)
        elif command == 2:
            print('1 - some information, 2 - full information')
            stat = int(input('Write your number choose:'))
            posts(id_us, stat)
        elif command == 3:
            comments_full(id_us)
        elif command == 4:
            print('If you want to see didn`t completed tasks - 1\nComplete tasks- 2')
            stat = int(input('Write your number choose:'))
            to_do(id_us, stat)
        elif command == 5:
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


def posts(id_post, status):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    with open('post.json', 'w') as user:
        user.write(response.text)
    with open('post.json', 'rb') as read:
        data = json.load(read)
        for i in data:
            if i['id'] == id_post:
                title = i['title']
                body = i['body']
                if status == 1:
                    print(f"ID: {id_post} \nTitle: {title} \n")
                else:
                    print(f"D: {id_post} \nTitle: {title} \nBody: {body}")


def comments_full(id_comment):
    response = requests.get('https://jsonplaceholder.typicode.com/comments')
    with open('post_comment.json', 'w') as f:
        f.write(response.text)
    with open('post_comment.json', 'rb') as f:
        data = json.load(f)
        comment = 0
        for i in data:
            if i['postId'] == id_comment:
                comment += 1
                print('----------------------')
                print(f"Name: {i['name']} \nComment: {i['body']}")
        print(f"Sum of comments is {comment}")


def to_do(id_user, status):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    with open('to_do.json', 'w') as f:
        f.write(response.text)
    with open('to_do.json', 'rb') as f:
        data = json.load(f)
        for i in data:
            if i['userId'] == id_user:
                if status == 1:
                    title = i['title']
                    if i['completed'] == False:
                        print('----------------------')
                        print(f"Title:{title}")
                elif status == 2:
                    title = i['title']
                    if i['completed'] == True:
                        print('----------------------')
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
