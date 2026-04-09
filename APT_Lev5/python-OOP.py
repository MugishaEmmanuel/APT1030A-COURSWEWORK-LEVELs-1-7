class RidePricingEngine:
    BASE_FARE = 200      # KES
    COST_PER_KM = 50     # KES

    def __init__(self, distance_km: float):
        self.distance_km = distance_km

    def compute_fare(self) -> float:
        return self.BASE_FARE + (self.COST_PER_KM * self.distance_km)

    def __repr__(self):
        return f"Ride({self.distance_km}km) → KES {self.compute_fare():.0f}"


try:
    distance = float(input("Enter distance (km): "))
    if distance <= 0:
        print("Distance must be greater than 0.")
    else:
        ride = RidePricingEngine(distance_km=distance)
        print(ride.compute_fare())
        print(ride)
except ValueError:
    print("Invalid input. Please enter a numeric value.")