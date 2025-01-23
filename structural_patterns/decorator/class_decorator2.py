def log_class_creation(cls):
    class WrappedClass(cls):
        def __init__(self, *args, **kwargs):
            print(f"Creating an instance of {cls.__name__}")
            super().__init__(*args, **kwargs)
    return WrappedClass

@log_class_creation
class MyClass:
    def __init__(self, name):
        self.name = name

# Test the decorator
obj = MyClass("John")



def add_greeting(cls):
    cls.greet = lambda self: f"Hello, I am {self.name}"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorator
p = Person("Alice")
print(p.greet())  # Output: Hello, I am Alice