class ConsoleUI:
    @staticmethod
    def display_menu():
        print("1. Add new car")
        print("2. Remove car")
        print("3. Save data to binary file")
        print("4. Load data from binary file")
        print("5. Save data to JSON file")
        print("6. Load data from JSON file")
        print("7. Sort by price (ascending)")
        print("8. Sort by price (descending)")
        print("9. Sort by year (ascending)")
        print("10. Sort by year (descending)")
        print("11. Add maintenance record to a car")
        print("12. Show maintenance history of a car")
        print("13. Show all vehicles")
        print("14. Exit")

    @staticmethod
    def get_input(message):
        return input(message)

    @staticmethod
    def display_data(data):
        for item in data:
            print(item)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_error(message):
        print(f"Error: {message}")
