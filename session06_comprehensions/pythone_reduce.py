# Python script to demonstrate the reduce() function

from functools import reduce

# A list of numbers to be manipulated using the reduce function
numbers = [17, 45, 23, 68, 144, 8, 51]

# get the largest number from the numbers list using the reduce() function
largest_num = reduce(lambda x, y: max(x, y), numbers)

# get the least number from the numbers list using the reduce() function 
least_num = reduce(lambda x, y: min(x, y), numbers)

# obtain the product of all numbers in the list using the reduce() function 
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# obtain the sum of all the numbers in the list using the reduce() function 
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# display the results
print(f"The list of numbers is:\n{numbers}")
print(f"The sum of the numbers is:\n{sum_of_numbers}")
print(f"The largest number is:\n{largest_num}")
print(f"The least number is:\n{least_num}")
print(f"The product of the numbers is:\n{product_of_numbers}")
