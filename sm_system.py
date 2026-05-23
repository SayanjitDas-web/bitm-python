
class StudentManagementSystem:
    def __init__(self):
        self.storage = []
    
    def addStudent(self):
        name = input("enter the student name: ")
        roll = input("enter the student roll: ")    
        age = input("enter the student age: ")    
        isPresent = input("enter the student attendance: ")
        data = {"id":id,"name":name,"roll":roll,"age":age,"isPresent":bool(isPresent)}
        self.storage.append(data)
        
    def removeStudent(self):
        roll = input("enter roll to remove: ")
        for record in self.storage:
            if record["roll"] == roll:
                self.storage.remove(record)
            else:
                print("failed to find the record.")
                
    def updateStudent(self):
        roll = input("enter roll to remove: ")
        for record in self.storage:
            if record["roll"] == roll:
                while(True):
                    print("choose a field to update[ name | isPresent ]")
                    print("type (exit) to exit update mode -- ")
                    choice = input("enter a choice: ")
                    if(choice == "exit"):
                        break
                    match choice:
                        case "name":
                            name = input("enter new name to update: ")
                            record["name"] = name
                        case "isPresent":
                            isPresent = bool(input("give new value to isPresent to update : "))
                            record["isPresent"] = isPresent

    def showRecord(self):
        for record in self.storage:
            print()
            print("student name: ",record["name"])
            print("student roll: ",record["roll"])
            print("student age: ",record["age"])
            print("student isPresent: ",record["isPresent"])
            print("----------------------")
            
sms = StudentManagementSystem()
while(True):
    print()
    print("choose a option:")
    print("""
          add: +
          remove: -
          update: u
          show: s
          exit: q
    """)
    choice = input("enter an option: ")
    match choice:
        case "+":
            sms.addStudent()
        case "-":
            sms.removeStudent()
        case "u":
            sms.updateStudent()
        case "s":
            sms.showRecord()
        case "q":
            break
        case _:
            print("please choose an option.")