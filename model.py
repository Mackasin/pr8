from abc import ABC, abstractmethod
import time


class Vehicle(ABC):
    def __init__(self, vehicle_id, model, year, price, registration_number):
        self.id = vehicle_id
        self.model = model
        self.year = year
        self.price = price
        self.registration_number = registration_number

    @abstractmethod
    def get_info(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_id, model, year, price, registration_number):
        super().__init__(vehicle_id, model, year, price, registration_number)
        self.__maintenance_history = [] 

    def get_info(self):
        return f"Car ID: {self.id}, Model: {self.model}, Year: {self.year}, Price: {self.price}, Registration Number: {self.registration_number}"

    def __str__(self):
        return f"Car ID: {self.id}, Model: {self.model}, Year: {self.year}, Price: {self.price}, Registration Number: {self.registration_number}"

    def add_maintenance(self, maintenance_record):
        self.__maintenance_history.append(maintenance_record)  # Додавання запису про технічне обслуговування

    def get_maintenance_history(self):
        return self.__maintenance_history  # Отримання історії технічного обслуговування

    def __eq__(self, other):
        return isinstance(other, Car) and self.id == other.id

    def __lt__(self, other):
        return isinstance(other, Car) and self.price < other.price

    def __gt__(self, other):
        return isinstance(other, Car) and self.price > other.price
