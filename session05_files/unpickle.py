import pickle
import os

# Path to the 'person_os.txt' file
file_pathn = os.path.abspath(os.path.join(os.getcwd(), "..", "files", "person_os.txt"))

# List to hold the person objects
persons = []

# Unpickle all Person objects from the file
with open(file_pathn, 'rb') as f:
    while True:
        try:
            unpickled_person = pickle.load(f)
            persons.append(unpickled_person)
        except EOFError:
            break  # End of file reached

# Access and display the unpickled persons' details/attributes
if persons:
    print("Unpickled persons:")
    for person in persons:
        # Assuming Person has attributes 'name' and 'age'
        print(f"Name: {person.name}, Age: {person.age}")
else:
    print("No persons found in the file.")




# python script/file to unpickle the persons details from the  person_pathlib.txt file and displsy them using the pathlib module


# to do
