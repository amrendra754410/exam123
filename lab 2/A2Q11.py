#Objective No.- 11
# Write a program to accept student name and marks from the keyboard and creates a
# dictionary. Also display student marks by taking student name as input

students = {}

while True:
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

    choice = input("Do you want to add another student? (yes/no): ")
    if choice.lower() != "yes":
        break

search_name = input("Enter student name to search: ")

if search_name in students:
    print("Marks of", search_name, "are", students[search_name])
else:
    print("Student not found.")

