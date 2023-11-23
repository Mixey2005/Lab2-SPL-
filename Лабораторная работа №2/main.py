def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)

def process_data(input_data):
    if isinstance(input_data, list):
        positive_index = -1
        total_sum = 0
        for i, num in enumerate(input_data):
            if num > 0:
                positive_index = i
            if positive_index != -1 and i > positive_index:
                total_sum += num
        input_data = [num for num in input_data if num != 0]
        return total_sum, input_data
    elif isinstance(input_data, dict):
        min_key = min(input_data, key=input_data.get)
        return input_data[min_key]
    elif isinstance(input_data, int):
        return int(str(input_data)[::-1])
    elif isinstance(input_data, str):
        words = input_data.split()
        return len(words)
    else:
        return "Неизвестный тип данных"

def process_matrix(matrix):

    all_positive = all(any(element > 0 for element in row) for row in matrix)
    if all_positive:
        result_matrix = [[-element for element in row] for row in matrix]
    else:
        result_matrix = matrix
    return result_matrix

def try_except_finally_example():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    except ValueError:
        print("Ошибка: Введите корректные числа!")
    else:
        print(f"Результат: {result}")
    finally:
        print("Программа завершена.")

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Задание 1 (Функция для определения анаграмм)")
        print("2. Задание 2 (Функция для обработки разных типов данных)")
        print("3. Задание 3 (Проверка и изменение матрицы)")
        print("4. Задание 4 (Программа с использованием try/except/finally)")
        print("0. Выход")

        choice = input("Выберите номер задания (или 0 для выхода): ")

        if choice == '1':
            word1 = input("Введите первое слово: ")
            word2 = input("Введите второе слово: ")
            result = are_anagrams(word1, word2)
            print(f"Результат: {'Анаграммы' if result else 'Не анаграммы'}")

        elif choice == '2':
            data = eval(input("Введите данные (список, словарь, число или строку): "))
            result = process_data(data)
            print(f"Результат: {result}")

        elif choice == '3':
            matrix = eval(input("Введите матрицу (список списков): "))
            result_matrix = process_matrix(matrix)
            print("Результат:")
            for row in result_matrix:
                print(row)

        elif choice == '4':
            try_except_finally_example()

        elif choice == '0':
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите номер задания из меню.")

if __name__ == "__main__":
    main_menu()
