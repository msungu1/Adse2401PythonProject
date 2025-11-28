

import pickle
import pathlib
from person import Person

# Prompt the user for their name and age
name = input("Enter your name: \n")
age = input("Enter your age: \n")

# Create/instantiate a Person object
user = Person(name, age)

# Ensure the 'files' directory exists
files_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "files"))
os.makedirs(files_dir, exist_ok=True)

# Path to the file
file_path = os.path.join(files_dir, "person_os.txt")

# Display the path
print(f"Path to the 'person_os.txt' file is:\n{file_path}")

# Pickle the person object (append mode)
with open(file_path, "ab") as file:
    pickle.dump(user, file)

# Read back the last stored object (for verification)
with open(file_path, "rb") as file:
    try:
        while True:
            person_obj = pickle.load(file)
            print(f"Loaded Person: {person_obj.name}, {person_obj.age}")
    except EOFError:
        pass
