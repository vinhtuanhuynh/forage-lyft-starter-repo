from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        threshold = 0.9
        for tire in self.tire_wear:
            if tire >= threshold:
                return True
        return False
    