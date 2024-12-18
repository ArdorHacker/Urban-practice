def get_multiplied_digits(number):
    str_number = str(number)
    fitst = int(str_number[0])

    if len(str_number) <= 1:
        return fitst
        
    else:
        return fitst * get_multiplied_digits(int(str_number[1:]))
    
result = get_multiplied_digits(10)
print(result)