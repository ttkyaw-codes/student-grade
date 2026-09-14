name = input("Input name:")
grades = [grade for grade in input("Input two grades separated by space:").split(" ")]
total_grade = 0
for grade in grades:
<<<<<<< HEAD
    total_grade += int(grade)
avg_grade = total_grade/len(grades)
    
print(f"Name: {name}\nAverage Grade: {avg_grade}\nTotal Grade: {total_grade}")
=======
    avg_grade += int(grade)
avg_grade = avg_grade/len(grades)
if avg_grade >= 40:
    status = "Passed"
elif avg_grade > 0 and < 40:
    status = "Failed"
else:
    status = "Error"
print("placeholder")
print(f"Name: {name}\nAverage Grade: {avg_grade}\nStaus: {status}")
>>>>>>> fc61e1032b19cc313d9c67d3419554a176e437b9
