def main():
    answer = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
    answer = answer.lower()

    if answer == "42" or answer == "сорок два":
        print("Да")
    else:
        print("Нет")

main()
