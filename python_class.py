# Design Class
# Base Class: Gadget
class Gadget:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def gadget_info(self):
        return f"Brand: {self.brand}, Price: ${self.price}"


# Derived Class: Smartphone
class Smartphone(Gadget):
    def __init__(self, brand, price, model, camera_megapixels):
        super().__init__(brand, price)
        self.model = model
        self.camera_megapixels = camera_megapixels

    def smartphone_info(self):
        return f"{self.gadget_info()}, Model: {self.model}, Camera: {self.camera_megapixels} MP"


# Derived Class: Laptop
class Laptop(Gadget):
    def __init__(self, brand, price, ram, processor):
        super().__init__(brand, price)
        self.ram = ram
        self.processor = processor

    def laptop_info(self):
        return f"{self.gadget_info()}, RAM: {self.ram} GB, Processor: {self.processor}"


# Creating Objects
phone = Smartphone("Apple", 999, "iPhone 14", 48)
laptop = Laptop("Dell", 1200, 16, "Intel i7")

# Display Information
print(phone.smartphone_info())
print(laptop.laptop_info())



# Polymorphism Challenge
# Base Class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


# Derived Class: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Derived Class: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


# Using Polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
