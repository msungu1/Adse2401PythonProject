class Student:
    """
    Represents a student in a learning institution.

    Attributes:
        student_no (str): The student's unique identifier.
        name (str): The student's name.
        birthdate (date): The student's date of birth.
        gender (str): The student's gender ('male' or 'female').
        city (str): The student's city of residence.
    """

    def __init__(self, student_no, name, birthdate, gender, city):
        self.student_no = student_no
        self.name = name
        self.birthdate = birthdate
        self.gender = self._validate_gender(gender)
        self.city = city

    def _validate_gender(self, gender):
        if gender.lower() not in ['male', 'female']:
            raise ValueError("Gender must be either 'male' or 'female'")
        return gender.lower()

    def __str__(self):
        return (f"Student No: {self.student_no}, "
                f"Name: {self.name}, "
                f"Birthdate: {self.birthdate}, "
                f"Gender: {self.gender}, "
                f"City: {self.city}")
