import json

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    student_id = input("Enter ID: ")
    program = input("Enter program: ")

    students = load_data()


    if any(s["id"] == student_id for s in students):
        print(" Student ID already exists!")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "program": program
    }
    students.append(student)
    save_data(students)
    print(" Student added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Program: {s['program']}")

def search_student():
    sid = input("Enter student ID to search: ")
    students = load_data()
    for s in students:
        if s["id"] == sid:
            print(f" Found: ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Program: {s['program']}")
            return
    print(" Student not found.")

def update_student():
    sid = input("Enter student ID to update: ")
    students = load_data()
    for s in students:
        if s["id"] == sid:
            print("  Student found. Leave blank to keep old value.")
            name = input(f"Enter new name (old: {s['name']}): ") 
            age = input(f"Enter new age (old: {s['age']}): ") 
            program = input(f"Enter new program (old: {s['program']}): ") 

            s["name"] = name
            s["age"] = age
            s["program"] = program

            save_data(students)
            print(" Student updated successfully!")
            return
    print("  Student not found.")

def delete_student():
    sid = input("Enter student ID to delete: ")
    students = load_data()
    for i, s in enumerate(students):
        if s["id"] == sid:
            print(f"Really na kar yar Are you sure you want to delete {s['name']} (ID: {sid})? (y/n)")
            confirm = input().lower()
            if confirm == 'y':
                students.pop(i)
                save_data(students)
                print("  Student deleted.")
            else:
                print(" Delete cancelled.")
            return
    print(" Student not found.")

def menu():
    while True:
        print(" ** Student Record Menu ***")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose option (1-6): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print(" Exiting... Bye Zeeshan!")
            break
        else:
            print("  Invalid choice. Try again!")

if __name__ == "__main__":
    menu()
