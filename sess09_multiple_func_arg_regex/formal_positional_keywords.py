# Python script to demonstrate the use of formal, positional, and keyword arguments in a function

# function definition
def profile(name, *args, **kwargs):
    # formal argument: name
    print(f"Name: {name}")

    # positional arguments: hobbies
    if args:
        print("Hobbies:")
        for hobby in args:
            print(f"- {hobby}")

    # keyword arguments: other info
    if kwargs:
        print("Other info:")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")


# function call/invocation
profile(
    "Robert",  # formal argument
    "Cooking", "Sleeping", "Traveling",  # positional arguments
    gender="Male", age=16, password="mzungu", job="IT Lecturer", city="Mombasa", country="Kenya"  # keyword arguments
)
