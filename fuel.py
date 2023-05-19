def main():
    while True:
        try:
            fraction = input("Дробь: ")
            x, y = map(int, fraction.split('/'))

            if x <= 0 or y <= 0 or x > y:
                print("Некорректная дробь. Повторите ввод.")
                continue

            percentage = (x / y) * 100
            rounded_percentage = round(percentage)

            if rounded_percentage <= 1:
                print("E")
            elif rounded_percentage >= 99:
                print("F")
            else:
                print(f"{rounded_percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            print("Некорректный ввод. Повторите ввод.")

if __name__ == '__main__':
    main()
