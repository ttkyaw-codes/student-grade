name = input("Input name:")
grades = [grade for grade in input("Input two grades separated by space:").split(" ")]
avg_grade = 0
for grade in grades:
    avg_grade += int(grade)
avg_grade = avg_grade/len(grades)
    
print(f"Name: {name}\nAverage Grade: {avg_grade}")