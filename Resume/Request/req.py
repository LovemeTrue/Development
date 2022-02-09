
from liberty import *

id_list = getJsonURL("https://jsonplaceholder.typicode.com/users")
posts = getJsonURL("https://jsonplaceholder.typicode.com/posts")


for dicts in id_list:
    print(dicts["id"], dicts["username"]) # Выводит список юзеров в консол
    
print("\n")

id_user_input = user_input()

for user in id_list:
    if (user['id'] == int(id_user_input)):
        print("\n")
        print("Сообщения пользователя: ","\n")
        break
else:
    print('Пользователя не существует!')

postFound = False

for dict_posts in posts:
    if dict_posts["userId"] == int(id_user_input):
        postFound = True
        print("title: ", dict_posts["title"],"\n")
        print("message: ", dict_posts["body"],"\n")
if not postFound:
    print("Сообщений этого пользователя нет")