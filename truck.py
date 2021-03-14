class Truck:

    def __init__(self, truck_num):
        """Initializes truck object with default values and truck number"""
        self.truck_num = truck_num
        self.route = []
        self.mileage = 0.0
        self.mph = 18
        self.depart = None
        self.arrive = None
