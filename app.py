name = input("Input name:")
grades = [grade for grade in input("Input two grades separated by space:").split(" ")]
avg_grade = 0
for grade in grades:
    avg_grade += int(grade)
avg_grade = avg_grade/len(grades)
if avg_grade >= 40:
    status = "Passed"
elif avg_grade > 0 and < 40:
    status = "Failed"
else:
    status = "Error"
    
print(f"Name: {name}\nAverage Grade: {avg_grade}\nStaus: {status}")
