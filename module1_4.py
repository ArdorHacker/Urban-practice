my_string = input("Введи своё имя: ")
len_of_string = len(my_string)

my_string_upper = my_string.upper()
my_string_lower = my_string.lower()
my_string_trim = my_string.replace(" ", "")
my_string_first_child = my_string[0]
my_string_last_child = my_string[-1]

print(f"Кол-во символов: {len_of_string}\n"
      f"Строка в верхнем регистре: {my_string_upper}\n"
      f"Строка в нижнем регистре: {my_string_lower}\n"
      f"Строка без пробелов: {my_string_trim}\n"
      f"Первый элемент строки: {my_string_first_child}\n"
      f"Последний элемент строки:{my_string_last_child}")
