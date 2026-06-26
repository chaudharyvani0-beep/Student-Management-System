# list to store students

students = []

stu1 = {
    "name" : "vani",
    "age" : 18,
    "roll_number" : 1205,
    "marks" : 88
}
students.append(stu1)

stu2 = {
    "name"  : "goonika",
    "age"  : 18 ,
    "roll_number" : 1201,
    "marks" : 89

}

students.append(stu2)

stu3 = {
    "name" : "vishakha",
    "age" : 19 ,
    "roll_number" : 1206,
    "marks" : 62
}

students.append(stu3)

# function to add student to the list

def add_student():
    name = input("enter student name : ")
    age = int(input("enter student age : "))
    roll_number = int(input("enter student roll_number: "))
    marks = int(input("enter students marks : "))

    student = {
        "name" : name ,
        "age" : age,
        "roll_number" : roll_number ,
        "marks" : marks
    }
    for stu in students:
        if stu["roll_number"] == roll_number:
            print("Roll number already exists.")
            return

    students.append(student)

# function to view all students in the list

def view_student():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("-" * 30)
        print(f"Name        : {student['name']}")
        print(f"Age         : {student['age']}")
        print(f"Roll Number : {student['roll_number']}")
        print(f"Marks       : {student['marks']}")

# function to search for a student by roll number

def search_student():
    roll_number = int(input("enter the roll number of the student  searching for : "))
    for student in students :
        if student["roll_number"] == roll_number:
            print(f"student name is {student['name']} and age is {student['age']} and marks achieved is {student['marks']}")
            return
#     print("student not found")

# function to delete a student by roll number    

def del_student():
    roll_number = int(input("enter the roll number of student to be deleted : "))

    for student in students :
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student Deleted.")
            return 
#     print("student not found.") 

# function to update a student's marks by roll number

def update_student():
    roll_number = int(input("enter roll number of student to be updated : "))

    for student in students :
        if student["roll_number"] == roll_number:
            student["marks"] = int(input("enter new marks : "))
            print("Updated successfully.")
            return 
        
    print("student not found." )

# function to find the student with the highest marks

def topper():
    topper_student = max(students, key=lambda x: x["marks"])
    print("\n----- TOPPER -----")
    print(f"Name : {topper_student['name']}")
    print(f"Marks: {topper_student['marks']}")

# function to calculate the average marks of all students

def average_marks():
    if not students:
        print("No students found.")
        return

    total_marks = sum(student["marks"] for student in students)
    average = total_marks / len(students)
    print(f"Average marks of all students: {average:.2f}")


while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Show Topper")
    print("7. Average Marks ")
    print("8. Exit ")

    print("Enter your choice : ")
    try :
        choice = int(input())
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()              

    elif choice == 3:
        search_student()
    
    elif choice == 4 :
        del_student()
    
    elif choice == 5:
        update_student()

    elif choice == 6:
        topper()

    elif choice == 7:
        average_marks()

    elif choice == 8:
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
        







