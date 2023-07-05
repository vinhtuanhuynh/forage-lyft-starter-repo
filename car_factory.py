from engine.capulet_engine import CapuletEngine 
from engine.sternman_engine import SternmanEngine 
from engine.willoughby_engine import WilloughbyEngine 
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        calliope = Car(engine, battery)
        return calliope

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        glissade = Car(engine, battery)
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        palindrome = Car(engine, battery)
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        rorschach = Car(engine, battery)
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        thovex = Car(engine, battery)
        return thovex
