def is_prime(func):
    def wrapper(*args):
        digit = func(*args) # исходное число
        prime_dividers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # простые делители
        cnt = 0 # счетчик делителей

        if digit not in prime_dividers:
            cnt = 1

        if digit == 0 or digit == 1: # ни простое, ни составное число
            print("Ни простое, ни составное число")
            return digit

        for i in prime_dividers: # считаем кол-во делителей
            if digit % i == 0:
                cnt += 1

        if cnt == 2:
            print("Простое")

        elif cnt > 2:
            print("Составное")

        return digit

    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

