import os
import pickle
from person import Person

# Ensure the 'files' directory exists (one level above current working directory)
def get_files_directory():
    files_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "files"))
    os.makedirs(files_dir, exist_ok=True)
    return files_dir

# Save a Person object to the file
def save_person(person, file_path):
    with open(file_path, "ab") as file:  # append binary mode
        pickle.dump(person, file)
    print(f"Person object saved: {person.name}, {person.age}")

# Load all Person objects from the file
def load_people(file_path):
    people = []
    with open(file_path, "rb") as file:
        try:
            while True:
                person_obj = pickle.load(file)
                people.append(person_obj)
        except EOFError:
            pass
    return people

# Main program
if __name__ == "__main__":
    # Prompt the user for their name and age
    name = input("Enter your name: \n")
    age = input("Enter your age: \n")

    # Create a Person object
    user = Person(name, age)

    # Get the files directory and file path
    files_dir = get_files_directory()
    file_path = os.path.join(files_dir, "person_os.txt")

    # Display the path
    print(f"Path to the 'person_os.txt' file is:\n{file_path}")

    # Save the Person object
    save_person(user, file_path)

    # Load and display all stored Person objects
    print("\nStored Person objects:")
    for person in load_people(file_path):
        print(f"- {person.name}, {person.age}")
