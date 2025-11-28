# python script demonstarting how to import a module and use its code in the current script

# import(bring in) the code from the greeting module
from greetings import greet

# prompt the user for their name
username = input("What is your name? ")

# use the function from the grretings module to great the user
print (greet(username))