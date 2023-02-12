from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @abstractmethod
    def wheels_num(self):
        raise NotImplementedError("You have to implement wheels_num()")
        # return 0

    def vehicle_type(self):
        return f"{self.brand_name} {self.__class__.__name__}"

    @property
    def is_motorcycle(self):
        self.wh_num = self.wheels_num()
        if self.wh_num == 2:
            return True
        else:
            return False

    @property
    def purchase_price(self):
        self.purc_price = self.base_price - 0.1 * self.mileage
        if self.purc_price <= 100_000:
            return 100_000
        else:
            return self.purc_price


class Car(Vehicle):
    def wheels_num(self):
        return 4


class Motorcycle(Vehicle):
    def wheels_num(self):
        return 2


class Truck(Vehicle):
    def wheels_num(self):
        return 10


class Bus(Vehicle):
    def wheels_num(self):
        return 6


vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
        print(
            f"Vehicle type={vehicle.vehicle_type()}\n"
            f"Is motorcycle={vehicle.is_motorcycle}\n"
            f"Purchase price={vehicle.purchase_price}\n"
        )

