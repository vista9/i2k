# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
# 5. Повторять все заново с использованием while
# 6. Завершить программу если пользователь введет 'exit'

while True:
    n1 = input("Введи первое число: ")
    if n1 == 'exit':
        exit()

    n2 = input("Введи второе число: ")
    if n2 == 'exit':
        exit()

    try:
        n1 = int(n1)
        n2 = int(n2)
    except:
        print(">> [ОШИБКА] Нужно указать число")
    else:
        operations = ['+', '-', '*', '/', 'exit']
        operation = input(f"Какую операцию хочешь выполнить? ({', '.join(operations)}): ")
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
            elif operation == operations[4]:
                exit()
        
            print(answer)
            print(type(answer))
        else:
            print(f">> [ОШИБКА] Указана некорректная операция ({', '.join(operations)})")
