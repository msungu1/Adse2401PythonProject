from pathlib import Path
import pickle

# Define the Person class (if not already in person.py)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Prompt the user for their details
name = input("Enter your name: \n")
age = input("Enter your age: \n")

# Create a Person object
user = Person(name, age)

# Define the path using pathlib
files_dir = Path.cwd().parent / "files"
files_dir.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

file_path = files_dir / "person_pathlib.txt"

# Display the path
print(f"Path to the 'person_pathlib.txt' file is:\n{file_path}")

# Store the person object using pickle (append mode)
with file_path.open("ab") as file:
    pickle.dump(user, file)

# Read back all stored Person objects for verification
with file_path.open("rb") as file:
    try:
        while True:
            person_obj = pickle.load(file)
            print(f"Loaded Person: {person_obj.name}, {person_obj.age}")
    except EOFError:
        pass
