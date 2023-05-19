def main():
    fruit_calories = {
        "Apple": 130,
        "Lime": 20,
        "Tomato": 57
    }

    fruit = input("Фрукт: ")
    if fruit in fruit_calories:
        calories = fruit_calories[fruit]
        print(f"Калории: {calories}")
    else:
        print("Калории для этого фрукта неизвестны.")

main()