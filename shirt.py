import sys
import os
from PIL import Image, ImageOps

def apply_tshirt(input_file, output_file):
    tshirt_file = "shirt.png"

    try:
        # Открываем файл футболки
        tshirt = Image.open(tshirt_file)

        # Открываем входной файл
        input_image = Image.open(input_file)

        # Изменяем размер и обрезаем до размеров футболки
        resized_image = ImageOps.fit(input_image, tshirt.size)

        # Наложение футболки на входное изображение
        resized_image.paste(tshirt, (0, 0), mask=tshirt)

        # Сохраняем результат
        resized_image.save(output_file)

        #djjjddjd
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        sys.exit()
    except Exception as e:
        print("Ошибка при обработке изображения:", str(e))
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Слишком много аргументов в командной строке.")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Слишком мало аргументов в командной строке")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]

    valid_extensions = [".jpg", ".jpeg", ".png"]

    if input_extension.lower() not in valid_extensions or output_extension.lower() not in valid_extensions:
        print("Ввод и вывод имеют разные расширения")
        sys.exit()

    if input_extension.lower() != output_extension.lower():
        print("Ввод и вывод имеют разные расширения.")
        sys.exit()

    if not os.path.exists(input_file):
        print("Файл не существует.")
        sys.exit()

    apply_tshirt(input_file, output_file)
