from Car import Car

class OwlRental:
    def __init__(self):
        self.depot = []

    def add_car(self, make, model, year, rate):
        self.depot.append(Car(make, model, year, rate))

    def list_cars(self):
        index = 0
        for car in self.depot:
            print(index, "-", end = ' ')
            car.info()
            index += 1

    def rent_car(self, index, days):
        if self.depot[index].isRented:
            print("Error: Car is already rented")
        else:
            Car.set_rented(self.depot[index], days)

    def return_car(self, index):
        if not self.depot[index].isRented:
            print("Error: Car is not rented")
        else:
            Car.set_returned(self.depot[index])