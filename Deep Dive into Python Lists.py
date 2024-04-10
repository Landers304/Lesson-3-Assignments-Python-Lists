#Task 1: 


students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for index in range(len(students)):
    if grades[index] < 80:
        print(students[index], grades[index], activities[index])




#Task 2:
        

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

students_approved = []
for index in range(len(students)):
    if grades[index] >= 80:
        students_approved.append(students[index])

print("The students that are approved:", students_approved)




#Task 3: 

        
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

students_approved = []
for index in range(len(students)):
    if grades[index] >= 80:
        students_approved.append(students[index])

print("The students that are approved:", students_approved)