def main():
    menu = {
        "кофе": 20.00,
        "чай": 10.00,
        "булочка": 5.00,
        "салат": 30.40,
        "пирожное": 45.50
    }

    total_cost = 0.0
    selected_dishes = []

    try:
        while True:
            dish = input("Блюдо: ").lower()
            if dish in menu and dish not in selected_dishes:
                total_cost += menu[dish]
                selected_dishes.append(dish)
    except EOFError:
        if selected_dishes:
            print("Блюдо:", end=" ")
            print(" Блюдо: ".join(selected_dishes))
            print(f"Сумма: {total_cost:.2f}")


main()
