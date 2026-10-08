import requests
from urllib.parse import quote
import json

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
folder_path = f"disk:/{GROUP_NAME}"

response = requests.put(url, headers=headers, params={"path": folder_path})
if response.status_code in [201, 409]:
    print("Папка готова.")
else:
    print("Ошибка создания папки.")
    exit()

file_name = text.replace(" ", "_") + ".jpg"
path_to_file = f"disk:/{GROUP_NAME}/{file_name}"

print("Загружаем файл в облако")

url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
params = {"path": path_to_file}

response = requests.get(url, headers=headers, params=params)
if response.status_code != 200:
    print("Не удалось получить ссылку для загрузки.")
    exit()
 


upload_href = response.json()["href"]

response = requests.put(upload_href, data=cat_image_bytes)
if response.status_code == 201:
    print("Файл успешно загружен на Яндекс.Диск!")
else:
    print("Ошибка при загрузке файла.")
    exit()

print("Сохраняем отчет в JSON")

report = {
    "text_on_image": text,
    "file_size_bytes": len(cat_image_bytes),
    "yandex_path": path_to_file,
    "status": "success"
}

with open("backup_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

print("=== Программа успешно завершена! ===")
