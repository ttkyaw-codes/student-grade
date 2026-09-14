name = input("Input name:")
grades = [grade for grade in input("Input two grades separated by space:").split(" ")]
total_grade = 0
for grade in grades:
    total_grade += int(grade)
avg_grade = total_grade/len(grades)
    
print(f"Name: {name}\nAverage Grade: {avg_grade}\nTotal Grade: {total_grade}")