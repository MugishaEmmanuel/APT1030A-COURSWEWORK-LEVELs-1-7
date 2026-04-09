BASE_FARE = 200
COST_PER_KM = 50

compute_fare = lambda distance: BASE_FARE + (COST_PER_KM * distance)

try:
    distance = float(input("Enter distance (km): "))
    print(f"Total fare: KES {compute_fare(distance):.0f}")
except ValueError:
    print("Invalid input. Please enter a number.")