# Python script to demonstrate the map() function

# set of fibonacci numbers -> golden ratio 1.61803
numbers = sorted(set([1,1,2,3,5,8,13,21,34,55,89,144]))

# get and display the triple of each of the fibonacci numbers in the above set
tripled_num = sorted(set(map(lambda x: x * 3, numbers)))

print(f"Set of Fibonacci numbers:\n{numbers}"
      f"\nSet of tripled Fibonacci numbers:\n{tripled_num}")

# list of names and ages
names = ['Abigail','Bernice','Charlene','Denise']
ages = [21,24,22,19]

# use the map function to combine the above names and ages for each person
combined_data = list(map(lambda name, age: f"{name} ({age})", names, ages))

print(f"Combined names and ages:\n{combined_data}")
