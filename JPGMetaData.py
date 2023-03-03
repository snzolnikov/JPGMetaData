# This is a sample Python script for get Meta data from JPEG files
# https://habr.com/ru/company/skillfactory/blog/551002/

from exif import Image
import datetime
import os.path



FORMAT_DATE_TIME = '%Y_%d_%m-%H_%M'
SOURCE_DIR = 'd:\\JPG\\'
FILES_AND_DIRS = [['.jpg','d:\\JPG']]

# Основная программа
for dir in FILES_AND_DIRS:
    for address, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.endswith(dir[0]):
                with open(os.path.join(SOURCE_DIR, file), "rb") as file_img:
                    image = Image(file_img)
                    try:
                        print('\nФайл:', file, 'Дата и время съемки:', image.datetime_original, ', Модель устройства:', image.model, '\n')
                    except:
                        print('Файл:', file, '- не содержит метаданных или атрибуты недоступны')

