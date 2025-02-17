"""
## There are important references between MetaClass magic functions and regular classes:

### **1. __new__**:

- **In Regular Classes**:
    - **__new__** is responsible for creating a new instance of the class. It’s called before __init__.
    - It’s rarely overridden, unless you're customizing instance creation or using **immutable types** like tuples or strings.
    - **Signature**: __new__(cls, *args, **kwargs)
- **In Metaclasses**:
    - **__new__** is called when creating the **class** (not the instance). It controls the creation of a class, and you can modify the class itself.
    - It’s responsible for returning the new class object.
    - **Signature**: __new__(cls, name, bases, dct) (where name is the class name, bases are the base classes, and dct is the class dictionary).

---

### **2. __init__**:

- **In Regular Classes**:
    - **__init__** is used to initialize the newly created instance after __new__.
    - It's called when an instance is created using the class.
    - **Signature**: __init__(self, *args, **kwargs)
- **In Metaclasses**:
    - **__init__** is used to initialize the **class** (not an instance). It’s called after the class is created by the __new__ method, and you can modify class attributes.
    - **Signature**: __init__(cls, name, bases, dct) (where name, bases, and dct are as described in __new__).

---

### **3. __call__**:

- **In Regular Classes**:
    - **__call__** allows an **instance** to be callable, i.e., it enables the use of the instance as a function (e.g., instance()).
    - **Signature**: __call__(self, *args, **kwargs)
- **In Metaclasses**:
    - **__call__** is invoked when a **new instance of the class** (which uses the metaclass) is created.
    - It overrides the default class instantiation behavior to control how instances are created (e.g., Singleton pattern).
    - **Signature**: __call__(cls, *args, **kwargs) (where cls is the class itself).
"""

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self, x):
        self.x = x
        print("Loading database...")


d1 = Database(1)
d2 = Database(2)

print(d1 == d2)
print(d1.x, d2.x)