print("Введие 3 числа:")
first = input()
second = input()
third = input()

if first == second and first == third:
    print('Все 3 числа равны между собой')
elif first == second or first == third or second == third:
    print('2 числа равны между собой')
else:
    print('Числа не равны между собой')

