from controller import CarManager
from model import Car

if __name__ == "__main__":
    car1 = Car(1, "Toyota Corolla", 2018, 15000, "AB1234CD")
    car2 = Car(2, "Honda Civic", 2015, 12000, "EF5678GH")
    car3 = Car(3, "Ford Mustang", 2019, 30000, "IJ91011KL")
    car4 = Car(4, "Toyota Camry", 2017, 18000, "DD1213DD")
    car5 = Car(5, "Toyota Camry", 2018, 20000, "KK1213OP")
    # vehicles_list = [car1, car2, car3, car4, car5]
    vehicles_list=[]
    car_manager = CarManager(vehicles_list)
    car_manager.run()
