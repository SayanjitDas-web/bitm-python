class StudentManagementSystem:

    def __init__(self, org_name):
        self.storage = []
        self.org_name = org_name
        self.file_name = "data.txt"

        open(self.file_name, "a").close()

        self.load_data()

    def load_data(self):
        self.storage.clear()

        with open(self.file_name, "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()

                if line != "":
                    name, roll, age = line.split(",")

                    data = {
                        "name": name,
                        "roll": int(roll),
                        "age": int(age)
                    }

                    self.storage.append(data)

    def save_data(self):
        with open(self.file_name, "w") as file:

            for student in self.storage:
                file.write(
                    f"{student['name']},{student['roll']},{student['age']}\n"
                )

    def add_student(self):

        student_name = input("Enter student name: ")
        student_roll = int(input("Enter roll no: "))
        student_age = int(input("Enter age: "))

        for student in self.storage:
            if student["roll"] == student_roll:
                print("Student with that roll already exists.")
                return

        data = {
            "name": student_name,
            "roll": student_roll,
            "age": student_age
        }

        self.storage.append(data)

        self.save_data()

        print("Student added successfully!")

    def delete_student(self):

        student_roll = int(input("Enter roll number: "))

        for student in self.storage:

            if student["roll"] == student_roll:

                self.storage.remove(student)

                self.save_data()

                print("Student deleted successfully.")
                return

        print("Student not found.")

    def update_student(self):

        option = input("Choose field [name / age]: ")

        student_roll = int(input("Enter student roll: "))

        for student in self.storage:

            if student["roll"] == student_roll:

                if option == "name":

                    new_name = input("Enter new name: ")

                    student["name"] = new_name

                    self.save_data()

                    print("Student name updated successfully.")

                elif option == "age":

                    new_age = int(input("Enter new age: "))

                    student["age"] = new_age

                    self.save_data()

                    print("Student age updated successfully.")

                else:
                    print("Invalid option.")

                return

        print("Student not found.")

    def show_storage(self):

        if len(self.storage) == 0:
            print("No student records found.")
            return

        print(f"\n===== {self.org_name} STUDENT RECORDS =====")

        for student in self.storage:

            print("\n------------------")
            print(f"Student Name : {student['name']}")
            print(f"Student Roll : {student['roll']}")
            print(f"Student Age  : {student['age']}")
            print("------------------")


sms = StudentManagementSystem("GENEX")

while True:

    print("\n===== Student Management System =====")
    print("[a] Add Student")
    print("[d] Delete Student")
    print("[u] Update Student")
    print("[s] Show Students")
    print("[q] Quit")

    option = input("Enter option: ")

    if option == "a":
        sms.add_student()

    elif option == "d":
        sms.delete_student()

    elif option == "u":
        sms.update_student()

    elif option == "s":
        sms.show_storage()

    elif option == "q":
        print("Exiting program...")
        break

    else:
        print("Invalid option.")