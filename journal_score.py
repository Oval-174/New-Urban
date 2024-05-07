grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students), students)
list_students = list(sorted(students))
print(list_students)
jornal_score = {}
for i in range (0, len(list_students)):
    jornal_score[list_students[i]] = round(sum(grades[i]) / len(grades[i]), 2)
print(type(jornal_score), jornal_score)
