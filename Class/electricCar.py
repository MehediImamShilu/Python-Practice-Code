# Python crush course
# An example of Inheritance

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increase_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        """Initialize battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement to describe battery size."""
        print("This car has " + str(self.battery_size) + " KWH battery.")

    def get_range(self):
        """Initialize car battery range capacity."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 280

        massage = "This car can travel approximately " + str(range)
        massage += " miles on full charge."
        print(massage)


class Electric_Car(Car):
    """Represent aspect of a car, specific to electric vehicle."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        & initialize attributes specific to electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


the_one_car = Electric_Car("The One", "Model PRO", 2025)
print(the_one_car.get_descriptive_name())
the_one_car.battery.describe_battery()
the_one_car.battery.get_range()
