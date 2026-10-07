import requests
text = input("Введите текст, который будет на картинке с котом: ")
token = input("Введите ваш токен Яндекс.Диска: ")

if not text or not token:
    print("Вы не ввели текст или токен. ")
    exit()

GROUP_NAME = "pyapi-160"