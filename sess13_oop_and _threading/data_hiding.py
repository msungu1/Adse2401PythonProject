# Python script to demonstrate OOP concepts:
# Data hiding, Overloading (simulation), and Overriding

class Animal:
    def __init__(self, name, age):
        self._name = name        # protected by convention
        self.__age = age         # private (name mangled to _Animal__age)

    # Getter for private variable
    def get_age(self):
        return self.__age

    # Base method
    def speak(self):
        return f"{self._name} makes a sound"

    # Simulated overloading using *args
    def make_sound(self, *args):
        base_sound = self.speak()
        if not args:
            return base_sound
        elif len(args) == 1 and isinstance(args[0], (int, float)):
            volume = args[0]
            return f"{base_sound} at volume {volume}"
        else:
            extras = ", ".join(map(str, args))
            return f"{base_sound} with extras: {extras}"


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # Overriding speak method
    def speak(self):
        return f"{self._name} barks 'WOOF' loudly!"


# Instantiate a Dog object and call the various methods
dog = Dog("Jimmy", 5)

print(dog.speak())                # overriding Animal's speak() method
print(dog.make_sound())           # no arguments (default behavior)
print(dog.make_sound(8))          # simulated overloading with volume
print(dog.make_sound(12, "with toy", "excited"))  # multiple arguments
print(f"Accessing protected name: {dog._name}")   # conventionally protected
print(f"Accessing private age via getter: {dog.get_age()}")  # proper access
