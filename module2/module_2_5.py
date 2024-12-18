def get_matrix(n, m, value):
    matrix = []
    
    for i in range(n):
        lst = []
        for j in range(m):
            lst.append(value)
            
        matrix.append(lst)
    
    return matrix

print(get_matrix(6, 6, 5))