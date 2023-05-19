def main():
    file_name = input("File name: ")

    if file_name.lower().endswith(".gif"):
        print("image/GIF")
    elif file_name.lower().endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif file_name.lower().endswith(".png"):
        print("image/PNG")
    elif file_name.lower().endswith(".pdf"):
        print("image/PDF")
    elif file_name.lower().endswith(".txt"):
        print("Тип файла: текстовый файл")
    elif file_name.lower().endswith(".zip"):
        print("Тип файла: ZIP-архив")
    else:
        print("Неизвестный тип файла")

main()