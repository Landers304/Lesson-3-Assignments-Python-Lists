#Task 1:


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print("Sorted grades in descending order:", grades)




#Task 2: 


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)


#Task 3:


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
for index in range(len(grades)):
    if grades[index] < 80:
        grades[index] = "Failed"
print("Updated grades:", grades)

