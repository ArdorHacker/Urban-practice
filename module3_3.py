values_list = [52, True, "Urban"]
values_list2 = ["Hello World!", 1.45]
values_dict = {"a": 34, "b": "Urban", "c": 1.23}

def print_params(a = 1, b = "string", c = True):
    print(a, b, c)

print_params()
print_params(5, 6)
print_params(b = "Hello")
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 100)
#print_params(4, "Hello", False, 5.2) выводится ошибка most recent call last переюор аргументов