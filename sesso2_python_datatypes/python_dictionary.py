# Python Dictionaries
# Dictionaries are built-in data types that represent a collection of key-value pairs.
# They are unordered, mutable, and can store elements of different types.
# Each element in a dictionary is accessed by its key rather than its index.
# Dictionaries are created using {}. Some dictionary operations are demonstrated below.

# student dictionary declaration
student = {"name": "Roberto", "age": 25, "favorite_color": "blue", "major": "software engineering"}

# display the length (number of key-value pairs) of the student dictionary
print(f"The number of key-value pairs in the student dictionary is:\n{len(student)}")

# fetch and display a view object of the keys in the student dictionary
print(f"The keys in student dictionary are:\n{student.keys()}")

# fetch and display a view object of the values in the student dictionary
print(f"The values in student dictionary are:\n{student.values()}")

# fetch and display a view object of the contents in the student dictionary
print(f"The items in student dictionary are:\n{student.items()}")

# get and display a value using its key from the student dictionary
print(f"The key 'name' in student dictionary is:\n{student.get('name')}")

# remove and display a value using its key from the student dictionary
# else return/give back an optional default value
phone_no = student.pop("phone_no", "Not Specified")
print(f"The phone number in student dictionary is:\n{phone_no}")

# remove and display the contents of the last key-value pair in the student dictionary
print(f"The last key-value pair removed from student dictionary is:\n{student.popitem()}")

# Update/modify and display the contents of the student dictionary
student.update({"age": 21, "grade": "A", "phone": "07123456", "favorite_color": "blue"})
print(f"The updated student dictionary is:\n{student.items()}")

# create a copy of the student dictionary
copy_of_student = student.copy()
print(f"The content of the copied student dictionary is:\n{copy_of_student}")

# fetch and return the value associated with a given key
# if not found, assign it with a default value
major = student.setdefault("major", "Software Engineering")
print(f"The major in student dictionary is:\n{major}")

# create and display a new dictionary for the keys of an existing dictionary
# dict.fromkeys() creates a new dictionary with given keys and default values
new_dict = dict.fromkeys(student.keys(), "N/A")
print(f"A new dictionary created from the keys of 'student' with default values:\n{new_dict}")

# display the remaining key-value pairs in the student dictionary
print(f"The remaining key-value pairs in student dictionary are:\n{student}")

# find out and display whether a given key exists/is present in a dictionary
key_to_check = "grade"
if key_to_check in student:
    print(f"Yes, the key '{key_to_check}' exists in the student dictionary with value: {student[key_to_check]}")
else:
    print(f"No, the key '{key_to_check}' does not exist in the student dictionary.")
