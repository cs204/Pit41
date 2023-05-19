def main():
    amount_due = 50
    change_owed = 0

    while change_owed < amount_due:
        print(f"Нужная сумма: {int(amount_due - change_owed)}")
        coin = float(input("Вставьте монету: "))
        change_owed += coin


    change_owed -= amount_due
    print(f"Ваша сдача: {int(change_owed)}")

main()
