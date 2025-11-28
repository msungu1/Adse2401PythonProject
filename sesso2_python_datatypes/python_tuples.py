# Python Tuples
# A Tuple is a built-in data type that represents an ordered collection of elements.
# Tuples allow duplicates and are immutable (their elements cannot be modified).
# Tuples are created using () parentheses or the tuple() constructor.
# Tuples are generally faster than lists as Python doesn’t have to worry about resizing them.

# Create a tuple of fruits
fruits = ("blueberry", "apple", "banana", "cherry", "avocado", "guava", "blueberry", "orange")

# Display the fruits in the tuple and their number
print(f"The fruits in the tuple are:\n{fruits}\nThe number of fruits in the tuple is: {len(fruits)}")

# Get and display the index of an item/element in the tuple
print(f"The index of 'avocado' is: {fruits.index('avocado')}")

# Get and display the number of occurrences of 'blueberry' in the tuple
print(f"'blueberry' appears {fruits.count('blueberry')} times in the fruits tuple")

# Combine two tuples to create a third one and display its content
combined_fruits = fruits + ("kiwi", "watermelon")
print(f"\nCombined fruits tuple: {combined_fruits}")

# create a sorted tuple of fruits
sorted_fruits = sorted(fruits)
print(f"Sorted fruits tuple: {sorted_fruits}")

# display the minimum and maximum items (fruits) in a tuples (least and highest fruits letterwise )
print(f"the least fruits lettewise is :{min(fruits)}" f"the highest fruits lettewise is :{max(fruits)}")

# Declaire a tumple of numbers
numbers = (1,2,3,4,5)

#display the tuple of numbers  and its sum
print(f"the numbers tuple contains :{numbers} and their sum is :{sum(numbers)}")

# display the first 3 numbers in the tuples
print(f"the first 3 numbers in the tuples are: {numbers[:3]}")
# display only the odd numbers from the numbers tuple
print(f"the odd numbers in the tuples are : {numbers[::2]}")

# use the 'any()' function to check if any element in the 'numbers 'tuple is true .
# in python ,non-zero numbers are considerd true.since all numbers in the tuple are non-zero,
# 'any(numbers)' will return true

any_true =any(numbers)
print(f"their only non-zero numbers in the 'numbers tuple are : {any_true}")

# use the 'all()' function to check if all elemnts in the numbers tuplesare trues
#since all elemnts (1,2,3,4,5) are non-zero, they  are all considered true , (numbers) will also return true

print(f"there are only non-zero numbers in the 'numbers tuple are : {any_true}")
