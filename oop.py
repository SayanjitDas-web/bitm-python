class Animal:
    def __init__(self,name):
        self.name = name
        
    def move(self):
        print(f"{self.name} is moving.")
        
    def sound(self):
        print(f"{self.name} is making sound")
        
class Tiger(Animal):
    def __init__(self,):
        super().__init__("Tiger")
        
    def sound(self):
        print(f"{self.name} is making sound of a tiger")
        
class Cat(Animal):
    def __init__(self,):
        super().__init__("Cat")
        
    def sound(self):
        print(f"{self.name} is making sound of a cat")
        
animal = Animal("Dog")
        
tiger1 = Tiger()
cat1 = Cat()

tiger1.move()
cat1.move()

tiger1.sound()
cat1.sound()

animal.move()
animal.sound()

class Database:
    def __init__(self,name):
        self.name = name
        self.storage = []
        
    def add_data(self,data):
        self.storage.append(data)
        print("Data got added.")
        
    def delete_data(self,data):
        self.storage.remove(data)
        print("Data got removed.")
        
    def update_data(self,ind,new_data):
        self.storage[ind] = new_data
        print("Data updated.")
        
    def get_data(self,ind):
        return self.storage[ind]
    
db1 = Database("Student Record")

db1.add_data("Student1")
db1.add_data("Student2")
db1.add_data("Student3")

print(db1.get_data(1))