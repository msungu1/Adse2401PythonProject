# Python script to demonstrate the filter() function

# list of fibonacci numbers -> golden ratio 1.61803
numbers = [1,1,2,3,5,8,13,21,34,55,89,144]

# get and display a list of odd fibonacci numbers using the filter() function
odd_fibonacci = list(filter(lambda x: x % 2 == 1, numbers))
print(f"Fibonacci numbers:\n{numbers}\nOdd Fibonacci numbers:\n{odd_fibonacci}")

# set of student names
students_names = {
    "Abigail","Bernice","Charlene","Denise","Sue","Jim","Mark","Micha",
    "Wiliam","Jane","Xi","Alfred","Hilarry","Anthony","Brigid","Mitchell","Alice"
}

# use the filter() function to get and display the names starting with 'A'
filtered_names = list(filter(lambda name: name.startswith('A'), students_names))
print(f"All student names:\n{students_names}\nNames starting with 'A':\n{filtered_names}")

# function to determine whether a number is prime or not
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# set the range of numbers that we'd like to get prime numbers
num_range = range(1, 78)
prime_numbers = list(filter(is_prime, num_range))
print(f"The prime numbers between 1 and 78 are:\n{prime_numbers}")

