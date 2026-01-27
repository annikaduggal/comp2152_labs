#Question1: Student grades list (lists, basic operations)
grades = [85, 92, 78, 95, 88]

grades.append(90)
grades.sort()
print("sorted grades: ", grades)
print("highest grade: ", grades[-1])
print("lowest grade: ", grades[0])
print("total grades: ", len(grades))