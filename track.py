import time
from datetime import datetime
import math
from typing import Tuple, List, Dict

class PetMonitoringSystem:
    def __init__(self):
        # Define safe temperature range (in Celsius)
        self.MIN_SAFE_TEMP = 15
        self.MAX_SAFE_TEMP = 30

        # Define restricted areas coordinates (example using lat/long)
        self.RESTRICTED_AREAS = [
            {
                'name': 'Cold Storage',
                'center': (40.7128, -74.0060),  # Example coordinates
                'radius': 10  # meters
            },
            {
                'name': 'Loading Dock',
                'center': (40.7130, -74.0062),
                'radius': 15
            }
        ]

        # Initialize alert system
        self.alert_active = False

    def calculate_distance(self, point1: Tuple[float, float], 
                         point2: Tuple[float, float]) -> float:
        """Calculate distance between two points using Haversine formula"""
        lat1, lon1 = point1
        lat2, lon2 = point2
        
        R = 6371000  # Earth's radius in meters

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    def is_in_restricted_area(self, pet_location: Tuple[float, float]) -> bool:
        """Check if the pet is in any restricted area"""
        for area in self.RESTRICTED_AREAS:
            distance = self.calculate_distance(pet_location, area['center'])
            if distance <= area['radius']:
                self.trigger_alert(area['name'])
                return True
        return False

    def check_temperature(self, temperature: float) -> bool:
        """Check if the temperature is within the safe range"""
        if temperature < self.MIN_SAFE_TEMP or temperature > self.MAX_SAFE_TEMP:
            self.trigger_temperature_alert(temperature)
            return False
        return True

    def trigger_alert(self, area_name: str):
        """Trigger an alert if the pet is in a restricted area"""
        self.alert_active = True
        print(f"Alert! Pet is in the restricted area: {area_name}")

    def trigger_temperature_alert(self, temperature: float):
        """Trigger an alert if the temperature is outside the safe range"""
        self.alert_active = True
        print(f"Alert! Temperature is out of safe range: {temperature}°C")

    def monitor_pet(self, pet_location: Tuple[float, float], temperature: float):
        """Monitor the pet's location and check for restricted areas and temperature"""
        if self.is_in_restricted_area(pet_location):
            print("Corrective action needed due to location!")
        elif not self.check_temperature(temperature):
            print("Corrective action needed due to temperature!")
        else:
            print("Pet is in a safe area with safe temperature.")