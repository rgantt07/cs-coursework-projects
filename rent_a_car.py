from OwlRental import OwlRental

owlCars = OwlRental()
owlCars.add_car("Toyota", "Corolla", 2025, 49.99)
owlCars.add_car("Honda", "Civic", 2023, 45.50)
owlCars.add_car("Tesla", "Model 3", 2023, 119.00)

choice = 0
print("[Owl Rent-a-Car]")
while choice != 4:
    print("1. Rent")
    print("2. Return")
    print("3. View cars")
    print("4. Exit")
    choice = int(input("> "))

    if choice == 1:
        print("")
        owlCars.list_cars()
        index = int(input("Select an index: "))
        days = int(input("How many day(s)?: "))
        owlCars.rent_car(index, days)
        print("")
    elif choice == 2:
        print("")
        owlCars.list_cars()
        index = int(input("Select an index: "))
        owlCars.return_car(index)
        print("")
    elif choice == 3:
        print("")
        owlCars.list_cars()
        print("")
