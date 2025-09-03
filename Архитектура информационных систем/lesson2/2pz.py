# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип

n1 = int(input("Введи первое число: "))
n2 = int(input("Введи второе число: "))

operations = ['+', '-', '*', '/']
operation = input(f"Какую операцию хочешь выполнить? {operations}: ")

if operation in operations:
    if operation == operations[0]:
        answer = n1 + n2
    elif operation == operations[1]:
        answer = n1 - n2
    elif operation == operations[2]:
        answer = n1 * n2
    elif operation == operations[3]:
        if n2 == 0:
            answer = 0
        else:
            answer = n1 / n2
    print(answer)
    print(type(answer))
else:
    print(f">> [ОШИБКА] Указана некорректная операция {operations}")