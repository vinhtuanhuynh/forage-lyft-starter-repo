from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        sum_threshold = 3
        return sum(self.tire_wear) >= sum_threshold