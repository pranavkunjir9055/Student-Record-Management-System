students = {}

def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    students[name] = {
        "Age": age,
        "Marks": marks
    }

    print("Student Added Successfully!")

def view_students():
    if len(students) == 0:
        print("No Records Found")
    else:
        for name, data in students.items():
            print(name, data)

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")