import time
import pickle
import json

from model import Car
from view import ConsoleUI


class CarManager:
    def __init__(self, vehicles_list):
        self.vehicles_list = vehicles_list

    def filter_by_model(self, model):
        return [vehicle for vehicle in self.vehicles_list if isinstance(vehicle, Car) and vehicle.model == model]

    def filter_by_model_and_years(self, model, years):
        current_year = time.localtime().tm_year
        return [vehicle for vehicle in self.vehicles_list if isinstance(vehicle, Car) and vehicle.model == model and (current_year - vehicle.year) > years]

    def filter_by_year_and_price(self, year, price):
        return [vehicle for vehicle in self.vehicles_list if isinstance(vehicle, Car) and vehicle.year == year and vehicle.price > price]

    def show_all_vehicles(self):
        ConsoleUI.display_data(self.vehicles_list)

    def sort_by_price_ascending(self):
        self.vehicles_list.sort(key=lambda x: x.price)

    def sort_by_price_descending(self):
        self.vehicles_list.sort(key=lambda x: x.price, reverse=True)

    def sort_by_year_ascending(self):
        self.vehicles_list.sort(key=lambda x: x.year)

    def sort_by_year_descending(self):
        self.vehicles_list.sort(key=lambda x: x.year, reverse=True)

    def add_maintenance_to_car(self, car_id, maintenance_record):
        for vehicle in self.vehicles_list:
            if isinstance(vehicle, Car) and vehicle.id == car_id:
                vehicle.add_maintenance(maintenance_record)
                ConsoleUI.display_message("Maintenance record added successfully.")
                break
        else:
            ConsoleUI.display_message("Car not found.")

    def show_maintenance_history(self, car_id):
        for vehicle in self.vehicles_list:
            if isinstance(vehicle, Car) and vehicle.id == car_id:
                ConsoleUI.display_message("Maintenance history:")
                ConsoleUI.display_data(vehicle.get_maintenance_history())
                break
        else:
            ConsoleUI.display_message("Car not found.")

    def run(self):
        while True:
            ConsoleUI.display_menu()
            choice = ConsoleUI.get_input("Enter your choice (1-9): ")
            if choice == "1":
                car_id = int(ConsoleUI.get_input("Enter car ID: "))
                model = ConsoleUI.get_input("Enter car model: ")
                year = int(ConsoleUI.get_input("Enter car year: "))
                price = int(ConsoleUI.get_input("Enter car price: "))
                registration_number = ConsoleUI.get_input("Enter registration number: ")
                car = Car(car_id, model, year, price, registration_number)
                self.vehicles_list.append(car)
            elif choice == "2":
                car_id = int(ConsoleUI.get_input("Enter car ID to remove: "))
                self.vehicles_list = [vehicle for vehicle in self.vehicles_list if not (isinstance(vehicle, Car) and vehicle.id == car_id)]
            elif choice == "3":
                filename = ConsoleUI.get_input("Enter filename to save data to binary file: ")
                with open(filename, 'wb') as file:
                    pickle.dump(self.vehicles_list, file)
            elif choice == "4":
                filename = ConsoleUI.get_input("Enter filename to load data from binary file: ")
                with open(filename, 'rb') as file:
                    self.vehicles_list = pickle.load(file)
            elif choice == "5":
                filename = ConsoleUI.get_input("Enter filename to save data to JSON file: ")
                with open(filename, 'w') as file:
                    json.dump([vars(vehicle) for vehicle in self.vehicles_list], file)
            elif choice == "6":
                filename = ConsoleUI.get_input("Enter filename to load data from JSON file: ")
                with open(filename, 'r') as file:
                    data = json.load(file)
                    self.vehicles_list = [Car(vehicle_data['id'], vehicle_data['model'], vehicle_data['year'], vehicle_data['price'], vehicle_data['registration_number']) for vehicle_data in data]
            elif choice == "7":
                self.sort_by_price_ascending()
            elif choice == "8":
                self.sort_by_price_descending()
            elif choice == "9":
                self.sort_by_year_ascending()
            elif choice == "10":
                self.sort_by_year_descending()
            elif choice == "11":
                car_id = int(ConsoleUI.get_input("Enter the ID of the car: "))
                maintenance_record = ConsoleUI.get_input("Enter the maintenance record: ")
                self.add_maintenance_to_car(car_id, maintenance_record)
            elif choice == "12":
                car_id = int(ConsoleUI.get_input("Enter the ID of the car: "))
                self.show_maintenance_history(car_id)
            elif choice == "13":
                self.show_all_vehicles()
            elif choice == "14":
                break
            else:
                ConsoleUI.display_message("Invalid choice. Please enter a number from 1 to 14.")
