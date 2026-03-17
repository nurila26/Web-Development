students = []
n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted({student[1] for student in students})

second_lowest = grades[1]

second_students = [student[0] for student in students if student[1] == second_lowest]

second_students.sort()

for name in second_students:
    print(name)