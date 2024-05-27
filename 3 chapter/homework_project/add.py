class Car:
    """Create a car"""

    def __init__(self, model, year, engine_volume, price, mileage):
        """Initializing the car's attributes"""
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def car_information(self):
        """Getting the car's description"""
        print(f'This is a {self.model}, the {str(self.year)} release, the engine volume is {str(self.engine_volume)}L, '
              f'the price is {str(self.price)}$, the mileage is {str(self.mileage)}km, it has {str(self.wheels)} wheels')


class Truck(Car):
    """Create a truck"""

    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8

    def get_wheels_quantity(self):
        """Get the wheels quantity"""
        print(f'The truck has {str(self.wheels)} wheels')

    def truck_information(self):
        """Getting the truck's description"""
        print(f'This is a {self.model}, the {str(self.year)} release, the engine volume is {str(self.engine_volume)}L, '
              f'the price is {str(self.price)}$, the mileage is {str(self.mileage)}km, it has {str(self.wheels)} wheels')



