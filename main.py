from pathlib import Path
from PIL import Image
from rembg.bg import remove
import io
import os

# получаем список файлов в папке

total_items = os.listdir('image_come\\')

def convert_imag():
    # пробегаемся создавая путь до каждого файла (откуда берем и куда запишем готовый)
    for x in total_items:
        input_path = f'image_come\{x}'
        output_path = f'image_out\done_{x}'

        # надо открыть картинку
        img = Image.open(input_path)
        # снимаем фон
        result = remove(img)
        # # сохраняем результат
        if '.jpg' in output_path:
            output_path = output_path.replace('.jpg', '.png')
            result.save(output_path)
        else:
            result.save(output_path)

convert_imag()



