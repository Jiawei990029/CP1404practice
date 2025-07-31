from prac_09.taxi import Taxi
import random

class UnreliableCar(Taxi):

    def __init__(self, name, fuel, price_per_km=1.23, reliability=0):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven
        return 0