#take user input list 10 subjects, grades without using max highest marks and lowest marks
grades = []
for i in range(10):
    subject = input(f"Enter the name of subject {i+1}: ")
    grade = float(input(f"Enter the grade for {subject}: "))
    grades.append((subject, grade))

for subject, grade in grades:       
    print(f"Subject : {subject}  Grade : {grade}.") 