from abc import ABC, abstractmethod

# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}")

# Composite
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)

# Client Code
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Create folders
    folder1 = Folder("folder1")
    folder2 = Folder("folder2")
    root = Folder("root")

    # Build the hierarchy
    folder1.add(file1)
    folder1.add(file2)

    folder2.add(file3)

    root.add(folder1)
    root.add(folder2)

    # Display the structure
    root.display()
