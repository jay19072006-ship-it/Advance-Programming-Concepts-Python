from package import get_student
from package import cal_result, check_result

name, roll_no = get_student()
marks = []

for i in range(3):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total, average = cal_result(marks)
result = check_result(average)

print("\n Student ")
print("Name:", name)
print("Roll No:", roll_no)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Result:", result)