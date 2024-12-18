numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
cnt = 0

for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    
    for j in range(1, 16):
        if numbers[i] % j == 0:
            print("countable")
            cnt += 1
        
    if cnt == 2:
        primes.append(numbers[i])
        cnt = 0
        
    if cnt > 2:
        not_primes.append(numbers[i])
        cnt = 0
    
print(primes)
print(not_primes)