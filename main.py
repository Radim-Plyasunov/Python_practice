from math import sqrt

# Создаем пустой список, куда будем складывать историю
history = []

while True:
    print("\n--- Решение квадратного уравнения ---")
    print("(Введите 'q' для выхода или 'h' для просмотра истории)")

    # Вводим коэффициенты с проверкой на выход
    try:
        a_str = input("Введите a: ")
        if a_str.lower() == 'q': break
        if a_str.lower() == 'h':
            print("\n--- История последних 5 решений ---")
            for record in history:
                print(record)
            continue  # Возвращаемся в начало цикла

        a = float(a_str)
        b = float(input("Введите b: "))
        c = float(input("Введите c: "))
    except ValueError:
        print("Ошибка! Введите число.")
        continue

    # Логика решения
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        result = f"{min(x1, x2)} \n{max(x1, x2)}"
        print(result)
    elif D == 0:
        x = -b / (2 * a)
        result = str(x)
        print(result)
    else:
        result = "Нет корней"
        print(result)

    # Сохраняем результат в историю
    record = f"Уравнение: {a}x^2 + {b}x + {c} = 0 -> Ответ: {result}"
    history.append(record)  # Добавляем в конец списка

    # Ограничиваем историю 5 последними элементами
    if len(history) > 5:
        history.pop(0)  # Удаляем самый первый (старый) элемент