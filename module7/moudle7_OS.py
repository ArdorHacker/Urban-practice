import os
import time

for root, dirs, files in os.walk("module7_1"):
    for file in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime(os.path.join(root, file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(os.path.join(root, file)).st_size
        parent_dir = root
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
