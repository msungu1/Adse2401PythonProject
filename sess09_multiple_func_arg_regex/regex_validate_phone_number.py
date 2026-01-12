# Python script/file to validate a Kenyan phone number using regular expressions (regex)

import re

# function to validate the phone number
def validate_phone_number(phone_number):
    """
    Validates whether a given phone number is a valid Kenyan phone number.

    The phone number must:
    - Start with the country code '+254'
    - Optionally include spaces after the country code or carrier code
    - Include a valid 3-digit carrier code starting with digits 1 to 7
    - Be followed by exactly 6 digits (total length = 9 digits after +254)

    Parameters:
        phone_number (str): The phone number to validate. Should be in international format (+254...).

    Returns:
        None: Prints a message indicating whether the phone number is valid or not.
    """

    # Correct regex pattern
    pattern = r"^\+254\s?[1-7]\d{2}\s?\d{6}$"

    if not phone_number:
        print("Invalid phone number: empty input")
        return

    # compare the input phone number and the pattern and display an apt message
    if re.match(pattern, phone_number):
        print(f"The number {phone_number} is a valid Kenyan phone number.")
    else:
        print(f"The number {phone_number} is NOT a valid Kenyan phone number.")

# Prompt the user for their phone number
phone_number = input("Enter a phone number and I will tell you if it's a Kenyan number: ")
validate_phone_number(phone_number)
