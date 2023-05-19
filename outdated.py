def main():
    months = ["январь", "февраль", "март", "апрель",
              "май", "июнь", "июль", "август", "сентябрь", "октябрь",
              "ноябрь", "декабрь"]

    while True:
        date_input = input("Дата: ")
        parts = date_input.split()

        if len(parts) == 3:
            day = parts[0]
            month = parts[1].lower()
            year = parts[2]
        elif len(parts) == 1:
            date = date_input.replace(".", " ").split()
            if len(date) != 3:
                print("Неправильный формат даты. Попробуйте снова.")
                continue
            day, month, year = date
        else:
            print("Неправильный формат даты. Попробуйте снова.")
            continue

        month_index = -1
        if month.isdigit():
            month_index = int(month) - 1
        else:
            for index, month_name in enumerate(months):
                if month_name == month:
                    month_index = index
                    break

        if month_index < 0 or month_index > 11:
            print("Неправильный формат даты. Попробуйте снова.")
            continue

        try:
            formatted_date = f"{int(year):04d}-{month_index + 1:02d}-{int(day):02d}"
            print(f"Отформатированная дата: {formatted_date}")
            break
        except ValueError:
            print("Неправильный формат даты. Попробуйте снова.")


main()
