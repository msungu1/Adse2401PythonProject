class PlusCounter:
    """
    A simple iterator that counts up from a starting number to an end number,
    incrementing by a specified step (default = 1).

    Attributes:
        current (int): current value in the iteration
        end (int): end value in the iteration
        step (int): step value in the iteration
    """

    def __init__(self, start, end, step=1):
        """
        Initializes the PlusCounter object.

        Args:
            start (int): start value of the counter
            end (int): end value of the counter
            step (int): step value of the counter
        """
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """
        Returns the next value in the iterator.

        Raises:
            StopIteration: if the current value exceeds the end value.
        """
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value


# Example usage:

# Counter from 1 to 10
print("Counting from 1 to 10:")
my_counter = PlusCounter(1, 10)
for num in my_counter:
    print(num)

print("\nMultiples of 5 from 1 to 75:")
my_counter2 = PlusCounter(5, 75, 5)
for num in my_counter2:
    print(num)
