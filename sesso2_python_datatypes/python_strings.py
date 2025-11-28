# Python script to demonstrate strings and string functions

# declare a string variable
string_var = "hello mzungu from Python Programming"

# Display the string variable with first LETTER in uppercase using % and f-string
print("'string_var' with the first letter capitalised is %s" % string_var.capitalize())
print(f"'string_var' with the first letter capitalised is {string_var.capitalize()}")

# display the type of string_var
print(f"The type of 'string_var' is {type(string_var)}")

# display the content of string_var in uppercase
print(f"'string_var' in uppercase is {string_var.upper()}")

# display the contents of string_var in lowercase
print(f"'string_var' in lowercase is {string_var.lower()}")

# center the text with a specified width and given fill character
string_2_center = "programming"
print(string_2_center.center(32, "="))

# count and display the number of times a character appears in string ('o' in 'string_var')
print(f"The letter 'o' appears {string_var.count('o')} times in 'string_var'")

# display the highest and lowest alphabetical characters in 'string_var'
print(f"The highest alphabetical character in 'string_var' is {max(string_var)}")
print(f"The lowest alphabetical character in 'string_var' is {min(string_var)}")

# replace the 'he ' with 'He' and 'Python' with 'C#'
new_str = string_var.replace("he ", "He")
new_str = new_str.replace("Python", "C#")
print(f"The modified contents of 'string_var' is {new_str}")

# display another string variable for more string operations
my_string = "  Hello World  "

# get and display the number of characters using len()
print(f"The Length of the string \n'{my_string}' is: {len(my_string)} characters")

# islower() - check if all alphabetical characters are lowercase
print(f"Is the string \n'{my_string}' all lowercase? {my_string.islower()}")

# isupper() - check if all alphabetical characters are uppercase
print(f"Is the string \n'{my_string}' all uppercase? {my_string.isupper()}")

# lstrip() - remove any leading whitespace (from the left)
print(f"Remove the leading white space from '{my_string}' to get: \n{my_string.lstrip()}")

# rstrip() - removes any trailing whitespace (from the right)
print(f"Remove the trailing white space from '{my_string}' to get: \n{my_string.rstrip()}")

# strip() - removes any leading and trailing whitespace
print(f"Remove the trailing and leading white space from '{my_string}' to get: \n{my_string.strip()}")

# endswith() - checks if the specified string ends with the specified substring
print(f"Does the string '{my_string.strip()}' end with '123'? {my_string.strip().endswith('123')}")

# find() - locates the first occurrence of the specified substring
print(f"The first occurrence of 'World' in '{my_string}' is at index: {my_string.find('World')}")

# index() - finds the first occurrence of the substring, raises error when not found
try:
    print(f"The index of 'Hello' in '{my_string}' is: {my_string.index('Hello')}")
except ValueError:
    print("Substring not found!")

# count() - counts the number of occurrences of the substring or character
print(f"The letter 'l' appears {my_string.count('l')} times in '{my_string}'")

# rfind() - finds the last occurrence of the specified substring
print(f"The last occurrence of 'l' in '{my_string}' is at index: {my_string.rfind('l')}")

# startswith() - checks if the string starts with the given substring (prefix)
print(f"Does the string '{my_string.strip()}' start with 'Hello'? {my_string.strip().startswith('Hello')}")
