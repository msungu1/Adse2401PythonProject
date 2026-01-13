# Process script to demonstrate running multiple processes concurrently

import multiprocessing as mp


# Function to calculate the square of a number
def square(n):
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a pool of processes
    with mp.Pool() as pool:
        # Map the squared results
        squared_results = pool.map(square, numbers)

    print("Original numbers:", numbers)
    print("Squared results:", squared_results)
