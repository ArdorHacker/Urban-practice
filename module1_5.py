immutable_var = (1, 2, "abc")
#immutable_var[1] = 3 кортеж неизменяемый тип данных
print("Кортеж: ", immutable_var)

mutable_list = [1, 3, "hello", 22]
print("Список без изменений: ", mutable_list)
mutable_list[2] = "hey"
print("Изменёный список: ", mutable_list)
