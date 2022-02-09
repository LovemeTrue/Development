from liberty import *

post_list = getJsonURL("https://jsonplaceholder.typicode.com/posts")
comments = getJsonURL("https://jsonplaceholder.typicode.com/comments")

post = 0
user_search_input = search_input()

foundId = False

for dicts_posts in post_list:

    if user_search_input in dicts_posts["title"]:

        foundId = True

        print(dicts_posts['id'], "title: ", dicts_posts["title"],"\n")

if not foundId:
    print("Заголовков с таким текстов не найдено! \n")
    exit()

id_input = serach_id_post()

foundComm = False

for com in comments:
    
    if int(id_input) == com["postId"]:
       
        foundCom = True

        print(
        "title:", dicts_posts["title"],"\n",
        "message:", dicts_posts["body"],"\n")

        print(
        "name:", com["name"],"\n",
        "mail:", com["email"],"\n",
        "commment: ", com["body"],"\n")

if not foundCom:
    print('Пользователя не существует!')

# for dict_posts in com:
#     if dict_posts["userId"] == int(id_user_input):
#         print("title: ", dict_posts["title"],"\n")
#         print("message: ", dict_posts["body"],"\n")
#         post += 1
# if post == 0:
#     print("Сообщений этого пользователя нет")