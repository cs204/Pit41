import sys

def count_lines(file_path):
    if not file_path.endswith(".py"):
        print("Неверное расширение файла. Файл должен иметь расширение .py")
        sys.exit(1)

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]
            return len(lines)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Использование: python lines.py <file_name.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    line_count = count_lines(file_path)

    print(f"{line_count}")

if __name__ == "__main__":
    main()