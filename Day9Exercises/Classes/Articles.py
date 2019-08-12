bike_types = {'cross': 'Cross Bicycle', 'road': 'Road bicycle'}

 class Bike(object):
    def __init__(self, color, type, front_wheel, back_wheel, frame):
        self.handlebar = 'fitness'
        self.seat = 'classic, stock, seat'
        self.color = color
        self.type = type
        self.front_wheel = front_wheel
        self.back_wheel = back_wheel
        self.frame = frame

    def ride(self):
        """Ride this bike!"""
        print(f"I'm riding {self.color} bike")

    def dzwonek(self):
        """Depnij ten dzwonek"""
        print("Dryn, dryn")

class ElectricBike(Bike):
    def increase_motor_power(self):
        print("Motor power Increase")

class Wheel(object):
    def __init__(self, size, color='black'):
        self.company = size
        self.color = color


class Frame(object):
    def __init__(self, size, color, geometry):
        self.size = size
        self.color = color
        self.geometry = geometry



