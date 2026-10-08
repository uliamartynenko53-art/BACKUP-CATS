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

print("Создаем папку на Яндекс.Диске")
url = "https://cloud-api.yandex.net/v1/disk/resources"
headers = {"Authorization": f"OAuth {token}"}
params = {"path": f"disk:/{GROUP_NAME}"}

response = requests.put(url, headers=headers, params=params)

if response.status_code in [201, 409]:
    print("Папка готова.")
else:
    print("Ошибка создания папки.")
    exit()
