# Basically what it does in simple terms is that when we create an abstract class, we are defining a blueprint for other classes to follow. It allows us to define methods that must be implemented in any subclass, ensuring a consistent interface across different implementations. This is useful for creating a common structure and enforcing certain behaviors in derived classes.


from abc import ABC, abstractmethod # that's how we import abstract class and abstract method

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

sq = Square(5)
print(f"Square Area: {sq.area()}")
print(f"Square Perimeter: {sq.perimeter()}")

c = Circle(3)
print(f"Circle Area: {c.area()}")
print(f"Circle Perimeter: {c.perimeter()}")


# so as you can see, we have to include the shape class in the square and circle class otherwise it will give an error. This is because we are inheriting the abstract class and we have to implement the abstract methods in the child class.