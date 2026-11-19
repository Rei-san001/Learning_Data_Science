# simply means many forms 

# Function Overriding (inherited class)
# Function Overloading (own class)

# Method Overriding 
class Animal:
    def sound(self):
        print("generic sound")
        
class Dog(Animal):
    def sound(self):
        print("Woof")
        
my_dog = Dog()
my_dog.sound()


# Method Overloading 
class Calculator:
    def add(self, a, b):
        return a+b
    
    def add(self, a, b, c):
        return a+b+c

calc = Calculator()
result = calc.add(4,5,6)
print(result)