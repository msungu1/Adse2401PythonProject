# Import required modules
from pathlib import Path   # Pathlib provides an object-oriented way to handle filesystem paths
import json                # JSON module allows reading/writing JSON data

# ------------------------------------------------------------
# Function: save_car_details
# ------------------------------------------------------------
def save_car_details(file_path: Path, car_list: list):
    """
    Saves a list of car dictionaries to a JSON file.
    """
    try:
        # Ensure the parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Open the file in write mode and dump JSON data
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(car_list, file, indent=4)

        print(f"Car data successfully saved to {file_path}")
    except Exception as e:
        print(f"Sorry, something went wrong while saving car details.\n{e}")


# ------------------------------------------------------------
# Function: display_car_data
# ------------------------------------------------------------
def display_car_data(car_list: list):
    """
    Displays car details from a list of dictionaries.
    """
    for car in car_list:
        make = car.get("make", "Unknown")
        model = car.get("model", "Unknown")
        year = car.get("year", "Unknown")
        price = car.get("price", "N/A")
        print(f"Make: {make}, Model: {model}, Year: {year}, Price: {price}")


# ------------------------------------------------------------
# Function: load_car_details
# ------------------------------------------------------------
def load_car_details(file_path: Path):
    """
    Loads car details from a JSON file and returns them as a list of dictionaries.
    """
    try:
        with file_path.open("r", encoding="utf-8") as file:
            car_list = json.load(file)

        print("Car details loaded successfully:\n")
        display_car_data(car_list)  # Use the helper function

        return car_list

    except FileNotFoundError as fnf:
        print(f"Sorry, the file was not found.\n{fnf}")
        return []
    except json.JSONDecodeError as jde:
        print(f"Sorry, failed to load the JSON data.\n{jde}")
        return []
    except Exception as e:
        print(f"Sorry, error loading car data.\n{e}")
        return []


# ------------------------------------------------------------
# Main usage example
# ------------------------------------------------------------
if __name__ == "__main__":
    # Define the path one directory up into files/cars.json
    file_path = Path.cwd().parent / "files" / "cars.json"

    # Example car_list with some car dictionaries
    car_list = [
        {"make": "Toyota", "model": "Corolla", "year": 2020, "price": 20000},
        {"make": "Honda", "model": "Civic", "year": 2019, "price": 22000},
        {"make": "Ford", "model": "Focus", "year": 2018, "price": 18000}
    ]

    # 1. Save car details
    save_car_details(file_path, car_list)

    # 2. Load and display car details
    load_car_details(file_path)
