grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

avarage_grade_dict = {}
sum_of_grades = 0
amount_of_grades = 0
avarage_grade = 0

for i in range(len(students)):
    for j in grades[i]:
        sum_of_grades = sum(grades[i])
        amount_of_grades = len(grades[i])
        avarage_grade = sum_of_grades / amount_of_grades
        
    avarage_grade_dict[students[i]] = avarage_grade

print(avarage_grade_dict)
