# Python List is a built-in data type that presents an ordered collection of items/elements.
# Lists allow duplicates and are mutable (i.e., their elements can be modified, added, or removed).
# Lists are created using [] or the list() constructor.
# A sample list and some of its operations are given below.

# Create a list of fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"]

# Display the number of items/elements in the fruit list
print("Number of fruits in the list:", len(fruits))

# Display the fruits in the fruit list
print(f"Fruits in the list: {fruits}")

# Display the number of items again (to confirm)
print("Total number of fruits:", len(fruits))

# Create another list of fruits
more_fruits = ["Strawberry", "Kiwi", "Papaya"]

# Add the content of another list to the fruit list
fruits.extend(more_fruits)

# Display the updated fruit list
print("\nUpdated Fruit List:", fruits)

# Display the new number of items
print("Total number of fruits after adding more:", len(fruits))

# Insert a fruit at a specific index
fruits.insert(2, "Watermelon")   # inserts at index 2 (third position)

# Display the fruit list after insertion
print("\nFruit List after inserting 'Watermelon' at index 2:", fruits)

# Display the new number of items again
print("Total number of fruits after insertion:", len(fruits))

# --- Removal operations ---
# Remove a fruit item at a given index
removed_fruit = fruits.pop(3)   # removes the fruit at index 3
print(f"\nRemoved fruit at index 3: {removed_fruit}")
print("Fruit List after removing by index:", fruits)

# Remove a specific fruit by name
fruits.remove("Banana")         # removes the first occurrence of "Banana"
print("\nFruit List after removing 'Banana':", fruits)

# Get and display the index of an item/element in the list
index_of_mango = fruits.index("Mango")
print(f"\nThe index of 'Mango' in the list is: {index_of_mango}")

print("Original Fruit List:", fruits)

# Sort the fruits in ascending (alphabetical) order
fruits.sort()

# Display the sorted fruit list
print("\nFruit List in Alphabetical Order:", fruits)

# Display each fruit on a separate line
print("\nFruits in Alphabetical Order (one per line):")
for fruit in fruits:
    print(fruit)

# Display every third fruit in the fruit list
print("\nEvery third fruit in the list:", fruits[2::3])

# Get and display the minimum and maximum items/elements in the list
# (least and highest fruits letterwise)
print(f"\nThe least fruit letterwise is: {min(fruits)}")
print(f"The highest fruit letterwise is: {max(fruits)}")

# Display every fruit starting from the second one
print("\nFruits starting from the second one:", fruits[1:])

# Display all the fruits apart from the first and last one
print(f"\nAll the fruits apart from the first and last one are: {fruits[1:-1]}")

# Display fruits in reverse order starting from the third last fruit
print(f"\nFruits in reverse order starting from the third last are: {fruits[-3::-1]}")

# Get and display an empty slice from the fruit list
print(f"\nThe empty slice from the fruit list is: {fruits[5:5]}")


