class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
        
        
        
class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")
   

s1 = Student("Alice", 20)
s1.greet()
s1.study()

p1  = Person("Alan", 25)
p1.greet()