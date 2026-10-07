import requests
from urllib.parse import quote
GROUP_NAME = "pyapi-160"
text = input("Введите текст, который будет на картинке с котом: ")
token = input("Введите ваш токен Яндекс.Диска: ")

if not text or not token:
    print("Вы не ввели текст или токен. ")
    exit()

print("Получаем картинку")

safe_text = quote(text)
url = f"https://cataas.com/cat?text={safe_text}"

response = requests.get(url)

if response.status_code != 200:
    print("Не удалось получить картинку.")
    exit()
 


cat_image_bytes = response.content
print("Картинка успешно получена!")