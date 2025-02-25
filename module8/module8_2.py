def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    cnt = 0

    if not isinstance(numbers, int):
        for i in numbers:
            try:
                result += i
                cnt += 1

            except TypeError:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы - {i}")

    else:
        return None

    return result, cnt, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)

        try:
            avg = result[0] / result[1]

        except TypeError:
            print('В numbers записан некорректный тип данных')
            return None

    except ZeroDivisionError as ex:
        print(ex)
        return 0

    return avg

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать