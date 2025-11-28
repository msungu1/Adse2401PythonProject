# Python script to demonstrate simple comprehension operations on a set and dictionary

# A list of names and initials (fixed the syntax error with 'Nemo,' → 'Nemo')
names = ['sam', 'paul', 'PAUL', 'Nemo', 'j', 'memo']
print(f"The original list of names and initials:\n{names}\n")

# Set comprehension: Get unique names longer than 1 character, properly capitalized
unique_names = {name.capitalize() for name in names if len(name) > 1}

# Display the unique set of properly capitalized names
print(f"Unique names with more than one letter (capitalized):")
print(unique_names)
print()

# Dictionary of letter occurrences (mixed case)
test_dic = {'l': 10, 'b': 34, 'z': 2, 'N': 4, 'L': 4, 'Z': 5}
print(f"Original letter count dictionary:")
print(test_dic)
print()

# Dictionary comprehension: Combine counts regardless of case (e.g. 'l' + 'L' → 'l': 14)
letter_count = {
    k.lower(): test_dic.get(k.lower(), 0) + test_dic.get(k.upper(), 0)
    for k in test_dic.keys()
}

# Display the case-insensitive total count
print(f"Total letter count (case-insensitive):")
print(letter_count)