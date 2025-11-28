# Python Sets
# A Python set is a built-in type that represents an unordered collection of elements.
# Sets DON'T allow duplicates and are mutable. They are suitable for tasks that involve
# checking membership, removing duplicates, and performing mathematical operations like
# intersection, union, difference, and symmetric_difference.
# Sets are created using curly braces {} or the set() constructor.

# Create a set of fruits
fruits = {"apple", "banana", "cherry", "durian", "elephant apple"}

# Display the contents of the fruit set
print(f"The fruits set contains {len(fruits)} items")

# Display the fruits in the fruit set
print(f"The fruits set contains: {fruits}")

# Add 'orange' to the fruit set
fruits.add("orange")
print(f"After adding orange, the fruits set contains {len(fruits)} items")

# Remove 'banana' from the fruit set
fruits.remove("banana")
print(f"After removing banana, the fruits set contains {len(fruits)} items")

# Discard 'cherry' from the fruit set
fruits.discard("cherry")
print(f"After discarding cherry, the fruits set contains: {fruits}")

# Remove the last item (random because sets are unordered)
popped_fruit = fruits.pop()
print(f"After popping '{popped_fruit}', the fruits set contains: {fruits}")

# Declare another set of fruits
more_fruits = {"pear", "avocado", "mango", "pineapple"}

# Create a new combined set of fruits and display it
combined_fruits = fruits.union(more_fruits)
print(f"The combined fruits set contains:\n{combined_fruits}")

# Get and display the common fruits in both sets
common_fruits = fruits.intersection(more_fruits)
print(f"The common fruits set contains:\n{common_fruits}")

# Get and display the fruits that are in 'fruits' but not in 'more_fruits'
different_fruits = fruits.difference(more_fruits)
print(f"The different fruits set contains:\n{different_fruits}")

# Get and display the fruits that are in either set but not both
symmetric_diff_fruits = fruits.symmetric_difference(more_fruits)
print(f"The fruits that are either in 'fruits' or 'more_fruits' but not both are:\n{symmetric_diff_fruits}")

# Check and display whether 'fruits' is a subset of 'more_fruits'
print(f"'fruits' set is a subset of 'more_fruits': {fruits.issubset(more_fruits)}")

# Check and display whether 'fruits' and 'more_fruits' have no common elements
print(f"'fruits' set is disjoint with 'more_fruits': {fruits.isdisjoint(more_fruits)}")

# Create another fruit set and update the 'fruits' set
other_fruits = {"watermelon", "strawberry", "blueberry"}
fruits.update(other_fruits)
print(f"After updating, the fruits set contains:\n{fruits}")

# Clear and display the 'fruits' set
fruits.clear()
print(f"After clearing, the fruits set contains:\n{fruits}")
