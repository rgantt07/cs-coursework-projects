class Car:
    def __init__(self, make, model, year, rate):
        self.make = make
        self.model = model
        self.year = year
        self.rate = rate
        self.isRented = False

    def is_available(self):
        return self.isRented

    def set_rented(self, days):
        self.isRented = True
        print(f'{self.year} {self.make} {self.model} has been rented for {days} days.')
        print(f"Customer will be charged ${self.rate * days:.2f} at return")

    def set_returned(self):
        self.isRented = False
        print(f'{self.year} {self.make} {self.model} has been returned')

    def info(self):
        if not self.isRented:
            print(f'{self.year} {self.make} {self.model} - AVAILABLE, PER DAY RATE: ${self.rate:.2f}')
        else:
            print(f'{self.year} {self.make} {self.model} - RENTED')