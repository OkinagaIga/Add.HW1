grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_mid = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
              sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
students_sort = sorted(students)

final_list = {students_sort[0]: grades_mid[0], students_sort[1]: grades_mid[1], students_sort[2]: grades_mid[2], students_sort[3]: grades_mid[3], students_sort[4]: grades_mid[4]}
print(final_list)