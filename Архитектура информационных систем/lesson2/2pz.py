# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип

n1 = int(input("Введи первое число\n> "))
n2 = int(input("Введи второе число\n> "))
operation = input("Какую операцию хочешь выполнить? [плюс, минус, умнж, дел]\n> ")

if operation == "плюс":
    answer = n1 + n2
    print(f">> Результат: {answer}")
    print(f">> Тип переменной answer: {type(answer)}")
elif operation == "минус":
    answer = n1 - n2
    print(f">> Результат: {answer}")
    print(f">> Тип переменной answer: {type(answer)}")
elif operation == "умнж":
    answer = n1 * n2
    print(f">> Результат: {answer}")
    print(f">> Тип переменной answer: {type(answer)}")
elif operation == "дел":
    answer = n1 / n2
    print(f">> Результат: {answer}")
    print(f">> Тип переменной answer: {type(answer)}")
else:
    print(">> Указана некорректная операция")
